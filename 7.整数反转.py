#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:

        # 转换为字符串后，去除左端的正负号
        result=int(str(x).lstrip("-")[::-1])

        # 整型x的值并未变化
        if x<0: 
            return -result if -2**31 <= -result else 0 
        return result if result <= 2**31-1 else 0

# @lc code=end

