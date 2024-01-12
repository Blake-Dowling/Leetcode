class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        vector<int> minCost = vector<int>(cost.size(), 0);
        minCost[minCost.size()-1] = cost[cost.size()-1];
        minCost[minCost.size()-2] = cost[cost.size()-2];
        for(int i=cost.size()-3; i>=0; i --){
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2]);
        }
        return min(minCost[0], minCost[1]);
    }
};