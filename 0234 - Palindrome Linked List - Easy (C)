/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool isPalindrome(struct ListNode* head) {
    if(head == NULL || head->next == NULL)
        return true;
    
    // couting number of nodes
    int count = 0; 
    struct ListNode *current = head;
    while(current != NULL){
        count++;
        current = current->next;
    }

    //storing the node values in an array;
    int values[count];
    current = head;
    for(int i = 0; i<count; i++){
        values[i] = current->val;
        current = current->next;
    }

    int left = 0;
    int right = count - 1;
    while(left < right){
        if(values[left] != values[right])
            return false;
        left++;
        right--;
    }
    return true;
}
