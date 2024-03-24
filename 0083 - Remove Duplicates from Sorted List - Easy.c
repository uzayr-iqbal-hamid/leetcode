/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *cur = head;
    while(cur!=NULL && cur->next!=NULL){
        if(cur->val == cur->next->val){
            // struct ListNode *temp = cur->next;
            cur->next = cur->next->next;
            // free(temp);
        }
        else{
            cur = cur->next;
        }
    }

    return head;
}
