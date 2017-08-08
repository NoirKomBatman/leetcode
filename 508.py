# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




class Solution(object):

    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        sum_hash={}

        def add(node):
            if node == None:
                return 0

            sum = 0

            sum += add(node.left)
            sum += add(node.right)
            sum += node.val
            if sum in sum_hash:
                sum_hash[sum] += 1
            else:
                sum_hash[sum] = 1
            return sum

        if root == None:
            return [];
        add(root);

        for key, val in sum_hash.iteritems():
            print(str(key) + ' ' + str(val))

        # traversing hash table to find max and frequency
        max = float('-inf')
        for key, val in sum_hash.iteritems():
            if val > max:
                max = val
        ret = []
        for key, val in sum_hash.iteritems():
            # print(str(key) + ' ' + str(val))
            if val == max:
                ret.append(key)

        return ret

    
