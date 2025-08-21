class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest=0
        current_length=0
        i=0
        current_string=""
        current_string_debut_index=0
        while i <= len(s)-1 :
            if s[i] not in current_string :
                current_string=current_string + s[i]
                current_length+=1
                longest=max(longest,current_length)
            else : 
                longest=max(longest,current_length)
                pos=current_string.find(s[i])
                current_string_debut_index+=pos+1
                current_string=s[current_string_debut_index:i+1]
                current_length=len(current_string)
            i=i+1
            
        return(longest)
                            
           
        