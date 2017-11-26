# coding:utf-8
class Solution:
    """
    Input:
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1, sc = 1, newColor = 2
    Output: [[2,2,2],[2,2,0],[2,0,1]]
    Explanation:
    From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
    by a path of the same color as the starting pixel are colored with the new color.
    Note the bottom corner is not colored 2, because it is not 4-directionally connected
    to the starting pixel.
    """
    startColor = 0

    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        # startColor = image[sr][sc]
        # rows, columns = len(image), len(image[0])

        # def paint(row,col):
        # print('startColor:', startColor)

        # if (0 <= sr < rows and 0 <= sc < columns) and image[sr][sc] == startColor:
        #     image[sr][sc] = newColor
        #     self.floodFill(image, sr - 1, sc, newColor)
        #     self.floodFill(image, sr, sc + 1, newColor)
        #     self.floodFill(image, sr, sc - 1, newColor)
        #     self.floodFill(image, sr + 1, sc, newColor)

        # return image

        rows, columns, startColor = len(image), len(image[0]), image[sr][sc]

        def paint(row, column):
            if (not (0 <= row < rows and 0 <= column < columns)) or image[row][column] != startColor:
                return
            print('startColor:', startColor)
            image[row][column] = newColor
            paint(row - 1, column)  # 上
            paint(row, column + 1)  # 右
            paint(row, column - 1)  # 下
            paint(row + 1, column)  # 左

        if startColor != newColor:
            paint(sr, sc)

        return image


solution = Solution()
print(solution.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
