#include <vector>
#include <algorithm>
#include <iostream>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::vector<int> res;

        for (int i = 0; i < nums.size() - 1; i++) {

            int search = target - nums[i];
            auto pos = std::find(nums.begin() + i + 1, nums.end(), search);  // find would returns the index of first occurance in the vector, and if not found would return nums.end() !!! it returns an iterator, thats why we should adjust the output

            if (pos != nums.end()) {
                int index = std::distance(nums.begin(), pos);// distance returns to us the index of the found element depending on pos
                res = {i, index};
                break;
            }
        }

        return res;
    }
};