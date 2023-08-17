# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return []
        # dfs function to find path from root to leaf
        def dfs(root,path):
            # to check if node is leaf
            if not root.left and not root.right:
                # if leaf then check if path sum matches target sum
                if targetSum==sum(path+[root.val]):
                    # if yes then add path to result array
                    return res.append(path+[root.val])
            # recursively cal for left and right nodes till leaf node
            if root.left:
                dfs(root.left,path+[root.val])
            if root.right:
                dfs(root.right,path+[root.val])
        # create a result array
        res=[]
        # call the function for root
        dfs(root,[])
        if res:
            return True
        return False
        