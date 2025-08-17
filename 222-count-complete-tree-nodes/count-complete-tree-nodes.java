/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int countNodes(TreeNode root) {
        TreeNode node;
        Deque<TreeNode> dq = new ArrayDeque<>();
        int node_count = 0;
        if (root != null) dq.offer(root);

        while (!dq.isEmpty())
        {
            for(int i = 0; i < dq.size();i++)
            {
                node = dq.pollFirst();
                if (node.left != null) dq.offer(node.left);
                if (node.right != null) dq.offer(node.right);
                node_count +=  1;
            }
        }
        return node_count;
        
    }
}