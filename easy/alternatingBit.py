# coding:utf-8
class Solution:
    """
    693. Binary Number with Alternating Bits
    Input: 5
    Output: True
    Explanation:
    The binary representation of 5 is: 101
    """

    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numStr = bin(n)[2:]
        # 我的思路：奇数位是1 偶数位0
        return not('0' in numStr[::2] or '1' in numStr[1::2])
        # 向右移一位，然后进行按位与(&)操作 ，判断是否为0
        # return (a & (a >> 1)) == 0;


solution = Solution()
print(solution.hasAlternatingBits(10))
