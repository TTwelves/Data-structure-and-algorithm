#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        slow,fast=0,0
        while fast< len(nums):
            if nums[slow]==nums[fast]:
                fast+=1
            else:
                slow+=1
                nums[slow] = nums[fast]
        return slow + 1
# @lc code=end

