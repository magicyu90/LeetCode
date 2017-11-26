# coding=utf-8
class Solution:
    """
    A self-dividing number is a number that is divisible by every digit it contains.
    For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
    Also, a self-dividing number is not allowed to contain the digit zero.
    Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.
    """

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # def is_self_dividing(num):
        #     return '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
        # return filter(is_self_dividing, range(left, right + 1))

        def check(num):
            return '0' not in str(num) and all([num % int(digit) == 0 for digit in str(num)])
        return filter(check, range(left, right + 1))

solution = Solution()
print(solution.selfDividingNumbers(1, 22))
