function maxAreaOfIsland(grid: number[][]): number {
  const ROWS = grid.length;
  const COLS = grid[0].length;

  const visitedCells: number[][] = []
  function cellHasBeenVisited(r: number, c: number) {
      return visitedCells.some(([_r, _c]) => _r == r && _c == c)
  }

  function dfsIterative(r: number, c: number) {
      let area = 0;
      const stack = [[r, c]]

      while (stack.length) {
          const [r, c] = stack.pop();
          if (
              r < 0 || r == ROWS ||
              c < 0 || c == COLS ||
              grid[r][c] == 0 ||
              cellHasBeenVisited(r, c)
          ) continue;

          stack.push(
              [r + 1, c],
              [r - 1, c],
              [r, c + 1],
              [r, c - 1],
          );
          visitedCells.push([r, c])
          area += 1
      }
      return area;
  }

  let maxArea = 0

  for (let r = 0; r < grid.length; r++) {
      for (let c = 0; c < grid[r].length; c++) {
          maxArea = Math.max(maxArea, dfsIterative(r, c))
      }
  }

  return maxArea;
};