class Solution(object):
    def subStrHash(self, s, p, m, k, hashValue):
        def order(a) : # this function for returning the alphabet order of the character
            the_order= ord(a.upper())-64
            return (the_order)

        def hashfunc (s,p) : 
            res=0
            for i in range (len(s)) :
                res= res + order(s[i])*(p**i)
            return(res)

        # these are the sliding window limits
        # we will start from the botton, in purpose of making the rolling hash much more easier
        hash=0
        end=len(s)-1
        start=(end-k) + 1
        slice=s[start:end+1]
        hash=hashfunc(slice,p)
        for i in range (end,0,-1) :
            if hash%m == hashValue : 
                the_slice=s[start:end+1] 

            
            #moving the sliding window
            new_hash = hash - (   order(s[end])   *   (p**(k-1))      )
            hash= order(s[start-1]) + new_hash*p # here we rolled the hash, meaning we updated it
            start-=1
            end-=1
            slice=s[start:end+1]
            
        return(the_slice)




