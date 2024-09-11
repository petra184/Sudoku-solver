# Sudoku Solver Project
This project is a graphical Sudoku solver built using Python and Pygame. It features an interactive grid where users can input numbers and solve Sudoku puzzles using the backtracking algorithm. The interface is designed for ease of use, allowing players to solve puzzles manually or automatically.

## Features
- Interactive 9x9 Sudoku grid where users can input their numbers.
- Two buttons: **Solve** (to solve the puzzle) and **Clear** (to reset the grid).
- Uses backtracking to solve the puzzle efficiently.
- User-friendly keyboard and mouse controls to navigate and input values.
- Input validation to prevent illegal moves in Sudoku.

## How to Use
1. **Enter numbers** into the grid by clicking on a cell and typing the desired number.
2. Press **Solve** to use the backtracking algorithm to automatically fill in the remaining cells.
3. Use the **Clear** button to reset the grid and start over.
4. Use arrow keys to move between cells, and the backspace key to delete entries.

## Requirements
- Python 3.x
- Pygame library

Run the program and interact with the grid using your mouse and keyboard to solve your Sudoku puzzles!

## Algorithm
The Sudoku solver uses the **backtracking algorithm** to fill in the puzzle. It works by trying numbers in empty cells and backtracking when a number leads to an invalid configuration, ensuring the correct solution is found.

