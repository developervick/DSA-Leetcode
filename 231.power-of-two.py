#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if abs(math.log(n, 2) - round(math.log(n, 2))) < 1e-10:
            return True
        return False
# @lc code=end

