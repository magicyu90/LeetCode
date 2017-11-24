# coding :utf-8
class Solution:
    """
    You're now a baseball game point recorder.

    Given a list of strings, each string can be one of the 4 following types:

    Integer (one round's score): Directly represents the number of points you get in this round.
    "+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
    "D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
    "C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
    Each round's operation is permanent and could have an impact on the round before and the round after.

    You need to return the sum of the points you could get in all the rounds.
    """

    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = []
        for step in ops:
            if step == "C":
                ans.pop()
            elif step == "D":
                ans.append(ans[-1] * 2)
            elif step == "+":
                ans.append(ans[-1] + ans[-2])
            else:
                ans.append(int(step))
        return sum(ans)


solution = Solution()
solution.calPoints(["5", "2", "C", "D", "+"])
