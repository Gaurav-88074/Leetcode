/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* head1,struct ListNode* head2) {
        if (head1==NULL){
        return head2;
    }
    else if (head2==NULL){
        return head1;
    }
    else if(head1->val<head2->val){
        head1->next = mergeTwoLists(head1->next,head2);
    }
    else{
        head2->next = mergeTwoLists(head2->next,head1);
    }
    return head1->val<head2->val?head1:head2;
    }