# temp conversion programme

print ("*************************")
print ("Temp conversion programme")
print ("**************************") # print the heading

choice = input ("enter 1 for celsius to fahrenheit,2 for fahrenheit to celsious or 3 to exit") # ask for which conversion

if choice == "1":
    c = int(input("whats the temp in celsius?")) # Function to calculate c to f
    f = (c * 9/5) + 32
    print("the temperature in fahrenheit is :" ,f)

elif choice == "2":
    f = int(input("whats the temperature in farenheit?")) # function to calculate f to c
    c = (f-32) *5/9
    print("the temperature in celsius is :" ,c)

elif choice == "3":
    exit # function to exit
