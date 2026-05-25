num1 = int(input("Enter No: "))
num2 = int(input("Enter No: "))
op = (input("Enter The Operator (+,-,/,*) : "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")