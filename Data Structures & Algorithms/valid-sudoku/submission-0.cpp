class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // verifying the rows (right to left)
        std::unordered_set<char> hashset;
        for (const vector<char>& i : board){
            for (const char j : i){
                if (j == '.') continue;
                else{
                    if(hashset.count(j)) return false;
                    else hashset.insert(j);
                }
            }
            hashset.clear();
        }
        // verifying the rows (top to bottom)
        for (int i = 0; i < 9; ++i){
            for (int j = 0; j < 9; ++j){
                if (board[j][i] == '.') continue;
                else {
                    if (hashset.count(board[j][i])) return false;
                    else hashset.insert(board[j][i]);
                }
            }
            hashset.clear();
        }
        // verifying each block
        auto isBlockClear = [](int startIndex_X, int startIndex_Y, vector<vector<char>>& data) {
            std::unordered_set<char> hashset;
            for (int i = startIndex_X; i < startIndex_X + 3; i++){
                for (int j = startIndex_Y; j < startIndex_Y + 3; j++){
                    if (data[i][j] == '.') continue;
                    else {
                        if (hashset.count(data[i][j])) return false;
                        else hashset.insert(data[i][j]);
                    }
                }
            }
            return true;
        };

        // since the constraint basically says it is 9x9, send hardcoded values
        vector<array<int,2>> squareIndex = {{0,0},{0,3},{0,6},
                                            {3,0},{3,3},{3,6},
                                            {6,0},{6,3},{6,6}};
        for (auto i : squareIndex){
            if (isBlockClear(i[0],i[1],board)) continue;
            else return false;
        }
        return true;
    }
};
