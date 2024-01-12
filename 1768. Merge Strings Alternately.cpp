class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        char* s = (char*)malloc(sizeof(char)*(word1.size() + word2.size() + 1));
        bzero(s, sizeof(char)*(word1.size() + word2.size() + 1));
        int i = 0;
        int j = 0;
        while(i<min(word1.size(), word2.size())){
            s[i*2] = word1[i];
            i ++;
        }
        while(j<min(word1.size(), word2.size())){
            s[1+(j*2)] = word2[j];
            j ++;
        }
        while(i<word1.size()){
            s[i+j] = word1[i];
            i ++;
        }
        while(j<word2.size()){
            s[i+j] = word2[j];
            j ++;
        }
        return s;
    }
};