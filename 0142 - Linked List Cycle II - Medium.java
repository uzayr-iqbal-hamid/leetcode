/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
    
            if (fast == slow) {
                ListNode test = head;
                while (test != slow) {
                    test = test.next;
                    slow = slow.next;
                }
                return slow;
            }
        }
        return null;
    }
}
