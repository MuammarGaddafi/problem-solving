# we wood base on hashkey as a converter, we would assign all the key words to the hashkey with their conversion as a value
class Solution(object):
    def entityParser(self, text):
        convert_key={ "&quot;" :"\"" , "&apos;" : "'" , "&amp;" : "&" ,  "&gt;" : ">" , "&lt;" : "<" , "&frasl;" : "/" }

        # this for loop is for the whole text parsing : 
        i=0
        while i < (len(text)-1) :
            if text[i] == "&" :
                j=i 
                while True : 
                    j=j+1
                    if text[j]=="&" : # this bloc to avoid the error caused by finding a normal & on our way not the & that tracks the start of the entity key word, like this case : text = "and I quote: &&&frasl;...&quot;" the && before frasl entity should remain intact
                        i=j-1
                        entity=""
                        break
                    if text[j]==";" :
                        entity=text[i:j+1]
                        break
                if entity in convert_key :
                    text= text[:i] + convert_key[entity] + text[j+1:]
                i=i+1


            else : 
                i+=1
        return(text)
        
 