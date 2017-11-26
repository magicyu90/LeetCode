# coding: utf-8
class Solution:
    """
    # The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
    # Given two integers x and y, calculate the Hamming distance.
    # Note:
    # 0 ≤ x, y < 231.
    # 关键词：异或
    """
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # binaryX = '{0:032b}'.format(x)
        # binaryY = '{0:032b}'.format(y)
        # defCount = 0
        # for index, value in enumerate(binaryX):
        #     if value != binaryY[index]:
        #         defCount += 1

        # return defCount
        # 按位异或 然后算1的个数
        return bin(x ^ y).count('1')


solution = Solution()
print(solution.hammingDistance(1, 4))
