from tkinter import *

# centimetres to inches
def CtoI_but():
	global expression
	total = float(expression) / 2.54
	equation.set(' ' + str(total))

# inches to centimetres

def ItoC():
	global expression
	total = float(expression) * 2.54
	equation.set(' ' + str(total))

# clear button
def clear_but():
    global expression
    expression = ""
    equation.set("")

# button press

expression = ' '

def button_press(but):
	global expression
	expression = expression + str(but)
	equation.set(expression)


# equal press

def equals_but():
	try:
		global expression
		total = str(eval(expression))
		short_total = round(float(total), 3)
		equation.set(' ' + str(short_total))
		expression = str(short_total)
	except:
		equation.set( 'error' )
		expression = ' '

# gui and tk
gui = Tk()
gui.configure(background="lightblue")
gui.title("Calculator 20220215 IT 4004 ")
gui.geometry("400x300")
equation = DoubleVar()
ExpressionInput = Entry(gui, textvariable=equation, background="white", font="15")
ExpressionInput.grid(columnspan=5, ipadx=96.5, ipady=10)
equation.set(' 0 ')


# buttons
clear = Button(gui, text='clear', fg='black', bg='orange', height=2, width=7, command=clear_but)
plus = Button(gui, text='+', fg='black', bg='pink', height=2, width=7, command=lambda: button_press('+') )
minus = Button(gui, text='-', fg='black', bg='pink', height=2, width=7, command=lambda: button_press('-') )
divide = Button(gui, text='\u00F7', fg='black', bg='pink', height=2, width=7, command=lambda: button_press('/') )
multiply = Button(gui, text='*', fg='black', bg='pink', height=2, width=7, command=lambda: button_press('*') )
equal = Button(gui, text='=', fg='black', bg='pink', height=2, width=7, command=equals_but)
zero = Button(gui, text='0', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(0) )
button1 = Button(gui, text='1', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(1) )
button2 = Button(gui, text='2', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(2) )
button3 = Button(gui, text='3', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(3) )
button4 = Button(gui, text='4', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(4) )
button5 = Button(gui, text='5', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(5) )
button6 = Button(gui, text='6', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(6) )
button7 = Button(gui, text='7', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(7) )
button8 = Button(gui, text='8', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(8) )
button9 = Button(gui, text='9', fg='black', bg='aqua', height=2, width=7, command=lambda: button_press(9) )
CtoI = Button(gui, text='cm to inch', fg='black', bg='pink', height=2, width=19, command=CtoI_but)
ItoC = Button(gui, text='inch to cm', fg='black', bg='pink', height=2, width=19, command=ItoC )

# button row 1
button1.grid(row=1, column=0, padx=10, pady=10)
button2.grid(row=1, column=1, padx=10, pady=10)
button3.grid(row=1, column=2, padx=10, pady=10)
plus.grid(row=1, column=3, padx=10, pady=10)
minus.grid(row=1, column=4, padx=10, pady=10)

# button row 2
button4.grid(row=2, column=0, padx=10, pady=10)
button5.grid(row=2, column=1, padx=10, pady=10)
button6.grid(row=2, column=2, padx=10, pady=10)
divide.grid(row=2, column=3, padx=10, pady=10)
multiply.grid(row=2, column=4, padx=10, pady=10)

# button row 3
button7.grid(row=3, column=0, padx=10, pady=10)
button8.grid(row=3, column=1, padx=10, pady=10)
button9.grid(row=3, column=2, padx=10, pady=10)
clear.grid(row=3, column=3, padx=10, pady=10)
equal.grid(row=3, column=4, padx=10, pady=10)

# button row 4
CtoI.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
zero.grid(row=4, column=2, padx=10, pady=10)
ItoC.grid(row=4, column=3, columnspan=2, padx=10, pady=10)


# the last line
gui.mainloop()