class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> longest = vector<int>(s.size(), 1);
        int i = s.size()-2;
        int window = s.size();
        while(i >= 0){
            int j = i+1;
            while(j < window){
                if(s[j] == s[i]){
                    window = j;
                    break;
                }
                longest[i] ++;
                j++;
            }
            i--;
        }
        int longestVal = 0;
        for(int i = 0; i < longest.size(); i ++){
            if(longest[i] > longestVal){
                longestVal = longest[i];
            }
        }
        return longestVal;
    }
};