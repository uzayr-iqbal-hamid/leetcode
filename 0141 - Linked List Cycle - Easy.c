/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    
    //if the head is NULL or if there exists only one node, then return false
    if(head==NULL || head->next==NULL)
        return false;
    
    //making two pointers to keep track of the nodes 
    struct ListNode *ptr1 = head;
    struct ListNode *ptr2 = head->next;

    //ptr1 moves by one node, ptr2 moves by two nodes at a time
    while(ptr1 != ptr2){
        //if ptr2 i.e. the pointer which moves forward 2 nodes at a time discovers a NULL, then return false
        if(ptr2 == NULL || ptr2->next == NULL)
            return false;

        ptr1 = ptr1->next;
        ptr2 = ptr2->next->next;
    }

    return true;
}
