class Solution {
public:
    int BinSearch(int min, int max, int tg, vector<int>& numbers){
            if (min > max)
                return -1;

            int mid = min + (max - min) / 2;
            if (numbers[mid] == tg)
                return mid;
            else if (numbers[mid] < tg)
                return BinSearch(mid+1,max,tg, numbers);
            else if (numbers[mid] > tg)
                return BinSearch(min,mid-1,tg, numbers);
        }
    vector<int> twoSum(vector<int>& numbers, int target) {
        int length = numbers.size();
        vector<int> arr;
        for (int i = 0; i < length; i++){
            int first_element = numbers[i];
            int difference = target - first_element;
            int value = BinSearch(i+1, length-1, difference, numbers);
            if (value == -1)
                continue;
            arr.insert(arr.end(), {i+1,value+1});
            break;
        }
        return arr;
    }
};
