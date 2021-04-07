#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 字符串解法
        # if x<0:
        #     return False
        # return True if x == int(str(x)[::-1]) else False
        
        if x<0 or (x%10==0 and x!=0):
            return False
        reversenum=0
        while x>reversenum:
            reversenum=reversenum*10+x%10
            x=x//10
        return True if reversenum==x or reversenum//10 == x else False
    
# @lc code=end

