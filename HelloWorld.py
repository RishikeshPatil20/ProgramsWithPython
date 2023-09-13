
num=0

def checkglobal():
    try:
        global num
        num=int(input("Enter a number : "))
        if(num==10):
            print (num)
        else:
            print(str(num)+" is value of 10")
    except Exception as e:
        print(e)
checkglobal()
print ("all good")
