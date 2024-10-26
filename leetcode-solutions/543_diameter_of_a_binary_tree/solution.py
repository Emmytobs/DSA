# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Method 1: Much slower compared to the recursive method
        def iterative_dfs():
            def height(node: TreeNode) -> int:
                if node == None: return 0
                return 1 + max(height(node.left), height(node.right))

            stack = [root]
            diameter = float("-inf")
            while stack:
                curr_node = stack.pop()
                left_subtree_height = height(curr_node.left)
                right_subtree_height = height(curr_node.right)
                if curr_node.left is not None:
                    stack.append(curr_node.left)
                if curr_node.right is not None:
                    stack.append(curr_node.right)
                diameter = max(diameter, (left_subtree_height + right_subtree_height))
            return diameter
        
        # Method 2: Much faster than the iterative method
        def recursive_dfs():
            diameter = float('-inf')
            def height(node: TreeNode) -> int:
                nonlocal diameter
                if node is None: return 0

                left_height = height(node.left)
                right_height = height(node.right)
                diameter = max(diameter, (left_height + right_height))

                return 1 + max(left_height, right_height)
            
            height(root)
            return diameter

        return iterative_dfs()