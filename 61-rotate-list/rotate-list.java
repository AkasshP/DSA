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
        ListNode Curr = head;
        ListNode temp = null;
        ListNode prev = null;
        ListNode Main_head = null;
        int count = 0;

        //edage case
        if(head == null || head.next == null || k==0) return head;
        
        for (ListNode p = head; p != null; p = p.next) count++;

        int total = count - k;
        while (total < 0) total = count - Math.abs(total);
        // main edge case don't want to rotate again and again
        if (total == 0) return head;

        count = 0;
        while(Curr != null)
        {
            if(total == count)
                {
                    temp = Curr;
                    prev.next = null;
                    break;
                }
            prev = Curr;
            Curr = Curr.next;
            count += 1;
        }
        Main_head = temp;
        while(temp.next != null)
        {
            temp = temp.next;
        }
        temp.next = head;
        return Main_head;  
    }
}