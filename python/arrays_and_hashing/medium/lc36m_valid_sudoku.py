# LC 36 (Medium): Valid Sudoku
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        :param List[List[str]] board: 9x9 Sudoku board
        :return: bool: True if board is valid, False otherwise
        Time Complexity: O(3N) = O(N) since we iterate over the board 3 times
        Space Complexity: O(3N) = O(N) since we store the rows, columns, and squares in 3 separate lists
        """

        def is_valid_row(board):
            for row in board:
                if not is_valid(row):
                    return False
            return True

        def is_valid_col(board):
            for col in zip(*board):
                if not is_valid(col):
                    return False
            return True

        def is_valid_square(board):
            for i in (0, 3, 6):
                for j in (0, 3, 6):
                    square = []
                    for x in range(i, i + 3):
                        for y in range(j, j + 3):
                            square.append(board[x][y])
                    if not is_valid(square):
                        return False
            return True

        def is_valid(values):
            nums = [value for value in values if value != "."]
            return len(nums) == len(set(nums))

        return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)
