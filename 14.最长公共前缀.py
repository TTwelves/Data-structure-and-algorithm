#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # max和min函数不能用于空的字符串，所以首先判断是否为空
        # if not: 等价于 if strs is NONE:
        if not strs:return ""
        # 选出一个最小的字符串和一个最大的字符串，相互比较
        # 此处的最大和最小字母是按照字母排序得来的,并不是字符串长度
        min_str=min(strs)
        max_str=max(strs)
        for x in range(len(min_str)):
            if min_str[x]!=max_str[x]:
                return min_str[:x]
        return min_str
# @lc code=end

