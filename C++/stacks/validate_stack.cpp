class Solution {
public:
    bool validateStackSequences(std::vector<int>& pushed, std::vector<int>& popped) {
        std::stack<int> ourstack;
        int ppindx = 0;

        for (int i = 0; i < pushed.size(); ++i) {
            ourstack.push(pushed[i]);

            while (!ourstack.empty() && ourstack.top() == popped[ppindx]) {
                ourstack.pop();
                ++ppindx;
            }
        }

        return ourstack.empty();
    }
};