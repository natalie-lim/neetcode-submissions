# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, preorder, inorder, lp, rp, li, ri, preorder_dict, inorder_dict):
        if rp - lp == 0:
            return None
        curr_val = preorder[lp]
        if (rp - lp) <= 1:
            return TreeNode (curr_val, None, None)

        inorder_idx = inorder_dict[curr_val]
        # left preorder
        lpl = lp + 1
        lpr = lpl + (inorder_idx - li)
        # right preorder
        rpl = lpr
        rpr = rp
        # left inorder
        lil = li
        lir = inorder_idx
        # right inorder
        ril = inorder_idx + 1
        rir = ri

        left_node = self.helper(preorder, inorder, lpl, lpr, lil, lir, preorder_dict, inorder_dict)
        right_node = self.helper(preorder, inorder, rpl, rpr, ril, rir, preorder_dict, inorder_dict)

        return TreeNode(curr_val, left_node, right_node)



    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_dict = {}
        inorder_dict = {}

        for i, val in enumerate(preorder):
            preorder_dict[val] = i
        for i, val in enumerate(inorder):
            inorder_dict[val] = i

        return self.helper(preorder, inorder, 0, len(preorder), 0, len(inorder), preorder_dict, inorder_dict)