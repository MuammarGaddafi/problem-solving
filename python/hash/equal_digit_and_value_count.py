class Solution(object):
    def digitCount(self, nums):
        occurence_count_hash={}
        for i in range (len(nums)) :
            if nums[i] in occurence_count_hash :
                occurence_count_hash[nums[i]]+=1
            else :
                occurence_count_hash[nums[i]]=1
        i=0
        carry_on=True
        while carry_on and i<=(len(nums)-1) :
            # we will assign to each index i its occurence time in the nums string by using the occurence count hash
            if str(i) not in occurence_count_hash : 
                occur=0
            else :
                occur=occurence_count_hash[str(i)] 
            if occur != int(nums[i]) :
                carry_on=False
            i=i+1
        return(carry_on)
    


"""

we use a hashmap to store the occurence of each element in the num string

then we loop over the num string while the carry_on bool is true, each index (i) has an occur variable where we assign its occurence based on the hashmap ,
 if i does not exist in the hashmap it means it has 0 occurence
, so if the occurence of the index in num equals to its value,
 we carry on else w break out of the while loop and we return carry_on
   
"""