#include <algorithm>
class Solution {
public:

    int buyChoco(vector<int>& prices, int money) {
        std::sort(prices.begin(), prices.end(), [](int a, int b){return a < b;});
        int leftover = money - (prices[0] + prices[1]);
        return leftover >= 0 ? leftover : money;
    }
};