function search(nums: number[], target: number): number {
  const numLength = nums.length;
  let startIndex = 0;
  let endIndex = numLength - 1;

  while (startIndex <= endIndex) {
      const midIndex = Math.floor((endIndex + startIndex) / 2);
      const numAtIndex = nums[midIndex]
      if (numAtIndex < target) {
          startIndex = midIndex + 1;
      } else if (numAtIndex > target) {
          endIndex = midIndex - 1;
      }
      else {
          return midIndex;
      }
  }

  return -1;
};