class Solution:
    """
    Input: [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
    """

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 我的思路：便利数组，遇到1进行累加，否则记录当前size并归0，返回size最大值
        maxSizeArr = []
        size = 0
        length = len(nums)
        index = 0
        for num in nums:
            index += 1
            if num != 0:
                size += 1
                if(index == length):
                    maxSizeArr.append(size)
            else:
                maxSizeArr.append(size)
                size = 0

        return max(maxSizeArr)


solution = Solution()
print(solution.findMaxConsecutiveOnes([1, 0, 0, 0, 1, 1, 1, 1]))
