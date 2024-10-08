function maxSubArray(nums: number[]): number {
  /* 
     Best approach using Kadane's Algorithm: https://www.enjoyalgorithms.com/blog/maximum-subarray-sum
  */
  // let bestSum = nums[0];
  // let currSum = nums[0];

  // for (let i = 1; i < nums.length; i++) {
  //     const num = nums[i];
  //     currSum = Math.max((currSum + num), num);
  //     bestSum = Math.max(bestSum, currSum);
  // }

  // return bestSum;

  /*
      Another approach using Dynanmic Programming
      
      We can solve the max subarray sum of smaller subarrays till we solve the 
      max subarray sum of the entire array.

      See explanation for this solution under the DP section in the article above.
  */
  
  // Each index stores the max sum of the subarray at that index
  const maxSumOfSubArrayEndingAtIndex = [nums[0]]; 
  let maxSubArraySum = nums[0];

  for (let i = 1; i < nums.length; i++) {
      if (maxSumOfSubArrayEndingAtIndex[i - 1] < 0) {
          maxSumOfSubArrayEndingAtIndex[i] = nums[i]
      } else {
          maxSumOfSubArrayEndingAtIndex[i] = maxSumOfSubArrayEndingAtIndex[i - 1] + nums[i]
      }  
      maxSubArraySum = Math.max(maxSubArraySum, maxSumOfSubArrayEndingAtIndex[i])
  }
  return maxSubArraySum;
};