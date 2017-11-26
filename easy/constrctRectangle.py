# coding:utf-8
class Solution:
    """
    492. Construct the Rectangle
    Input: 4
    Output: [2, 2]
    Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
    But according to requirement 2, [1,4] is illegal; according to requirement 3,
    [4,1] is not optimal compared to [2,2]. So the length L is 2, and the width W is 2.

    """

    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        # import functools
        import math
        num = int(math.sqrt(area))
        if num ** 2 == area:
            return [num, num]
        for num in range(num, 0, -1):
            if area % num == 0:
                return [int(area / num), num]
        # 我的思路：找到所有的因子
        # factors = set(functools.reduce(list.__add__,
        #                                ([i, area // i] for i in range(1, int(area**0.5) + 1) if area % i == 0)))

        # factors = sorted(factors)
        # size = len(factors)

        # return [factors[int(size / 2)], int(area / factors[int(size / 2)])]
        # 得到平方根，从平方根到0进行遍历
        for num in range(int(math.sqrt(area)), 0, -1):
            if area % num == 0:
                return [int(area / num), num]


solution = Solution()
print(solution.constructRectangle(9999991))
