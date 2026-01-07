#include<iostream> 
#include<vector>

using namespace std ;

class Solution {
public:
    int findMin(vector<int>& nums) {
        
        
int right= nums.size() - 1 ; 

int left = 0 ; 

int middle = ((nums.size())/2) ; 



while ( right > left )  {


    if ( nums[middle] > nums[right]) {

        // we used the right element in the comparison, because it may the rotated element is in the right so the ascending numbers may be broken at certain point 

        cout << nums[right] << endl;
        left = middle + 1 ;
        middle =  left + (( right - left ) / 2 ) ; 
    }


    
    else  {

        right = middle  ; 
        middle =  left + (( right - left ) / 2 ) ; 
    }


}



    return nums[left]  ;

};

} ;