/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* compute(ListNode* head,ListNode* prev,int i){
        if(head==NULL){
            return head;
        }
        compute(head->next,head,i+1);
        if (i%2==0 && prev!=NULL){
            int a = prev->val;
            prev->val=head->val;
            head->val=a;
        }
        return head;
    }
    ListNode* swapPairs(ListNode* head) {
        
        return compute(head,NULL,1);
    }
};