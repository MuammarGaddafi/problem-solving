class Solution(object):
    def groupAnagrams(self, strs):
        hashmap={}
        for i in range (len(strs)) :
            sorted_word=''.join(sorted(strs[i])) #joining the sorted list is optional just for more clarity and to return the result of the sorted into a string word
            if sorted_word in hashmap :
                hashmap[sorted_word].append(strs[i])
            else : 
                hashmap[sorted_word]=[strs[i]]

        output=[]
        for element in hashmap : 
            output.append(hashmap[element])

        return(output)