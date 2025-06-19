
class Solution (object) :
    def findErrorNums(se1f, nums) :
        myset=set(nums)
        dup=sum(nums)-sum(myset)
        n=len(nums)
        somme=0
        for i in range (1,n+1) :
            somme=somme+i
        miss=somme-sum(nums)+dup
        corr=[dup,miss]
        return(corr)

"""

9 lines simple python solution, no need to any deep math or programming knowledge, beats 63% of subs

Approach
we all know when we transform a list into a set it removes any duplicated value, so i substracted the sum of the set from the sum of nums list and the difference between them is the duplicated removed number after the set creation,therefore, we have the dup value.
and now to get the miss value you only have to calculate the sum of the original list(just for loop from 1 to length of the nums list to get it) and then substract from it the sum of nums list after that we add the dup value and now we get the miss value
miss value : ((sum of original list) - (sum of current list (nums))) + duplicate value (dup)

"""