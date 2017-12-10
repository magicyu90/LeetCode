# coding:utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    """
    Input:
      3
     /  \
    9   20
        /  \
       15   7
    Output: [3, 14.5, 11]
    Explanation:
    The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

    """
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        queue = []
        current = root
        queue.append(current)
        while queue:
            queue_size = len(queue)
            queue_sum = 0.0
            for i in range(queue_size):
                current = queue.pop(0)
                queue_sum += current.val
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            ans.append(queue_sum / queue_size)
        return ans