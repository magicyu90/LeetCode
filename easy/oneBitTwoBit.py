class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """

        # 借鉴答案思路：如果有1出现那么肯定是2位长度，所以如果得到index==长度-1，肯定最后一位是0
        size = len(bits)
        index = 0

        if size == 1:
            return True

        while index < size:
            if index == size - 1:
                return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False


solution = Solution()
print(solution.isOneBitCharacter([0, 1, 0]))
