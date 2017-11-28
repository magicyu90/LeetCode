# coding :utf-8
class Solution:
    """
    575. Distribute Candies

    Given an integer array with even length, where different numbers in this array represent different kinds of candies.
    Each number means one candy of the corresponding kind.
    You need to distribute these candies equally in number to brother and sister.
    Return the maximum number of kinds of candies the sister could gain.
    """

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        # 取长度一半和不同种类数量较小值
        return min(int(len(candies) / 2), len(set(candies)))


solution = Solution()
print(solution.distributeCandies([1, 1, 2, 2, 3, 3]))
