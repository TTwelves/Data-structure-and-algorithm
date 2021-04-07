#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
'''

语法
以下是 enumerate() 方法的语法:

enumerate(sequence, [start=0])
参数
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
返回值
返回 enumerate(枚举) 对象。

实例
以下展示了使用 enumerate() 方法的实例：

>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable=dict()
        for k,v in enumerate(nums):
            if target-v in hashtable:
                return [hashtable[target-v],k]
            hashtable[v]=k # k、v反转 就能通过访问原本的数值返回相应的序号


# @lc code=end
      
                
                    
