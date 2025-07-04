class Solution(object):
    def isArraySpecial(self, nums):
        if len(nums)==1 :
             return(True)
        else :
            cont=True
            i=0
            while cont==True and i<(len(nums)-1):
                if (nums[i]%2)==(nums[i+1]%2) :
                    cont=False 
                #else
                i=i+1
            return(cont)
                
