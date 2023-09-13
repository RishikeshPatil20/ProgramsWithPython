#0,1,1,2,3,5,8,13


n=int(input("Enter a number : "))

def fibonacci_sequence(n):
    a=0
    b=1
    for x in range(0,n):
        c=a+b
        a=b
        b=c
        print(c)

fibonacci_sequence(n)
