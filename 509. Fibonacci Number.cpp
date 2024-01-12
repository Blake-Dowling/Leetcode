class Solution {
public:
    int fib(int n) {
        if(n < 2){
            return n;
        }
        int* fibs = (int*)calloc(n+1, sizeof(int));
        fibs[1] = 1;
        for(int i=2; i<=n; i++){
            fibs[i] = fibs[i-2] + fibs[i-1];
        }
        return fibs[n];
    }
};