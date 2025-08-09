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
    public ListNode rotateRight(ListNode head, int k) {
        ListNode temp = null;
        int count = 0;

        //edage case
        if(head == null || head.next == null || k==0) return head;
        
        for (ListNode p = head; p != null; p = p.next) count++;

        k %= count;
        if (k == 0) return head;
        int total = count - k;
        // main edge case don't want to rotate again and again
        if (total == 0) return head;

        count = 0;
        ListNode prev = null, curr = head;
        while(curr != null)
        {
            if(total == count)
                {
                    temp = curr;
                    prev.next = null;
                    break;
                }
            prev = curr;
            curr = curr.next;
            count += 1;
        }
        ListNode Main_head = temp;
        while(temp.next != null) temp = temp.next;
        temp.next = head;

        return Main_head;  
    }
}