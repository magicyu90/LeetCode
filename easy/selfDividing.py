class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        # resultArr = []
        # for number in range(left, right + 1):
        #     numberStr = str(number)
        #     isOK = True
        #     for char in numberStr:
        #         if char == '0':
        #             isOK = False
        #             break
        #         if number % int(char) != 0:
        #             isOK = False
        #             break
        #     if isOK == True:
        #         resultArr.append(number)
        # return resultArr

        result = filter(Solution.check, range(left, right + 1))
        print('result:', result)
        return result

    @staticmethod
    def check(num):
        digits = set(map(int, str(num)))
        if 0 in digits:
            return False
        return not any(num % d for d in digits)


solution = Solution()
solution.selfDividingNumbers(1, 300)
