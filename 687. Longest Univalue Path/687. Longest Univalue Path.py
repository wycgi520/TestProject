#方法一、递归, 左子树的路径长度和右子树的路径长度叠加
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.ans = 0

        def arrow_length(node):
            # 到None返回
            if not node: return 0
            # 左边的长度
            left_length = arrow_length(node.left)
            # 右边的长度
            right_length = arrow_length(node.right)
            # 左边和右边的长度
            left_arrow = right_arrow = 0
            # 如果左边子节点和本节点的值相等, 长度可以在此基础上+1
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            # 同上
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            # 左边长度和右边长度相加,得到本节点的路径长度, 并对比长度更新ans
            self.ans = max(self.ans, left_arrow + right_arrow)
            # 因为是路径, 所以在父节点看来, 只能取左边或右边的最长路径作为下一次计算的值, 而不能两个都取
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans