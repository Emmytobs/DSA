function lengthOfLongestSubstring(s: string): number {
  /* 
      Method #1: Using a brute force approach - the approach your brain instictively takes.
  */

  // let longestSubString: Array<string> = [];
  // let substring: Array<string> = [];

  // if (s.length === 1) return 1;

  // for (let i = 0; i < s.length; i++) {
  //     const char = s[i];
  //     substring = [char];

  //     for (let j = i + 1; j < s.length; j++) {
  //         const compareChar = s[j];

  //         if (!substring.includes(compareChar)) {
  //             substring.push(compareChar);
  //             continue;
  //         }
  //         break;
  //     }
  //     if (substring.length > longestSubString.length) {
  //         longestSubString = substring.slice();
  //     }
  // }
  // return longestSubString.length;

  /* 
      Method #2: Using a sliding window approach; (better runtime);
  */

  // let longestSubstring = '';
  // let maxLength = 0;
  // let windowStartIdx = 0;

  // let i = 1;
  // while (i < s.length) {
  //     const char = s[i];
  //     longestSubstring = s.slice(windowStartIdx, i);

  //     if (longestSubstring.includes(char) && windowStartIdx !== i) {
  //         maxLength = Math.max(maxLength, longestSubstring.length);
  //         windowStartIdx++;
  //         continue;
  //     }
  //     maxLength = Math.max(maxLength, longestSubstring.length + 1);
  //     i++;
  // }

  // return s.length === 1 ? 1 : maxLength;

  // Method #3: Also uses sliding window, but tries to be cleaner than #2
  let start = 0;
  let end = 1;
  let length = 0;

  while (end < s.length) {
      const subStr = s.substring(start, end);

      const currChar = s[end];
      if (subStr.includes(currChar) && start != end) {
          length = Math.max(length, subStr.length);
          start++;
          continue;
      }
      length = Math.max(length, subStr.length + 1);
      end++;
  }

  return s.length == 1 ?  1 : length;
};