class Solution:
    """
    258. Add Digits

    Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
    For example:
    Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

    要求算法的时间复杂度是O(1) 也就是一个运算操作指令
    """

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = num % 9
        return 0 if num == 0 else res if res != 0 else 9


solution = Solution()
print(solution.addDigits(111))
