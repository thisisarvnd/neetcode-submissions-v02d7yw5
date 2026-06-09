class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        // brute forcing just to check TLE and to get a flow

        // THIS IS RIDICULOUS
        // I did the same in Python and it got TLE-d
        // The same inefficient solution in C++ got accepted
        // 2500ms vs 308ms
        // python loops are terrible
        vector<vector<int>> solution;
        int n = nums.size();
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                for (int k = j + 1; k < n; k++) {
                    
                    if (nums[i] + nums[j] + nums[k] == 0) {
                        vector<int> pairs = {nums[i], nums[j], nums[k]};
                        sort(pairs.begin(), pairs.end());
                        
                        // Replicating "if pairs in solution:"
                        if (find(solution.begin(), solution.end(), pairs) != solution.end()) {
                            continue;
                        } else {
                            solution.push_back(pairs);
                        }
                    }
                    
                }
            }
        }
        return solution;
    }
};