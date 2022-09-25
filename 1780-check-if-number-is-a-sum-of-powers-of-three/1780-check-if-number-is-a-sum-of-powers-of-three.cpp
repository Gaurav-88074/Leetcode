class Solution {
public:
    bool checkPowersOfThree(int n) {
        if(n <= 3) return (n == 1 || n == 3);
        if(n % 3 == 2)return false;
        return checkPowersOfThree(n/3);
    }
};