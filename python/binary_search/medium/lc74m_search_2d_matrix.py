# LC 74 (Medium): Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(logm + logn) = O(log(m*n)) for m-rows, n-cols
        # Space: O(1)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top_row = 0
        bot_row = ROWS - 1

        # Use Binary Search log(m) on the col values
        while top_row <= bot_row:
            mid_row = (top_row + bot_row) // 2

            # if target value is greater than last value on the row
            # We know its not on the row since the matrix is sorted
            if target > matrix[mid_row][-1]:
                top_row = mid_row + 1  # move to next row down

            # if trgt is less than first num on the row
            # we know its not on the row so we move the bottom (ptr) up
            elif target < matrix[mid_row][0]:
                bot_row = mid_row - 1

            # cond where we know its on the row (or not in the matrix)
            else:
                break

        # if we iterated and moved the top_row past the bot_row
        # we know the value did not fall in the bounds of any row, so we return
        if not (top_row <= bot_row):
            return False

        left = 0
        right = COLS - 1
        search_row = (top_row + bot_row) // 2
        # Use Binary search log(n) on the values in the found search_row
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[search_row][mid]:
                left = mid + 1
            elif target < matrix[search_row][mid]:
                right = mid - 1
            else:
                return True
        return False

    def searchMatrix0(self, matrix: List[List[int]], target: int) -> bool:
        # Time: O(m * n) where m is number of rows, n number of cols
        # Space: O(1)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                value = matrix[i][j]
                if value == target:
                    return True
        return False
