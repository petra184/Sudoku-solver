import pygame as pg
import sys
from sudoku import *

pg.init()
screen = pg.display.set_mode([700, 600])
pg.display.set_caption('SUDOKU SOLVER')
clock = pg.time.Clock()
base_font = pg.font.Font(None, 32)

user_text = [['' for i in range(9)] for i in range(9)] 
active = [[False for i in range(9)] for i in range(9)]
active_color = pg.Color(230, 230, 230)
def text_grid(input_rect, active):
    side = 0
    down = 0

    for i in range(9):
        for j in range(9):
            text_surface = base_font.render(user_text[i][j], True, (0, 0, 0))
            input_rect = pg.Rect(125 + side, 20 + down, 40, 40)
            if active[i][j]:
                color = active_color
            else: color = pg.Color("White")
            pg.draw.rect(screen, color, input_rect)
            text_x = input_rect.x + (input_rect.width - text_surface.get_width()) // 2
            text_y = input_rect.y + (input_rect.height - text_surface.get_height()) // 2
            screen.blit(text_surface, (text_x, text_y))
            side+=50
        down+=50
        side = 0

def grid():
    side = 0
    down = 0
    for i in range(9):
        for j in range(9):
            pg.draw.rect(screen, pg.Color("Black"), pg.Rect(120+side,15+down,50,50),1)
            side+=50
        down+=50
        side = 0
    down = 0
    left = 0
    for i in range(2):
        pg.draw.line(screen, pg.Color("Black"), [120, 165 + down], [568, 165 + down], 4)
        pg.draw.line(screen, pg.Color("Black"), [270 + left, 15], [270 + left, 460], 4)
        down+= 150
        left+=150

def button():
    font = pg.font.Font(None, 24)
    button_surface1 = pg.Surface((100, 50)) 
    button_surface1.fill((173, 216, 230))
    pg.draw.rect(button_surface1, pg.Color("Black"), pg.Rect(0, 0, 100, 50), 1)
    text1 = font.render("SOLVE", True, (0, 0, 0))  
    text_rect1 = text1.get_rect(center=(button_surface1.get_width() // 2, button_surface1.get_height() // 2))
    button_rect_solve = pg.Rect(220, 500, 50, 50)
    button_surface1.blit(text1, text_rect1)
    screen.blit(button_surface1, (button_rect_solve.x, button_rect_solve.y))
    return button_rect_solve

def clear_b():
    font = pg.font.Font(None, 24)
    button_surface = pg.Surface((100, 50)) 
    button_surface.fill((173, 216, 230))
    pg.draw.rect(button_surface, pg.Color("Black"), pg.Rect(0, 0, 100, 50), 1)
    text = font.render("CLEAR", True, (0, 0, 0))  
    text_rect = text.get_rect(center=(button_surface.get_width() // 2, button_surface.get_height() // 2))
    button_rect_clear = pg.Rect(360, 500, 50, 50)
    button_surface.blit(text, text_rect)
    screen.blit(button_surface, (button_rect_clear.x, button_rect_clear.y))

    return button_rect_clear

def get_inputs(ff):
    grid = [[0 for i in range(9)] for i in range(9)]
    for i in range(9):
        for j in range(9):
            if ff[i][j]=='':
                continue
            else: grid[i][j] = int(ff[i][j])
    solve(grid)
    for i in range(9):
        for j in range(9):
            user_text[i][j] = str(grid[i][j])

def control(direction):
    global active
    for i in range(9):
        for j in range(9):
            if active[i][j]:
                active[i][j] = False
                if direction == "left" and j > 0:
                    active[i][j - 1] = True
                elif direction == "right" and j < 8:
                    active[i][j + 1] = True
                elif direction == "up" and i > 0:
                    active[i - 1][j] = True
                elif direction == "down" and i < 8:
                    active[i + 1][j] = True
                return
            
def main():
    global active, user_text
    input_rect = pg.Rect(125, 20, 40, 40)
    active[4][4] = True
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect_solve.collidepoint(event.pos):
                    get_inputs(user_text)
            
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if button_rect_clear.collidepoint(event.pos):
                    for i in range(9):
                        for j in range(9):
                            user_text[i][j] = ''

            if event.type == pg.MOUSEBUTTONDOWN:
                for i in range(9):
                    for j in range(9):
                        input_rect = pg.Rect(125 + j * 50, 20 + i * 50, 40, 40)
                        if input_rect.collidepoint(event.pos):
                            active[i][j] = True
                        else:
                            active[i][j] = False

            if event.type == pg.KEYDOWN:
                for i in range(9):
                    for j in range(9):
                        if active[i][j]:
                            if event.key == pg.K_BACKSPACE:
                                user_text[i][j] = user_text[i][j][:-1]
                            elif event.unicode.isdigit() and 1 <= int(event.unicode) <= 9:
                                num = int(event.unicode)
                                if valid_move(user_text, i, j, num):
                                    user_text[i][j] = event.unicode

                if event.key == pg.K_RETURN:
                    get_inputs(user_text)
                
                if event.key == pg.K_LEFT:
                    control("left")
                if event.key == pg.K_RIGHT:
                    control("right")
                if event.key == pg.K_UP:
                    control("up")
                if event.key == pg.K_DOWN:
                    control("down")
            

        screen.fill(pg.Color("White"))
        pg.draw.rect(screen, pg.Color("Black"), pg.Rect(120, 15, 450, 450), 4)
        grid()
        button_rect_solve = button()
        button_rect_clear = clear_b()
        text_grid(input_rect, active)

        pg.display.flip()

        clock.tick(60)


main()