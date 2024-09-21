// LC link: https://leetcode.com/problems/invert-binary-tree/description/

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function invertTree(root: TreeNode | null): TreeNode | null {
  const invertedTree = new TreeNode();

  if (root === null) return null;
  
  const queue = [root];
  while (queue.length) {
      const currNode = queue.shift() as TreeNode;
      const temp = currNode.left;
      currNode.left = currNode.right;
      currNode.right = temp;

      if (currNode.left) { queue.push(currNode.left) }
      if (currNode.right) { queue.push(currNode.right) }
  }

  return root;
  
  // Method 2: Using recursive BFS
  // if (root === null) {
  //     return null;
  // }
  
  // const temp = root.left;
  // root.left = root.right;
  // root.right = temp;
  
  // invertTree(root.left);
  // invertTree(root.right);
  
  // return root; 
};