def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print("The Gmean is:", mean)

a = 19
b = 12
calculateGmean(a,b)


# 2nd Function
def isGreater(a,b):
    if(a>b):
        print(a,"is greater than", b)
    else:
        print(b,"is greater than", a)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
isGreater(a,b)