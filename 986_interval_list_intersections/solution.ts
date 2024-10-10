function intervalIntersection(firstList: number[][], secondList: number[][]): number[][] {
  if (firstList.length == 0 || secondList.length == 0) return []

  const output: number[][] = []

  // (Better) Method #2: Using two pointers. Runs in O(n) time
  let firstPointer = 0
  let secondPointer = 0

  while (firstPointer < firstList.length && secondPointer < secondList.length) {
      const firstInterval = firstList[firstPointer]
      const secondInterval = secondList[secondPointer]

      /*
          Two intervals [a, b] and [c, d] intersect if:
          a <= d and c >= b (as long as the intervals are sorted; that is, a < b and c < d)
      */

      if (
          firstInterval[0] <= secondInterval[1] &&
          firstInterval[1] >= secondInterval[0]
      ) {
          const lowerBound = Math.max(firstInterval[0], secondInterval[0])
          const upperBound = Math.min(firstInterval[1], secondInterval[1])
          output.push([lowerBound, upperBound]);
      }
      
      if (firstInterval[1] > secondInterval[1]) {
          secondPointer += 1
      } else if (secondInterval[1] > firstInterval[1]) {
          firstPointer += 1
      } else  {
          secondPointer += 1
          firstPointer += 1
      }
  }

  // Method #1: Using a nested loop. (Less efficient; runs in O(n^2) time)
  // for (const intervalA of firstList) {
  //     const [startA, endA] = intervalA;
      
  //     for (const intervalB of secondList) {
  //         const [startB, endB] = intervalB;
  //         let lowerBound
  //         let upperBound
  //         if (startA <= endB && endA >= startB) {
  //             lowerBound = Math.max(startA, startB)
  //             upperBound = Math.min(endA, endB)
  //         } 
  //         else {
  //             continue;
  //         }
  //         output.push([lowerBound, upperBound])
  //     }
  // }

  return output
};