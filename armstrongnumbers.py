num =  int(input(" enter a numbers :"))
temp = num
sum = 0
while num > 0 :
    r=num%10
    sum=sum+r*r*r
    num=num//10
if temp==sum :
    print("is a armstrong number ")
else :
    print("not a armstrong number")