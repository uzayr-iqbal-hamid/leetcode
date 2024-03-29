/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode *ptr1 = malloc(sizeof(struct ListNode));
    ptr1->next = head;

    struct ListNode *f = ptr1;
    struct ListNode *s = ptr1;

    for(int i = 0; i<n+1; i++){
        f = f->next;
    }

    while(f!=NULL){
        f = f->next;
        s = s->next;
    }
    s->next = s->next->next;

    return ptr1->next;
}
