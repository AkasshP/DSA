/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
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
    TreeNode node;
    ListNode curr;
    public TreeNode sortedListToBST(ListNode head) {
        curr = head;// initalize the head
        List<Integer> arr = new ArrayList<>();
        while (curr != null)
        { 
            arr.add(curr.val);
            curr = curr.next;
        }
        return divide(arr,0,arr.size()-1);
    }
    public TreeNode divide(List<Integer> arr,int low,int high)
    {
        if (low > high) return null;
        int mid = low + (high - low) / 2;
        TreeNode root = new TreeNode(arr.get(mid));
        root.left = divide(arr,low,mid-1);
        root.right = divide(arr,mid+1,high);
        return root;
    }

}