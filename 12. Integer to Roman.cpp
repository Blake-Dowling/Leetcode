class Solution {
public:
    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

    string intToRoman(int num) {
        if(num == 0){
            return "";
        }
        for(int i=0; i<values.size(); i++){
            if(num >= values[i]){
                return symbols[i] + intToRoman(num-values[i]);
            }
        }
        return "";
    }
};
