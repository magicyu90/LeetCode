# coding:utf-8
class Solution:
    """
    463. Island Perimeter
    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]]

    Answer: 16
    """

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        premiter = 0
        rows = len(grid)
        columns = len(grid[0])

        # 我的思路：扩展成大一圈的正方形
        for i in range(rows):
            grid[i].insert(0, 0)
            grid[i].append(0)

        grid.insert(0, [0] * (columns + 2))
        grid.append([0] * (columns + 2))

        newRows = rows + 2
        newColums = columns + 2

        for i in range(1, newRows - 1):
            for j in range(1, newColums - 1):
                if grid[i][j]:
                    currentVaule = 4
                    if grid[i - 1][j]:
                        currentVaule -= 1
                    if grid[i + 1][j]:
                        currentVaule -= 1
                    if grid[i][j - 1]:
                        currentVaule -= 1
                    if grid[i][j + 1]:
                        currentVaule -= 1
                    premiter += currentVaule
        return premiter

        # 也可以换一个思路，查看当前1的方块的右方和下方是否是1，若是则减2
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]:
                    premiter += 4
                    if j + 1 < columns and grid[i][j + 1]:
                        premiter -= 2
                    if i + 1 < rows and grid[i + 1][j]:
                        premiter -= 2
        return premiter


solution = Solution()
print(solution.islandPerimeter([[1, 0]]))
