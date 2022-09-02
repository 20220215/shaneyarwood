# programme to find the sum and average of 10 integers

Sum = 0

print ("Enter 10 integers\n") # ask for the numbers
i = 1

while (i <= 10):
    num = int(input("integer %d = " %i))
    Sum = Sum + num # function to calculate
    i = i + 1

avg = Sum / 10 # average = sum divide by 10

print ("the sum of the integers = ", Sum) # print sum of integers
print ("the average of the integers  = ", avg) # print average of integers
