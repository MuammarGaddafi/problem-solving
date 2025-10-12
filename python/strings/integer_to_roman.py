class Solution(object):
    def intToRoman(self, nums):

        nums= str(nums)
        normal_map={ "0" : "I" , "1" : "X" , "2" : "C" , "3" : "M" }

        five_map =  {"0" : "V" , "1" : "L" , "2" : "D"}




        roman="" 

        


        for i in range ( len(nums)) : 

            coeff= (len(nums)-1) - i 

            if nums[i] == "4" : 

                roman = roman + normal_map[str(coeff)] + five_map[str(coeff)] 

            elif nums[i] == "9" : 

                roman = roman + normal_map[str(coeff)] + normal_map[str(coeff + 1)] 

            elif int(nums[i]) < 4 : 

                roman = roman + normal_map[str(coeff)]*int(nums[i]) 

            elif    5  <= int(nums[i]) < 9 :

                roman = roman + five_map[str(coeff)] + normal_map[str(coeff)]*( int(nums[i]) - 5 ) 


        return(roman)

            

example=Solution()
output=example.intToRoman(1203) 
print(output)
     





