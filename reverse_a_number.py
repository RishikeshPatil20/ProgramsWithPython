def reverse_number():
    num = int(input("Enter a number "))
    temp=num
    reverse=0
    while (temp>0):
        reverse=reverse * 10+(temp%10)
        temp=temp//10
        
    print("The Given number is {} and Reverse is {}".format(num, reverse))
reverse_number()