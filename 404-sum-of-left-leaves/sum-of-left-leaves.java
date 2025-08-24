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
    public int sumOfLeftLeaves(TreeNode root) {
        Deque<TreeNode> dq = new ArrayDeque<>();
        ArrayList<Integer> arr = new ArrayList<>();
        TreeNode node;
        if(root != null)
        {
            dq.offer(root);
        }
        while (!dq.isEmpty())
        {
            for (int i=0; i < dq.size(); i++)
            {
                node = dq.pollFirst();

                if (node.left != null)
                {
                    dq.offer(node.left);
                    if(node.left.left == null && node.left.right == null)
                    {
                        arr.add(node.left.val);
                    }

                }
                if (node.right != null)
                {
                    dq.offer(node.right);
                }
            }
        }
        System.out.println(arr);

    int sum = arr
    .stream()
    .mapToInt(Integer::intValue)
    .sum();
    return sum;
    }
}