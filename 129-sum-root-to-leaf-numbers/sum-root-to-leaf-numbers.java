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
    List<String> arr = new ArrayList<>();
    List<List<String>> final_list = new ArrayList<>();
    List<Integer> main = new ArrayList<>();
    public int sumNumbers(TreeNode root) {
        dfs(root,arr);
        for(int i = 0; i < final_list.size();i++)
        {
            String temp = String.join("",final_list.get(i));
            main.add(Integer.valueOf(temp));
        }
        return main.stream().reduce(0,(a,b) -> a + b);
    }
    public void dfs(TreeNode root,List<String> arr)
    {
        
        if (root == null)
        {
            return;
        }

        //add element
        arr.add(String.valueOf(root.val)); 
        //leaf node calculation
        if (root.left == null && root.right == null) final_list.add(new ArrayList(arr));
        else{
        dfs(root.left,arr);
        dfs(root.right,arr);
        }
        arr.remove(arr.size() - 1);

    }
}