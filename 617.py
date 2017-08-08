# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 == None:
            return None
        if t1 == None:
            return t2
        if t2 == None:
            return t1

        ret = t1
        stack1 = []
        stack1.append(t1)
        stack2 = []
        stack2.append(t2)

        while stack2:
            temp1 = stack1.pop()

            temp2 = stack2.pop()

            if temp2:
                temp1.val += temp2.val
            else:
                continue

            if temp2.left and temp1.left == None:
                temp1.left = TreeNode(0)

            if temp2.right and temp1.right == None:
                temp1.right = TreeNode(0)

            stack2.append(temp2.left)
            stack2.append(temp2.right)
            stack1.append(temp1.left)
            stack1.append(temp1.right)

        return ret
    
