# encoding :utf-8
"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

【思路】：遍历整数数组，将每个元素nums[i]与目标数target作差得到结果less，
     如果在数组剩余的数中找到差less 排除掉与自身相加等于target的情况
     将差值less所对应的下标与下标i输出成列表
【问题】：其中遇到两个问题
      一个是在pycharm上使用数组输入不行
      另一个是对于不能重复利用这点不是很理解
      最后的关键在于设置条件
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            less = target - nums[i]
            for j in range(len(nums)):
                if (less == nums[j]):
                    if (less == nums[i]) & (i == j):
                        continue
                    else:
                        return [i, j]


# list1 = [int(i) for i in input()]
list1 = input()
goal = input()
twonum1 = Solution()
twonum1.twoSum(list1, int(goal))


