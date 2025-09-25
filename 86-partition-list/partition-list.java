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
class Solution {
    public ListNode partition(ListNode head, int x) {
        // Edge Cases
        if (head == null ) return head;



        List<ListNode> left =  new ArrayList<>();
        List<ListNode> right =  new ArrayList<>();
        ListNode current;
        current = head;
        while (current != null)
        {
            if (current.val < x) left.add(current);
            else right.add(current);
            current = current.next;
        }
        // Edge Cases both the left and right are empty then no partition needed..
        if (right.isEmpty() || left.isEmpty()) return head;

        for (int i=0; i < left.size(); i++)
        {
            if (i+1 < left.size()) left.get(i).next = left.get(i+1);
            else left.get(i).next = right.get(0); // attach the link here
        }
        for (int i=0; i < right.size(); i++)
        {
            if (i+1 < right.size()) right.get(i).next = right.get(i+1);
            else right.get(i).next = null; // attach the link here
        }
        return left.get(0);
    }
}