/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {

    if(list1 == NULL)
        return list2;
    if(list2 == NULL)
        return list1;

    struct ListNode ans;
    ans.next = NULL;
    struct ListNode *tail = &ans;

    while(list1 != NULL && list2 != NULL){
        if(list1->val < list2->val){
            tail->next = list1;
            list1 = list1->next;
        } else {
            tail->next = list2;
            list2 = list2->next;
        }
        tail = tail->next;
    }

    if(list1 != NULL)
        tail->next = list1;
    else
        tail->next = list2;

    return ans.next;
}
