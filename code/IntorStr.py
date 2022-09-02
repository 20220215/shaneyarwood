# Programme to see if its a string or a integer

text = input ("Input a string: ") # ask for a string
text = text.strip()

if len (text) < 1:
    print ("Input a valid text") # func ask for valid text is less then one

else:
    if all (text[i] in "0123456789" for i in range(len(text))):
        print ("The string is an integer.") # func if its  0123456789 print its a integer

    elif (text[0] in "+-") and \
            all (text[i] in "0123456789" for i in range(1, len(text))):
        print ("The string is an integer.") # else if stat print its is a integer

    else:
        print ("The string is not an integer.") # any other input print its not a integer
