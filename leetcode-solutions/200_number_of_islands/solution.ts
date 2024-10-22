function numIslands(grid: string[][]): number {
  let output = 0;
  const ROWS = grid.length;
  const COLS = grid[0].length;

  const visited: string[] = [];
  const cellHasBeenVisited = (r, c) => visited.includes(`${r},${c}`)

  function dfs(r, c) {
      const stack = [[r, c]];
      while(stack.length) {
          const [r, c] = stack.pop(); // Would work with a queue (via BFS)
          if (
              r < 0 || r == ROWS ||
              c < 0 || c == COLS ||
              grid[r][c] == "0" ||
              cellHasBeenVisited(r, c)
          ) continue
          stack.push(
              [r + 1, c],
              [r - 1, c],
              [r, c + 1],
              [r, c - 1]
          )
          visited.push(`${r},${c}`)
      }
  }

  for (let r = 0; r < grid.length; r++) {
      for (let c = 0; c < grid[r].length; c++) {
          if (grid[r][c] == "1" && !cellHasBeenVisited(r, c)) {
              dfs(r, c)
              output += 1
          }
      }
  }

  return output;
};