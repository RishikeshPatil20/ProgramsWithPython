num=int(input("Enter a number"))#5445
num2=num
temp=0

while num2 > 0:
    temp=temp*10+num2 % 10
    num2=num2//10
    
if(temp==num):
    print("Number is pallindrone number")
else:
    print ("Numbr is not a palndrone number")