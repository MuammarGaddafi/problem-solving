class Solution(object):
    def findSubstring(self, s, words):
        hashmap1={}
        for elt in words :
            if elt in hashmap1 :
                hashmap1[elt] += 1
            else :
                hashmap1[elt]=1
        wordlen=len(words[0])
        deb=0 # this is the debut value of the sliding window
        end= (len(words)*wordlen)-1 # this is the start value of the end of sliding window 
        output=list()
        for end in range (end,len(s)) :
            hashmap2={}
            test=True
            substring=s[deb:end+1]
            j=0
            while test==True and j<=(len(substring)-1) :
                if substring[j:j+wordlen] in hashmap1  and substring[j:j+wordlen] in hashmap2  :
                    hashmap2[substring[j:j+wordlen]] +=1
                elif substring[j:j+wordlen] in hashmap1  and substring[j:j+wordlen] not in hashmap2 :
                    hashmap2[substring[j:j+wordlen]] = 1
                elif substring[j:j+wordlen] not in hashmap1 :
                    test=False
                j=j+wordlen
            if hashmap1==hashmap2 :
                output.append(deb)
            deb=deb+1
        return(output)





        
