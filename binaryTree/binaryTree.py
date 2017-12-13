# coding:utf-8


class Node():
    """
    二叉树节点类
    """

    def __init__(self, value=None, lchild=None, rchild=None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

    def __str__(self):
        return str(self.value)


class BinaryTree():
    """
    二叉树类
    """

    def __init__(self):
        self.root = Node()
        self.queue = []

    def add(self, element):
        """
        二叉树新增节点
        """
        new_node = Node(element)
        self.queue.append(new_node)
        # 增加根节点
        if self.root.value is None:
            self.root = new_node
        else:
            tree_node = self.queue[0]
            if tree_node.lchild is None:
                tree_node.lchild = new_node
            else:
                tree_node.rchild = new_node
                # 将当前根节点推出
                self.queue.pop(0)

    def recursion_vlr(self, root: Node):
        """递归先序遍历-根左右"""
        if root is None:
            return
        print(root.value, end=' ')
        self.recursion_vlr(root.lchild)
        self.recursion_vlr(root.rchild)

    def recursion_lvr(self, root: Node):
        """递归中序遍历-左根右"""
        if root is None:
            return
        self.recursion_lvr(root.lchild)
        print(root.value, end=' ')
        self.recursion_lvr(root.rchild)

    def recursion_lrv(self, root: Node):
        """递归后序遍历-左右根"""
        if root is None:
            return
        self.recursion_lrv(root.lchild)
        self.recursion_lrv(root.rchild)
        print(root.value, end=' ')

    def level_scan(self):
        """按层进行扫描"""
        queue = []
        current = self.root
        queue.append(current)
        while queue:
            current = queue.pop(0)
            print(current.value, end=' ')
            if current.lchild is not None:
                queue.append(current.lchild)
            if current.rchild is not None:
                queue.append(current.rchild)

    def count_level_average(self):
        """计算每层平均值"""
        ans = []
        queue = []
        current = self.root
        queue.append(current)
        while queue:
            queue_size = len(queue)
            queue_sum = 0.0
            for i in range(queue_size):
                current = queue.pop(0)
                queue_sum += current.value
                if current.lchild is not None:
                    queue.append(current.lchild)
                if current.rchild is not None:
                    queue.append(current.rchild)
            ans.append(queue_sum / queue_size)
        print(ans)

    def stack_vlr(self):
        """利用栈实现先序遍历"""
        stack = []
        current = self.root
        total = 0
        while current or stack:
            while current:
                print(current.value, end=' ')
                stack.append(current)
                current = current.lchild
                if current is not None:
                    if current.lchild is None and current.rchild is None:
                        total += current.value
            current = stack.pop()
            current = current.rchild
        print('\ntotal:', total)

    def stack_lvr(self):
        """利用栈实现中序遍历"""
        stack = []
        current = self.root
        while current or stack:
            while current:
                stack.append(current)
                current = current.lchild

            current = stack.pop()
            print(current.value, end=' ')
            current = current.rchild

    def invert_tree(self, root: Node):
        """左右交换"""
        if root.lchild is not None and root.rchild is not None:
            temp = root.lchild.value
            root.lchild.value = root.rchild.value
            root.rchild.value = temp
        if root.lchild is not None:
            self.invert_tree(root.lchild)
        if root.rchild is not None:
            self.invert_tree(root.rchild)


if __name__ == '__main__':
    print('Here is main')
    tree = BinaryTree()
    for i in [3, 7]:
        tree.add(i)

    print('先序遍历结果:', end=' ')
    tree.recursion_vlr(tree.root)
    print('\n')

    print('中序遍历结果:', end=' ')
    tree.recursion_lvr(tree.root)
    print('\n')

    print('后序遍历结果:', end=' ')
    tree.recursion_lrv(tree.root)
    print('\n')

    print('按层遍历结果:', end=' ')
    tree.level_scan()
    print('\n')

    print('计算每层平均值:', end=' ')
    tree.count_level_average()
    print('\n')

    print('根据栈先序遍历结果:', end=' ')
    tree.stack_vlr()
    print('\n')

    print('根据栈中序遍历结果:', end=' ')
    tree.stack_lvr()
    print('\n')

    print('左右交换:', end=' ')
    tree.invert_tree(tree.root)
    tree.level_scan()
    print('\n')
