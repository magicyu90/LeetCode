# coding:utf-8
class Solution:
    """
    136. Single Number
    Given an array of integers, every element appears twice except for one. Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


    """

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import functools
        # nums.sort()
        # length = len(nums)
        # if length < 2:
        #     return nums[0]
        # for i in range(0, length, 2):
        #     if i == length - 1:
        #         return nums[i]
        #     else:
        #         if nums[i] != nums[i + 1]:
        #             return nums[i]
        # 换个思路：按位进行异或操作
        # res = 0
        # for num in nums:
        #     res ^= num
        # return res
        return functools.reduce(lambda x, y: x ^ y, nums)


solution = Solution()
print(solution.singleNumber([2, 2, 3, 3, 5, 5, 7, 1, 1]))
