class Solution {
public:
    bool isPalindrome(int x) {
        while(1){
            //Base - negative or 1 digit
            if(x < 0){
                return false;
            }
            if(x < 10){
                return true;
            }
            //Compare first and last
            int first = (int)(x / pow(10 , (int)(log10(x))));
            int last = (int)(x % 10);
            if(first != last){
                return false;
            }
            //Remove first and last
            int firstWithSig = first * pow(10 , (int)(log10(x)));
            int numZeros = (int)(log10(x)) - (int)(log10(x - firstWithSig)) - 1;
            x = x - firstWithSig;
            x = (int)(x / 10);
            //Handle zeros
            while(numZeros > 0){
                last = (int)(x % 10);
                if(last != 0){
                    return false;
                }
                x = (int)(x / 10);
                numZeros --;
            }
        }
        return false;
    }
};