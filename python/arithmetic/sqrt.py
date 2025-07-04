class Solution(object):
    def mySqrt(self, x):
        sqrt=0
        if x==0 :
            return(sqrt)
        else :
            i=1
            while (sqrt==0) :
                if i*i>x :
                    sqrt=i-1
                else :
                    i=i+1
        
    
        return(sqrt)
            
        
        
        