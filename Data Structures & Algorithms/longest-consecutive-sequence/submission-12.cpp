class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        std::unordered_set<int> hashset;
        std::unordered_set<int> startIndex;

        hashset.insert(nums.begin(), nums.end());
        for (int i : nums){
            if (hashset.count(i+1)){
                startIndex.insert(i);
            }
        }
        std::vector<int> counts;
        for (int i : startIndex){
            int counter = 1;
            for (int j = 1; j < nums.size(); j++){
                if (hashset.count(i+j)) ++counter;
                else break;
            }
            counts.push_back(counter);
        }
        if (startIndex.size() > 0)
            return static_cast<int>(*std::max_element(counts.begin(), counts.end()));
        else return 1;
    }
};
