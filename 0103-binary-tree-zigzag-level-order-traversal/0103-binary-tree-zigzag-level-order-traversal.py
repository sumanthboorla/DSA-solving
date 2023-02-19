from queue import Queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        re=[]
        q=deque([root])
        level=0
        if not root:
            return []
        while(q):
            le_node=[]
            length=len(q)
            for i in range(length):
                node=q.popleft()
                if(level%2==0):
                    le_node.append(node.val)
                else:
                    le_node.insert(0,node.val)
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
            re.append(le_node)
            level+=1
        return re
            
            
        