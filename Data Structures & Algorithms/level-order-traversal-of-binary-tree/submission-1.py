# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root_list, full_list):
        if all(node is None for node in root_list):
            return full_list

        val_list = []
        new_list = []
        for r in root_list:
            if r is not None:
                val_list.append(r.val)
                new_list.append(r.left)
                new_list.append(r.right)
        
        full_list.append(val_list)
        return self.helper(new_list, full_list)



    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.helper([root], [])