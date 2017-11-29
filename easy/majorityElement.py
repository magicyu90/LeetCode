# coding:utf-8
class Solution:
    """
    169. Majority Element

    Given an array of size n, find the majority element.
    The majority element is the element that appears more than ⌊ n/2 ⌋ times.
    You may assume that the array is non-empty and the majority element always exist in the array.
    """

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # size = len(nums)
        # for num in nums:
        #     if nums.count(num) > int(size / 2):
        #         return num
        # 我的思路：使用collections，得到数量最大值的key
        # import collections
        size = len(nums)
        # count = collections.Counter(nums)
        # for key, value in count.items()
        #     if value > int(size / 2):
        #         return key
        # 改进版 一行代码
        # return max(count, key=count.get)
        nums.sort()
        return nums[size // 2]


solution = Solution()
print(solution.majorityElement([1, 1, 1, 3, 2, 3, 1]))
