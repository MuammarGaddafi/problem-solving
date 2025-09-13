class Solution(object):
    def isValid(self, s):
        hashmap= { ']' : '[' , ')' : '(' , '}' : '{'} 
        stack=[]
        for i in s : 

            if i in hashmap.values() : 
                stack.append(i)

            elif i in hashmap : 
                if  (not stack)==True or hashmap[i]!=stack[-1] : # not list checks if the list empty or not, the second condition is comparing the actual element with the top of the stack
                    return False
                elif hashmap[i]==stack[-1] :
                    stack.pop()
            
        return(not stack)

       