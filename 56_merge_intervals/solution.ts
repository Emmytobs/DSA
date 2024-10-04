function merge(intervals: number[][]): number[][] {
  const mergedIndices: number[] = []

  // Sort the lower bounds of the intervals
  intervals.sort((intervalA, intervalB) => {
      const [startA] = intervalA;
      const [startB] = intervalB;
      return startA - startB
  })
  const output: number[][] = [intervals[0]]

  intervals.forEach(([start, end]) => {
      const [, lastIntervalEnd] = output[output.length - 1]
      if (start <= lastIntervalEnd) {
          output[output.length - 1][1] = Math.max(end, lastIntervalEnd)
      } else {
          output.push([start, end])
      }
  })

  // My initial implementation (without sorting the intervals) didn't pass all test cases
  // for (let i = 0; i < intervals.length; i++) {
  //     if (mergedIndices.includes(i)) continue;
  //     const merged = [intervals[i][0], intervals[i][1]];
  //     for (let j = i + 1; j < intervals.length; j++) {
  //         const [startI, endI] = merged;
  //         const [startJ, endJ] = intervals[j];
  //         if (
  //             startJ >= startI && startJ <= endI ||
  //             endJ <= endI && endJ >= startI ||
  //             startI >= startJ && startI <= endJ ||
  //             endI <= endJ && endI >= startJ
  //         ) {
  //             merged[0] = Math.min(startI, startJ)
  //             merged[1] = Math.max(endI, endJ)
  //             mergedIndices.push(j)
  //             console.log(merged)
  //         }
  //     }
  //     output.push(merged)
  // }
  
  return output;
};