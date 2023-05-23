"""
Leetcode 36 (Medium): Valid Sudoku

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
validated according to the following rules:

 Each row must contain the digits 1-9 without repetition.
 Each column must contain the digits 1-9 without repetition.
 Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
without repetition.

 Note:
 A Sudoku board (partially filled) could be valid but is not necessarily
solvable.
 Only the filled cells need to be validated according to the mentioned rules.

 Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

 Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner
being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is
invalid.

 Constraints:
 board.length == 9
 board[i].length == 9
 board[i][j] is a digit 1-9 or '.'.
"""

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
                    for x in range(i, i+3):
                        for y in range(j, j+3):
                            square.append(board[x][y])
                    if not is_valid(square):
                        return False
            return True

        def is_valid(values):
            nums = [value for value in values if value != "."]
            return len(nums) == len(set(nums))

        return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)
