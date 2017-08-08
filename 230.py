# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        stack = []
        visited = []
        current = root
        done = 0
        while not done: # in order loop traversal
            if current:
                stack.append(current)
                current = current.left
            else:
                if stack:
                    current = stack.pop()
                    visited.append(current.val)
                    current = current.right
                else:
                    done = 1

        for i in range(len(visited)):
            if (i+1) == k:
                return visited[i]
