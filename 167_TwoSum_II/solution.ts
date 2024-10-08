function twoSum(numbers: number[], target: number): number[] {
  let l = 0;
  let r = numbers.length - 1;

  /* 
  The Two Sum problem is easier to solve when the array is sorted.
  
  Since the 'numbers' param is a sorted array, we can use two pointers
  (at the beginning and end of the sorted array) to "walk" along the array until
  we find two values that equal the target.
  */

  while (l < r) {
      const twoSum = numbers[l] + numbers[r];
      if (twoSum > target) r -= 1
      else if (twoSum < target) l += 1
      else {
          return [l+1, r+1]
      }
  }
};