n=7
hashset=set()
test=False
while (test==False)  and (n not in hashset) :
    somme=0
    hashset.add(n)
    while n!=0 : 
        somme=somme + (n%10)**2
        n=n//10
    if somme==1 : 
        test=True
    n=somme

print(test)