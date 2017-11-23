# coding :utf-8
# Input: [1,4,3,2]

# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return sum(sorted(nums)[::2])
        nums.sort()
        output = 0
        for i in nums[::2]:
            output += i
        return output


solution = Solution()
solution.arrayPairSum([1, 4, 3, 2])
