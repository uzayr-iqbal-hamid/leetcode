/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* middleNode(struct ListNode* head) {
    struct ListNode *ptr1 = head;
    struct ListNode *ptr2 = head;
    int count = 0;
    while(ptr1->next != NULL){
        ptr1 = ptr1->next;
        count++;
    }
    count++;
    for(int i = 0; i<count/2; i++){
        ptr2 = ptr2->next;
    }
    return ptr2;
}
