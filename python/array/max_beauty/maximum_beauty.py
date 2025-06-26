""" this solutions as it's shown in the read me file (the photo) is based on the ranges intersection after sorting the array,
if nums[0]+k >= nums[1]-k then it means that the ranges intersect"""


class Solution(object):
    def maximumBeauty(self, nums, k):
        nums.sort()
        beauty_seq=1
        i=0
        while len(nums)>=beauty_seq and  i<(len(nums)-1) : #we should make sure that the process stop when the rest of the array is shorter than the current beauty seq, therefore there's no need to continue
            current_beauty=1
            test=True
            j=i+1
            while test==True and  j<=(len(nums)-1) :
                if (nums[i]+k)>= (nums[j]-k) :
                    current_beauty=current_beauty+1
                    j=j+1
                else :
                    test=False
                    
            if current_beauty>beauty_seq :
                beauty_seq=current_beauty
            i=i+1
        return(beauty_seq)


