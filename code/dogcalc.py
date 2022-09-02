# Python programme to calculate a dogs age in dog years

h_age = int(input("Input a dog's age in human years: ")) # ask for input

if h_age < 0: # if age is less the 0
    print("Age must be positive number.") # print asking for number over zero

elif h_age <= 2:
    d_age = h_age * 10.5 # function calculte

else:
    d_age = 21 + (h_age - 2) * 4

print ("The dog's age in dog's years is", d_age) # print the answer
