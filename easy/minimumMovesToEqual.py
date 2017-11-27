class Solution:
    """
    453. Minimum Moves to Equal Array Elements
    Input:
    [1,2,3]

    Output:
    3

    Explanation:
    Only three moves are needed (remember each move increments two elements):

    [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
    """

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # total = sum(nums)
        # big = max(set(nums))
        # small = min(set(nums))
        # if small == big:
        #     return 0

        # return total - len(nums) * small
        return sum(nums) - len(nums) * min(nums)

solution = Solution()
print(solution.minMoves([1, 1, 1]))
