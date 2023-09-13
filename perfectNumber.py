num=int(input("Enter a number : "))
temp=0
def perfectNumber(num):
    global temp
    for x in range(1,num,1):
        if (num%x==0):
            temp=temp +x
    
perfectNumber(num)
if num == temp:
    print(str(num)+"is a perfect number")
