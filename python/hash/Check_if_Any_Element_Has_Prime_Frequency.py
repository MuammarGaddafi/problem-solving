"""
run time beats 100%, memory beats 99.3% on leetcode 
approach :

when you understand the hashmap concepts, it is no longer a complexe thing to solve, we have made a loop over the array to store every element in the hashmap as a key and its occurence as value, when we find an existing element in the hashmap, we increment its value which is its number of occurences,
then we simply loop over the hashmap values and once we get a prime value we return True otherwise we return False (the prime function would handle the track of prime numbers)
"""

class Solution(object):
    def checkPrimeFrequency(self, nums):
        def prime(a) :
            if a<2 :
                return(False)
            else :
                test=True
                i=1
                nbdiv=1
                while test==True and i<=(a//2):
                    if a%i==0 :
                        nbdiv=nbdiv+1
                    if nbdiv>2 :
                        test=False
                    i=i+1
                return(test)
        hashmap={}
        for i in range (len(nums)) :
            if nums[i] in hashmap :
                hashmap[nums[i]]=hashmap[nums[i]]+1
            else :
                hashmap[nums[i]]=1
        verif=False
        for element in hashmap.values() :
            if prime(element) :
                verif=True
                break
        return(verif)


