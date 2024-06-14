class Solution {
public:
    bool isPalindrome(int x) {
    if (x<0 || (x>0 && x % 10 == 0)) return false;
    int y = x;
    int result = 0;
    while (y > 0)
    {
        result = result * 10 + y % 10;
        y = y / 10;
    }
    if (x == result) return true;
    return false;
    }
};