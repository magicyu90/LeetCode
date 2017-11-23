class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        numStr = '{0:032b}'.format(num)
        oneCharIndex = numStr.index('1')
        numStr = numStr[oneCharIndex:]

        completeStr = ''
        for char in numStr:
            if char == '0':
                completeStr += '1'
            else:
                completeStr += '0'

        return int(completeStr, 2)
