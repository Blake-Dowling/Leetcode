class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> answer = vector<int>(temperatures.size(), 0);
        vector<int> stack = vector<int>(0);
        int i = 0;
        while(i < temperatures.size()-1){
            stack.push_back(i);
            i ++;
            while(stack.size() > 0 && temperatures[i] > temperatures[stack.back()]){
                answer[stack.back()] = i - stack.back();
                stack.pop_back();
            }
            
        }
        return answer;
    }
};