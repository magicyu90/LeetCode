
class Solution:
    """
    566. Reshape the Matrix
    
    Input:
        nums =
        [[1,2],
        [3,4]]
        r = 1, c = 4
        Output:
        [[1,2,3,4]]
        Explanation:
        The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
    """

    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        temp = []
        item = []
        ans = []
        if len(nums) * len(nums[0]) != r * c:
            return nums
        else:
            for num in nums:
                temp.extend(num)
            for i in range(r):
                item.extend(temp[i * c:i * c + c])
                ans.append(item)
                item = []
            return ans


solution = Solution()
print(solution.matrixReshape([[1, 2],
                              [3, 4]], 1, 4))
