class Solution {
public:
    int integerBreak(int n) {
        if(n <= 3)
            return n-1;
        int num_threes = (int(n/3) - int(n%3 == 1));
        int product = pow(3, num_threes);
        int non_three = (n - 3*num_threes);
        if(non_three)
            product = non_three * product;
        return product;
    }
};