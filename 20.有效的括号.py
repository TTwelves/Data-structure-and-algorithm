#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start

class Solution:
    def isValid(self, s: str) -> bool:
        dict1={'(':')','[':']','{':'}','?':'?'}
        stack=['?']

        for i in s:
            if i in dict1:
                stack.append(dict1[i])
            else:
                if stack.pop()==i: 
                    pass
                else:
                    return False         
        return True if len(stack)==1 else False
# @lc code=end

