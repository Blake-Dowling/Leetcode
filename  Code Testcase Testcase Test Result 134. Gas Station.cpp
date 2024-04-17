class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int total_net = 0;
        int cur_net = 0;
        int start = 0;
        for(int i=0; i<gas.size(); i++){
            total_net += gas[i] - cost[i];
            cur_net += gas[i] - cost[i];
            if(cur_net < 0){
                start = i+1;
                cur_net = 0;
            }
        }
        return (total_net>=0)?start:-1;
    }
};