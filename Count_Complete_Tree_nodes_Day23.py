Given a complete binary tree, count the number of nodes.

Note:

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Example:

Input: 
    1
   / \
  2   3
 / \  /
4  5 6

Output: 6

Python3 program:

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        def lheight(node):
            if not node: return 0
            return 1+lheight(node.left)
        
        def rheight(node):
            if not node: return 0
            return 1+rheight(node.right)
        
        l,r  = lheight(root), rheight(root)
        
        #is this balanced
        if l>r:
            return 1+self.countNodes(root.left) + self.countNodes(root.right)            
        else:    
            return (2**l) -1
        
Alternate method:
#         def pre(node):
#             if not node: return 0
#             return pre(node.left) + pre(node.right) +1
        
#         return pre(root)
