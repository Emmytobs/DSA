class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        visited_cells = set()

        def dfs_recursive(r: int, c: int):
            if (
                r < 0 or r == ROWS or \
                c < 0 or c == COLS or \
                grid[r][c] == 0 or \
                (r, c) in visited_cells
            ):
                return 0
            visited_cells.add((r, c))

            return 1 + (
                dfs_recursive(r + 1, c) +
                dfs_recursive(r - 1, c) +
                dfs_recursive(r, c + 1) +
                dfs_recursive(r, c - 1)
            )
        def dfs_iterative(r: int, c: int):
            stack = [[r, c]]
            area = 0

            while len(stack):
                r, c = stack.pop()
                if (
                    r < 0 or r == ROWS or \
                    c < 0 or c == COLS or \
                    grid[r][c] == 0 or \
                    (r, c) in visited_cells
                ):
                    continue
                stack.extend([
                    [r + 1, c],
                    [r - 1, c],
                    [r, c + 1],
                    [r, c - 1]
                ])
                area += 1
                visited_cells.add((r, c))
            return area
                
        max_area = 0

        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs_iterative(r, c))
        
        return max_area
                