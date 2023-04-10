template <typename Type>
class Node{
    public:
        Type data;
        Node * next=NULL;
        Node(Type data){
            this->data = data;    
    }
};
template <typename Type>
// template <class Type>
class Stack {
    private:
        Node<Type> *head = NULL;
    public:
        void push(Type data){
            Node<Type> * toAdd = new Node<Type>(data);
            if(head==NULL){
                head=toAdd;
                return;
            }
            toAdd->next=head;
            head=toAdd;
        }
        void pop(){
            if(head==NULL){
                // cout<<"Stack Underflow!!"<<endl;
                return ;
            }
            head = head->next;
        }
        Type peek(){
            if(head==NULL){
                // cout<<"Stack is Empty!!"<<endl;
                return 'n';
            }
            return head->data;
            
        }
        bool isEmpty(){
            return head==NULL;
        }
        void print(){
            Node<Type> *temp = head;
            cout<<"[ ";
            while (temp!=NULL)
            {
                cout<<temp->data<<" ";
                temp=temp->next;
            }
            cout<<"]"<<endl;;
        }

};

    
class Solution {
public:
    bool isValid(string s) {
        Stack<char>* l = new Stack<char>();
        // string s;
        // // cout<<"enter your input:";
        // cin.get();
        // cin>>s;
        bool flag=true;
        for (int i = 0; i < s.size(); i++)
        {
            if( s[i]=='{'||
                s[i]=='['||
                s[i]=='('){
                l->push(s[i]);
                continue;
            }
            if(s[i]=='}' && l->peek()=='{'){
                l->pop();
            }
            else if(s[i]==']' && l->peek()=='['){
                l->pop();
            }
            else if(s[i]==')' && l->peek()=='('){
                l->pop();
            }
            else{
                flag=false;
            }
        }
        if(l->isEmpty() && flag){
            return true;
        }
        else{
            return false;
        }
    }
};

//--------------
        
        
        
        