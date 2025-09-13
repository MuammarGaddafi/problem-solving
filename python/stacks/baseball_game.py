class Solution(object):
    def calPoints(self, ops):
        record_stack=[]
        for i in range (len(ops)) :
            if ops[i]=="C" :
                record_stack.pop()
            
            elif ops[i] == "D" :
                res=2*int(record_stack[-1])
                record_stack.append(str(res)) 

            elif ops[i]== "+" :
                res=0
                for i in range (len(record_stack)-1,len(record_stack)-3 , -1) :
                    res=res+int(record_stack[i])
                record_stack.append(str(res))
            else : 
                record_stack.append(ops[i])
        summ=0

        for i in range (len(record_stack)) :
            summ= summ + int(record_stack.pop())

        return(summ)
