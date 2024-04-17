class Solution {
public:
    int myAtoi(string s) {
        //whitespace
        char i = 0;
        while(s[i] == ' '){
            i ++;
        }
        //+ or -
        int multiplier = 1;
        if(s[i] == '-'){
            multiplier = -1;
            i ++;
        }
        else if(s[i] == '+'){
            i ++;
        }
        //get number
        long res = 0;
        while(i < s.length() && s[i] >= 48 && s[i] <= 57){
            res *= 10;
            res += s[i] - 48;
            i ++;
            if(res * multiplier >= INT_MAX){
                return INT_MAX;
            }
            if(res * multiplier <= INT_MIN){
                return INT_MIN;
            }
        }
        //apply multiplier
        res = res * multiplier;
        //cast to int
        res = min(res, (long)INT_MAX);
        int resInt = (int)max(res, (long)INT_MIN);
        return resInt;
    }
};