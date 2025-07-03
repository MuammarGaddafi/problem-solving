""" we have a target value we should reach it after adding up 2 values from the array
so the easiest way is to make hashmap, filling it with the array values in this form { value : index in the array},
 then we start to iterate through the table
and at every element we make y=(target - element) if y is in the hashmap so the job is done
we will do the same process but a little bit refined : we will make the entire job while we are filling the hashmap,
 once the condition is satisfied, it's finished """

# 1st method : the classical and friendly beginner one : we make a hashmap derivated from the array and then we start searching for the appropriate value every iteration :

hashmap={} # val : index
"""
for i in range len(nums):
    if nums[i] in hashmap :
        hashmap[nums[i]]=i 
    else :
        hashmap[nums[i]]=i
""" 
#but you should know that if u add to a dict a new value with an existing key, the dict would overwrite the existing key to store the new value, so there's no need for this if loop, the dict would always take the index of the latest duplicated value in the array
# so we'd rather do this :
for i in range (len(nums)): #filling the hash map
    hashmap[nums[i]]=i
for i in range(len(nums)):
    y=target-nums[i]
    if y in hashmap and hashmap[y] != i : #example target=6, nums[i]=3, y=3, if 3 index in hashmap different to i : it means it's a duplicate value of 3 so 3+3 is valid, if hashmao index is equal to i it means it's the same value not a duplicate and we cannot count the same element twice 
        return([i,hashmap[y]])




# second method : we do not have to track if the value is a duplicate of the y value or not, because we will do the process at the same time we are filling tha hash map, if the y exists in the hashmap it means the process is over otherwise we add nums[i] to the hashmap (!dont forget that y=target-nums[i])
# this the solution that i've adopted to solve the problem on leetcode
class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        test=False
        i=0
        while test==False :
            y=target-nums[i]
            if y in hashmap :
                answer=[hashmap[y],i]
                test=True
            #else
            hashmap[nums[i]]=i
            i=i+1
        return(answer)


