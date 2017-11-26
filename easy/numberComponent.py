class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # numStr = '{0:032b}'.format(num)
        # oneCharIndex = numStr.index('1')
        # numStr = numStr[oneCharIndex:]

        # completeStr = ''
        # for char in numStr:
        #     if char == '0':
        #         completeStr += '1'
        #     else:
        #         completeStr += '0'

        # return int(completeStr, 2)

        i = 1
        # print(len(bin(num)[2:]))
        # for index in range(len(bin(num)[2:])):
        #     i = i << 1
        #     index += 1
        # return (i - 1) ^ num
        while i <= num:
            i = i << 1
        return (i - 1) ^ num
        # 重要结论：一个数跟它的全1按位异或得到它的相反数 跟0按位异或得到本身
        # return bin(5 ^ 3)


solution = Solution()
print(solution.findComplement(5))
