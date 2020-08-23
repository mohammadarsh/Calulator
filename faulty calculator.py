#program make a simple calculator
#the function add two number
def multiply(x,y):
    if x==45 and y==3:
        return 555
    else:
        return int(x)*int(y)

def add(x,y):
    if x==56 and y==9:
        return 77
    else:
        return int(x)+int(y)

def divide(x,y):
    if x==56 and y==6:
        return 4
    else:
        return int(x)/int(y)


print("select operation")
print("1.Add")
print("2.subtract")
print("3.Multiplication")
print("4.divides")

while True:
    choice = input("enter choice(1/2/3/4):")
    #check if choice on of the four option
    if choice in ('1','2','3','4'):
        num1=int(input("Enter first Number"))
        num2=int(input("Enter second Number"))

        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))
        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))
        elif choice=='4':
            print(num1,"/",num2,divide(num1,num2))
        break
    else:
        print("invalid input")
