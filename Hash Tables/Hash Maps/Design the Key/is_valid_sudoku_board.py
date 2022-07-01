"""
    PROMPT:
            Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
                Each row must contain the digits 1-9 without repetition.
                Each column must contain the digits 1-9 without repetition.
                Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
            
            Note:
                A Sudoku board (partially filled) could be valid but is not necessarily solvable.
                Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sudoku = dict()
        for y in range(9):
            for x in range(9):
                
                # Shorthand
                cell = board[y][x]
                
                # Initialize the row counter
                if x == 0:
                    sudoku["row"] = set()
                # Initialize each column counter
                if y == 0:
                    sudoku[x] = set()
                # Initialize 3 counters for boxes -> 
                # [x: 0-3 & y: 0-3], [x: 2-5 & y: 0-3], [x: 6-8 & y: 0-3], etc...
                if (x == 0) and (y % 3 == 0):
                    sudoku["first"] = set()
                    sudoku["second"] = set()
                    sudoku["third"] = set()
                
                # Skip tracking on empty cells
                if cell == '.':
                    continue
                
                # Determine which box we are in; Can definitely optimize these box interactions
                if x in {0,1,2}:
                    box = "first"
                elif x in {3,4,5}:
                    box = "second"
                else:
                    box = "third"
                
                # If the number already exists in it's row, column, or box; return False
                if (cell in sudoku["row"]) or (cell in sudoku[x]) or (cell in sudoku[box]):
                    return False
                
                # Add cell to it's row, column, or box; return False
                sudoku["row"].add(cell)
                sudoku[x].add(cell)
                sudoku[box].add(cell)
        
        # Algorithm executed flawlessly
        return True
