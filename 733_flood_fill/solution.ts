function floodFill(image: number[][], sr: number, sc: number, color: number): number[][] {
  // From the starting pixel, get the four adjacent pixels.
      // For each of the four adjacent pixels of the starting pixel, get the four adjacent pixels
          // And so on...

  const ROWS = image.length;
  const COLS = image[0].length;
  const startingPixel = image[sr][sc];
  
  const visitedPixels: number[][] = []

  function pixelHasBeenVisited(sr: number, sc: number) {
      return visitedPixels.some(([_sr, _sc]) => _sr == sr && _sc == sc)
  }

  function dfsIterative(sr, sc) {
      const stack = [[sr, sc]]
      
      while (stack.length) {
          const [sr, sc] = stack.pop();
          if (
              sr < 0 || sr == ROWS ||
              sc < 0 || sc == COLS ||
              image[sr][sc] != startingPixel || 
              pixelHasBeenVisited(sr, sc)
          ) continue;

          const top = [sr - 1, sc]
          const bottom = [sr + 1, sc]
          const left = [sr, sc - 1]
          const right = [sr, sc + 1]

          image[sr][sc] = color;
          stack.push(top, bottom, left, right)
          visitedPixels.push([sr, sc])
      }
  }
  dfsIterative(sr, sc);

  return image;
};