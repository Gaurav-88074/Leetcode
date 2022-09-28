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
    int index;
    int n;
    ListNode* get(ListNode* head,int size){
        if(head==NULL){
            this->index = size-n;
            return head;
        }
        head->next = get(head->next,size+1);
        if(index==size){
            return head->next;
        }
        return head;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        this->n = n;
        this->index = 0;
        return get(head,0);
    }
};