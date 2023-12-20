class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> list = vector<int>(n+1, 0);
        for(int i=0; i<=n; i++){
            list[i] = list[int(i/2)] + i%2;
        }
        return list;
    }
};