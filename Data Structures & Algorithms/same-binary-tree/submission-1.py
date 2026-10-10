# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool: 
  
        pQueue = deque([p])
        qQueue = deque([q])

        while pQueue and qQueue:

            for _ in range(len(pQueue)):

                pCurr = pQueue.popleft()
                qCurr = qQueue.popleft()

                if (pCurr is None and qCurr is None):
                    continue
                if (pCurr is None or qCurr is None or pCurr.val != qCurr.val):
                    return False
            

                pQueue.append(pCurr.left)
                pQueue.append(pCurr.right)
                qQueue.append(qCurr.left)
                qQueue.append(qCurr.right)

        return True

            



       
        
        