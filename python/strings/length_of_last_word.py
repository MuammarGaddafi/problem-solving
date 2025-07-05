class Solution(object):
    def lengthOfLastWord(self, s):
        i=len(s)-1
        while s[i]==" " :
            i=i-1
        last=i
        while i>=0 and s[i]!=" " : #it should be i>=0 not i>0 other wise the last iteration would not be counted if the we have reached the first element of the string 
            i=i-1
        return((last-i)) #we dont put (last-i)+1 because there is already an additional iteration before quitting the loop so last-i doesnt count it : example : hello word could quit after counting the iteration of the space before "world"

    

    
        
"""
does not need much concentration to understand, just first loop to trach the start of the end of the last world,
 named last, the second loop to track the start of the last world, which is the counter i,
 we added i>=0 case because the string could be
 composed of only one world, so the start index of the last world is the start index of the string if there is no spaces before it
"""