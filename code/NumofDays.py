# program to convert month name to a number of days

month_name = input ("Input the name of Month: ") # ask user for month

if month_name == "February":
	print ("No. of days: 28/29 days") # function if feb  print numnber is 28 or 29

elif month_name in ("April", "June", "September", "November"):
	print ("No. of days: 30 days") # function if month apr jun sep nuv print 30

elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
	print ("No. of days: 31 day") # if other days entered print 31

else:
	print ("not a month") # function if anything else entered print not a month
