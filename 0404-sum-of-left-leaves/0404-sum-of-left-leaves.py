# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if(root==None):
            return 0
        if(root.left==None and root.right ==None):
            return 0
        sum1=0
        if(root.left!=None and root.left.left==None and root.left.right ==None):
            sum1+=root.left.val
            
        return sum1+self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
    
    
    
    
 
