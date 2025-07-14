class Solution(object):
    def stringHash(self, s, k):
        new_string=""
        for i in range (0,len(s),k) :
            count=0
            for j in range (i,i+k) :
                count=count+(ord(s[j])-97)
                print(count)
            new_string=new_string+chr((count%26)+97)

        return(new_string)
            
        
        
