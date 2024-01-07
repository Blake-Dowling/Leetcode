class Solution {
public:
    int reverse(int x) {
        if(x == 0 || x >= pow(2,31) || x <= -pow(2,31)){
            return 0;
        }
        int result = 0;
        int maxDigitIndex = log10(abs(x)); //2
        int digitIndex = maxDigitIndex; //2,1,0

        while(digitIndex >= 0){
            int tenPower = pow(10, digitIndex); //100,10,1
            int curValue = int(x / tenPower); //1,2,3
            if(result + curValue * pow(10, maxDigitIndex - digitIndex) >= pow(2,31) || \
                result + curValue * pow(10, maxDigitIndex - digitIndex) < -pow(2,31)){
                    return 0;
            }
            result += curValue * pow(10, maxDigitIndex - digitIndex); //1,20,300
            curValue *= tenPower; //100,20,3
            x = x - curValue; //23,3,0
            digitIndex --; //2,1,0
        }
        return result;
    }
};