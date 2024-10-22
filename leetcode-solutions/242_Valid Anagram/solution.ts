function isAnagram(s: string, t: string): boolean {
  const charCount = {};

  if (s.length !== t.length) return false;

  for (let charInS of s) {
      const count = charCount[charInS];
      if (count === undefined) {
          charCount[charInS] = 1;
      } else {
          charCount[charInS] += 1;
      }
  }

  for (let charInT of t) {
      const count = charCount[charInT];
      if (count != undefined && count > 0) {
          charCount[charInT] -= 1;
      } else {
          return false;
      }
  }

  return true;
};
