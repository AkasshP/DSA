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
        ListNode Dummy = head;
        ListNode Curr = head;
        ListNode temp = null;
        ListNode prev = null;
        ListNode Main_head = null;
        int count = 0;

        //edage case
        if (head == null || k == 0) return head; 
        while(Dummy != null)
        {
            Dummy = Dummy.next;
            count += 1;
        }
        //edge case
        if (count <= 1) return head;
        if (count > 1 && k != 0)
        {
            int total = count - k;
            while (total < 0)
            {
                total = count - Math.abs(total); // update the total with the number of nodes
            }
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
        return head;
    }
}