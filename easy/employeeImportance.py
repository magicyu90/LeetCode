# coding:utf-8


class Solution:
    """
    690. Employee Importance

    Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
    Output: 11
    Explanation:
    Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3.
    They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
    """

    importance = 0

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        leader = next(employee for employee in employees if employee[0] == id)
        Solution.importance += leader[1]
        for sid in leader[2]:
            self.getImportance(employees, sid)

        return Solution.importance


solution = Solution()
print(solution.getImportance(
    [[1, 5, [2, 3]], [2, 3, [5, 6]], [3, 3, []], [5, 9, []], [6, 8, []]], 2))
