num =int(input("enter your salary") )
num1 =num + (10/100) * num
num2 =num + (20/100) * num
num3 =num + (40/100) * num
if(num<=1000) :
    print("your salary is :",num1)
elif(num >1000 and num<=2000) :
    print("your salary is :",num2)
elif(num >2000) :
    print("your salary is :",num3)
else :
    print("you are fired ")