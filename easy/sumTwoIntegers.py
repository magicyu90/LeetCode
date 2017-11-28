# coding:utf-8


class Solution:
    """
    Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

    Example:
    Given a = 1 and b = 2, return 3.
    """

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        #
        # 首先，sum 存放每次循环中 a 与 b 的异或值，也就是直接相加值；
        # b 存放每次的进位值，然后 a 存储 sum （也就是直接相加值）进入下一次循环（当进位值非空）；
        # 当且仅当进位值为空时，用户的上一次循环中的 sum 已经是可以直接相加的异或结果了，此时得到结果，返回。
        #
        sum = a
        while b != 0:
            sum = a ^ b
            b = (a & b) << 1
            a = sum
        return sum


solution = Solution()
print(solution.getSum(5, 700))
