class Solution(object):
    def isHappy(self, n):
        hashset=set()
        test=False
        while (test==False)  and (n not in hashset) :
            somme=0
            hashset.add(n)
            while n!=0 : 
                somme=somme + (n%10)**2
                n=n//10
            if somme==1 : 
                test=True
            n=somme

        return(test)
            

"""
Approach
we use the hashset to store every new n value ( to avoid the infenitive loop, when n takes an already existed value in the hashset, we end the loop and return false )

how to get every n digit each time ? :
we divide n (//) by 10 every number divided (//) by ten : the rest is the last digit of the number and the we assigns the result as the new value of n :
n=147
n%10=7
n//10=14
we continue the process until n=0

"""
