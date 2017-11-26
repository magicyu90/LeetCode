class Solution:
    """
    598. Range Addition II

    Input:
    m = 3, n = 3
    operations = [[2,2],[3,3]]
    Output: 4
    Explanation:
    Initially, M =
    [[0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]]

    After performing [2,2], M =
    [[1, 1, 0],
    [1, 1, 0],
    [0, 0, 0]]

    After performing [3,3], M =
    [[2, 2, 1],
    [2, 2, 1],
    [1, 1, 1]]

    So the maximum integer in M is 2, and there are four of it in M. So return 4.
    """

    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # zeros = [0] * (m * n)
        # for step in ops:
        #     row = step[0]
        #     column = step[1]
        #     for i in range(row):
        #         for j in range(column):
        #             zeros[column * i + j] += 1
        # return zeros.count(max(zeros))
        # 思路：我提供的算法会造成内存溢出，正确的答案是最大值的数量为步数中行的最小值*步数中列的最小值，厉害！
        if not ops:
            return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)



# solution = Solution()
# print(solution.maxCount(m=3, n=3, ops)
