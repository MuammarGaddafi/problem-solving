/*
Approach :
may be the solution seems to be dumb,
 but it prooved its effectivenes in terms of run time and memory,
  i simply trachked the possible cases, negative ints could rise some troubles in some cases, cz sometimes the product of the 2 smallest negative ints could make a huge difference, so i made 3 possible maximums (every maximum represents a specific case) and all those possible maximums would be put in a vector, than we return the maximum of the vector which contains all the possible maximums

Complexity ;
time complexity : beats 100%
space complecity : beats 95%
*/


#include<vector> 
#include<iostream>
#include<algorithm> // for std::sort function
using namespace std ;
class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int max1 , max2 , max3 ;
        sort(nums.begin(),nums.end()) ; //would sort the vector nums in place

        max1 = nums[nums.size()-1]*nums[nums.size()-2]*nums[nums.size()-3] ;
        max2 = nums[nums.size()-1]*nums[nums.size()-2]*nums[0];
        max3= nums[0]*nums[1]*nums[nums.size()-1];
         vector<int> maximums={max1,max2,max3};
        int maxval = *max_element(maximums.begin(), maximums.end());





return maxval ;
    }
};


/* problem description : 

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

Example 1:

Input: nums = [1,2,3]
Output: 6
Example 2:

Input: nums = [1,2,3,4]
Output: 24
Example 3:

Input: nums = [-1,-2,-3]
Output: -6
 



*/