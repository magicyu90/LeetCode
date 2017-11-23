# coding:utf-8
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        movesDict = {"U": 1, "R": 1, "D": -1, "L": -1}
        movesCount = 0
        for move in moves:
            movesCount += movesDict[move]
        return movesCount == 0


solution = Solution()
print(solution.judgeCircle("UDLR"))
