# coding :utf-8
class Solution:
    """
    Input:
    [4,3,2,7,8,2,3,1]
    Output:
    [5,6]
    """

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 我的思路：使用set进行去重筛选，然后进行set相减
        return list(set(range(1, len(nums) + 1)) - set(nums))


solution = Solution()
print(solution.findDisappearedNumbers([1, 2]))
