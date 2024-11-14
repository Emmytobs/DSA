#
# @lc app=leetcode id=1391 lang=python3
#
# [1391] Check if There is a Valid Path in a Grid
#

# @lc code=start
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        valid_directions = {
            1: [(0,-1), (0,1)],
            2: [(-1,0), (1,0)],
            3: [(0,-1), (1,0)],
            4: [(0,1), (1,0)],
            5: [(0,-1), (-1,0)],
            6: [(0,1), (-1,0)],
        }

        ROWS = len(grid)
        COLS = len(grid[0])
        destination = (ROWS-1, COLS-1)
        visited_cells = set()

        def dfs(cell: tuple) -> bool:
            visited_cells.add(cell)
            if cell == destination:
                return True
            [m, n] = cell
            directions = valid_directions[grid[m][n]]
            for d in directions:
                dm, dn = m + d[0], n + d[1]
                if (
                    0 <= dm < ROWS and 
                    0 <= dn < COLS and
                    # Determines valid path by checking if the inverse of the direction is in the next cell.
                    (-d[0], -d[1]) in valid_directions[grid[dm][dn]] and 
                    (dm, dn) not in visited_cells
                ):
                    if dfs((dm, dn)):
                        return True
            return False

        return dfs((0,0))
# @lc code=end

