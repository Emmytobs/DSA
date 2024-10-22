function threeSum(nums: number[]): number[][] {
  const output: number[][] = []

  /**
      Implementation 2
      [-4, -1, -1, 0, 1, 2]

      TIPS:
      Solve TwoSum and TwoSum II first.
      This method for ThreeSum uses the two-pointer technique
  */
  // This problem can be easily solved when the array is sorted
  nums.sort((a, b) => a - b)
  const TARGET = 0;

  for (let i = 0; i < nums.length; i++) {
      const a = nums[i];
      // If a is the same value as the one before it, then skip it to avoid having a duplicate triplet
      if (i > 0 && a == nums[i - 1]) {
          // console.log(i, "->", nums[i])
          continue;
      }

      let l = i + 1
      let r = nums.length - 1

      while (l < r) {
          const b = nums[l]
          const c = nums[r]
          const threeSum = a + b + c;
          if (threeSum > TARGET) r -= 1
          else if (threeSum < TARGET) l += 1
          else {
              // console.log(i, "->", l, r)
              output.push([a, b, c]);
              l += 1
              while (nums[l] == nums[l - 1] && l < r) {
                  l += 1
              }
          }
      }
  }

  // Implementation 1: This implementation below will work, but will include duplicate triplets
  // for (const target of nums) {
  //     const sums = []
  //     const map = {}
  //     for (const num of nums) {
  //         if (num != target) {
  //             const complement = map[num]
  //             if (complement === undefined) {
  //                 map[(-1 * target) - num] = num
  //                 continue;
  //             }
  //             sums.push([target, num, complement])
  //         }
  //     }
  //     output.push(...sums);
  // }

  return output;
};