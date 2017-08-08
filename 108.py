# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        from math import ceil
        n = len(nums)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(nums[0])
        def createBST(root,nums,left,right):
            if right - left == 0:
                return None

            mid = left + (right - left) / 2
            if root == None:
                root = TreeNode(nums[mid])
            root.left = createBST(root.left,nums,left,mid)
            root.right = createBST(root.right,nums,mid + 1,right)
            return root



        return createBST(None,nums,0,n)
