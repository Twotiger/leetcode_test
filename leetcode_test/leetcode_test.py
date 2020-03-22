from typing import List
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @classmethod
    def create(cls, l: list):
        return TreeNodeFactory().create(l)

    def get_value(self):
        """从此节点生成list
        """
        queue = [self]
        data = [self.val]
        while 1:
            new_queue = []
            new_data = []
            for node in queue:
                if node:
                    new_queue.append(node.left)
                    new_queue.append(node.right)
                    new_data.append(node.left.val if node.left else None)
                    new_data.append(node.right.val if node.right else None)
                else:
                    new_queue.extend([None, None])
            if any(new_queue):
                queue = new_queue
                data.extend(new_data)
            else:
                break
        return data

    def __str__(self):
        return "<TreeNode: %s>" % self.val


class TreeNodeFactory:
    @classmethod
    def create(cls, l: list) -> TreeNode:
        """
        输入列表[3,9,20,None,None,15,7]
        返回一个二叉树
        """
        if not l:
            return None

        root = TreeNode(l[0])
        queue = [root]
        n = len(l)
        p = 1

        while queue:
            new_queue = []
            for tree_node in queue:
                if not tree_node:
                    continue
                if p < n:
                    if l[p] is not None:
                        left = TreeNode(l[p])
                        tree_node.left = left
                        new_queue.append(left)
                    else:
                        new_queue.append(None)
                    p += 1

                if p < n:
                    if l[p] is not None:
                        right = TreeNode(l[p])
                        tree_node.right = right
                        new_queue.append(right)
                    else:
                        new_queue.append(None)
                    p += 1
       
            queue = new_queue
        return root

    @staticmethod
    def is_odd(num):
        return num % 2


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.loop = False  # 是否有环

    @classmethod
    def create(cls, l: list):
        """创建一个链表
        ListNode.create([1,2,3,4]) # 1 -> 2 -> 3 -> 4
        """
        root = ListNode(0)
        node = root
        for i in l:
            tmp = ListNode(i)
            node.next = tmp
            node = tmp
        return root.next

    @classmethod
    def create_loop(cls, l: list, loop_start):
        """创建一个有环链表
        ListNode.create([1,2,3,4], 1) # 1 -> 2 -> 3 -> 4 -> 2 -> 3 -> 4 -> ....
        在索引1处循环
        """
        if loop_start >= len(l):
            raise ValueError("loop_start must less than length of list")
        root = ListNode(0)
        node = root
        loop_node = None
        for index, value in enumerate(l):
            tmp = ListNode(value)
            if index == loop_start:
                loop_node = tmp
            node.next = tmp
            node = tmp
        else:
            node.next = loop_node

        return root.next

    def get_value(self) -> List:
        data = []
        root = self
        while root:
            data.append(root.val)
            root = root.next
        return data

    def __str__(self):
        return "<ListNode: %s>" % self.val


def test_listnode():
    node = ListNode.create([1, 2, 3])
    assert node.get_value() == [1, 2, 3]


def test_treenode():
    tree = TreeNode.create([1, None, 2, 3])
    assert tree.val == 1
    assert tree.left == None
    assert tree.right.val == 2
    assert tree.right.left.val == 3


def test_treenode2():
    tree = TreeNode.create([5, 4, 7, 3, None, 2, None, -1, None, 9])
    assert tree.right.left.left.val == 9

def test_treenode3():
    # 创建不合法的tree node
    tree = TreeNode.create([3, None, 20, None, None, 15, 7])
    assert tree.get_value() == [3, None, 20]


if __name__ == "__main__":
    t = TreeNode.create([3, None, 20, None, None, 15, 7])
    print(t.get_value())
