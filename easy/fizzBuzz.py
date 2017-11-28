# coding:utf-8
class Solution:
    """
    412. Fizz Buzz

    Write a program that outputs the string representation of numbers from 1 to n.
    But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
    For numbers which are multiples of both three and five output “FizzBuzz”.
    """

    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        numbers = list(range(1, n + 1))
        # numbers = ["Fizz" if number % 3 == 0 else number for number in numbers]
        ans = []
        for number in numbers:
            if number % 15 == 0:
                ans.append("FizzBuzz")
            elif number % 5 == 0:
                ans.append("Buzz")
            elif number % 3 == 0:
                ans.append("Fizz")
            else:
                ans.append(str(number))
        return ans
        # 好方法
        # fblist = [str(i+1) for i in range(n)]
        # fblist[2::3] = ["Fizz"] * (n//3)
        # fblist[4::5] = ["Buzz"] * (n//5)
        # fblist[14::15] = ["FizzBuzz"] * (n//15)
        # return fblist


solution = Solution()
print(solution.fizzBuzz(15))
