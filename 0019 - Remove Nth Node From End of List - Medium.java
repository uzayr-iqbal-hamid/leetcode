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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        ListNode curr = head;

        int count = 0;
        while (curr != null) {
            count++;
            curr = curr.next;
        }
        
        int k = count - n;

        ListNode kth = dummy;
        for (int i = 0; i < k; i++) {
            kth = kth.next;
        }
        kth.next = kth.next.next;
        return dummy.next;
    }
}
