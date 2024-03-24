/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode *findMiddle(struct ListNode *head) {
    struct ListNode *fast = head, *slow = head;
    while(fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }
    return slow;
}
struct ListNode *reverseList(struct ListNode *head) {
    struct ListNode *prev = NULL, *curr = head, *next = NULL;
    while(curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}
void reorderList(struct ListNode* head) {
    if(!head || !head->next)
        return;
    
    struct ListNode *middle = findMiddle(head);
    struct ListNode *secondHalf = reverseList(middle->next);
    middle->next = NULL;

    struct ListNode *first = head, *second = secondHalf, *temp;
    while(second) {
        temp = first->next;
        first->next = second;
        second = second->next;
        first->next->next = temp;
        first = temp;
    }
}
