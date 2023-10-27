# 리트코드 617. 두 이진 트리 병합
# https://leetcode.com/problems/merge-two-binary-trees

# 디버깅 관련 수정 중

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    result: int = 0
    def __init__(self):
        self.longest = 0
        self.root = None

    def __str__(self):
        if self.root:
            return f"Solution (root={self.root.val})"
        else:
            return "Solution (no root)"

    def make_by_tree(self, lst, index):
        parent = None

        if len(lst) > index:
            value = lst[index]

            if value is None:
                return

            parent = TreeNode(value)
            parent.left = self.make_by_tree(lst, 2 * index + 1)
            parent.right = self.make_by_tree(lst, 2 * index + 2)

        if index == 0:
            self.root = parent

        return parent
    




    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and root2:
            node = TreeNode(root1.val + root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            
            return node
        else:
            return root1 or root2
        



lst = [1,2,3,None,None,4,5]
lst2 = [1,2,3,None,None,4,5]
# lst = []

s1 = Solution()
s1.make_by_tree(lst, 0)
print(s1)
result = s1.mergeTrees(s1.root)
print(result)