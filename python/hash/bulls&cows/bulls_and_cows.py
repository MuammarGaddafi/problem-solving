class Solution(object):
    def getHint(self, secret, guess):
        hashmap={}
        for i in range(len(secret)) :
            if secret[i] in hashmap :
                hashmap[secret[i]].append(i)
            else :
                hashmap[secret[i]]=[i]

        guessmap={}
        for i in range(len(guess)) :
            if guess[i] in guessmap :
                guessmap[guess[i]].append(i)
            elif (guess[i] in hashmap and ( guess[i] not in guessmap)) :
                guessmap[guess[i]]=[i]


        bulls=0
        cows=0
        for element in guessmap :

            intersection = (set(guessmap[element]) & set(hashmap[element])) #the intersection is the commun digits with same index which are bulls
            bulls= bulls+len(intersection)
            if (len(hashmap[element])-len(intersection))>= (len(guessmap[element])-len(intersection)) :
                cows=cows+(len(guessmap[element])-len(intersection))
            elif len(hashmap[element])!=len(intersection) and len(guessmap[element]) > len(hashmap[element]) :
                cows=cows+(len(hashmap[element])-len(intersection))

        output= str(bulls)+"A"+str(cows)+"B"
        return(output)



