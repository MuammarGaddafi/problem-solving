
class Solution(object):
    def reverseString(self, s):
        left=0
        right=len(s)-1
        while (left<=(len(s)//2)) and (right>=(len(s)//2)) :
            aux=s[right]
            s[right]=s[left]
            s[left]=aux
            right=right-1
            left=left+1
        return(s)

        