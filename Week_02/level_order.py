class Solution:
    def __init__(self):
        self.ans = []

    def helper(self, root, rank):
        if root:
            if len(self.ans) - 1 >= rank:
                self.ans[rank].append(root.val)
            else:
                self.ans.append([root.val])

            for i in root.children:
                self.helper(i, rank + 1)

    def levelOrder(self, root: 'Node') -> List[List[int]]:
        self.helper(root, 0)
        return self.ans