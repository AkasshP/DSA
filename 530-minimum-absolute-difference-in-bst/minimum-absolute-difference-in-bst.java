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
    ArrayList<Integer> list = new ArrayList<>();
    public void inorder(TreeNode root)
        {
            if (root == null) return;
            inorder(root.left);
            list.add(root.val);
            inorder(root.right);
        }
    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        int res = Integer.MAX_VALUE;;
        int i;
        for(i = 0; i < list.size(); i++)
        {
            if (i+1 < list.size()) res = Math.min(res,list.get(i+1) - list.get(i));
        }
        return res;
    }
    
}