/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2){
    struct ListNode *temp = list1;
    for(int i = 0; i < a - 1; i++)
        temp = temp->next;
    //pointing at ath node
    struct ListNode *ath = temp;

    for(int i = 0; i < b - a + 2; i++)
        temp = temp->next;
    //pointing at bth node
    struct ListNode *bth = temp;

    ath->next = list2;

    while(list2->next)
        list2 = list2->next;

    list2->next = bth;

    return list1;

}
