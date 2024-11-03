"""
Leetcode 200 (Medium): Number of Island
Given an m x n 2D binary grid `grid` which represents a map of '1's (land) and '0's (water),
return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Depth-First Search
        # Time-Complexity: O(m * n) where m is num of rows, n is num of cols
        # Space-Complexity O(m * n) where m is num of rows, n is num of cols
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        def dfs(r: int, c: int):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != "1":
                return
            else:
                grid[r][c] = "0"
                dfs(r, c + 1)  # right
                dfs(r + 1, c)  # down
                dfs(r, c - 1)  # left
                dfs(r - 1, c)  # up

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)

        return num_islands

    def numIslands1(self, grid: List[List[str]]) -> int:
        # Breadth-First Search
        # Time-Complexity: O(m * n) where m is num of rows, n is num of cols
        # Space-Complexity O(m * n) where m is num of rows, n is num of cols
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        def bfs(r: int, c: int):
            q = collections.deque()
            grid[r][c] = "0"
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if (new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols
                            or grid[new_row][new_col] != "1"
                    ):
                        continue
                    q.append((new_row, new_col))
                    grid[new_row][new_col] = "0"

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c)

        return num_islands
