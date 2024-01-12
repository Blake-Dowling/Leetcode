//Beats 100%
class Solution {
public:
    int tribonacci(int n) {
        int* tribs = (int*)calloc(max(3, n+1), sizeof(int));
        tribs[1] = 1;
        tribs[2] = 1;
        for(int i=3; i<=n; i++){
            tribs[i] = tribs[i-3] + tribs[i-2] + tribs[i-1];
        }
        return tribs[n];
    }
};