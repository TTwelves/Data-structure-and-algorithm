#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total=0
        for i in range(len(s)-1):
            # 逻辑为：罗马数字里小数字在大数字旁边就当作负数即可
            # 例如：
            # VI=6----> 5+1
            # IV=4----> -1+5     
            if dict1[s[i]]>=dict1[s[i+1]]:
                total+=dict1[s[i]]
            else:
                total -= dict1[s[i]]
        # 为防止数组越界，最后一位放在循环外
        total+=dict1[s[-1]]
        return total
        
# @lc code=end

