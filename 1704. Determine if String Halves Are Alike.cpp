class Solution {
public:
    set<char> vowels; 
    Solution(){
        vowels = set<char>{65,69,73,79,85,97,101,105,111,117};
    }
    bool halvesAreAlike(string s) {
        int numVowels = 0;
        for(int i=0; i < s.size()/2; i ++){
            numVowels += ((this->vowels).find(s[i]) != vowels.end());
        }
        for(int i=s.size()/2; i < s.size(); i ++){
            numVowels -= ((this->vowels).find(s[i]) != vowels.end());
        }
        return numVowels == 0;
    }
};