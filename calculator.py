#program make a simple calculator
#the function add two number
def add(x,y):
    return x+y

#the fuction subtracts two number
def subtract(x,y):
    return x-y
#the funtion multiplies two number
def multiply(x,y):
    return x*y
#the function divides two number
def divide(x,y):
    return x/y

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











