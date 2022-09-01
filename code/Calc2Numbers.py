 Take two numbers and add, divide, multiply or subtract them

num1 = 0  # first variable

num2 = 0  # second variable

result = 0 # result

num1 = int(input("Enter First Number: "))  # asking first number

opp = input("Choose an operation --> + - * / : ") # choose the operation

num2 = int(input("Enter Second Number: "))  # ask second number

if (opp == '+'):
    result = num1 + num2 # addition of both numbers

elif (opp == '-'):
    result = num1 - num2 # subtraction of both numbers

elif (opp == '*'):
    result = num1 * num2 # Multiply both numbers

elif (opp == '/'):
    result = num1 / num2; # divide both numbers

else:
    print("Wrong Input!!!") # they entered in the wrong operation


print("The result is of Two Numbers is ", result) # printing the results
