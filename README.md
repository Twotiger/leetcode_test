# leetcode test

仅用适用于python

方便本地测试,ListNode和TreeNode类型


```
# filename leetcode.py
from leetcode_test import TreeNode

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def symmetric(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (
                left.val == right.val
                and symmetric(left.left, right.right)
                and symmetric(left.right, right.left)
            )
        if not root:
            return True
        return symmetric(root.left, root.right)

def test():
    tree = TreeNode.create([1,2,3,4,5])
    assert Solution().isSymmetric(tree)

```


使用pytest测试

```
pytest leetcode.py
```

如何安装

```
pip install git+https://github.com/Twotiger/leetcode_test.git
```

# 0.0.5

为ListNode, TreeNode添加`__str__`方法