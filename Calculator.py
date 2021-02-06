from tkinter import *
from math import *
win = Tk() 
win.title("Calculator") # this title will be displayed on the top of the app
#win.geometry("300x400") # this defines the size of the app of window
input_box=StringVar()
e = Entry(win,width = 35, borderwidth = 5,textvariable=input_box) # this defines the size of the entry box for user input
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10) # this displays the entry box on the top
expression = "" # Initiate the variable expression

def button_click(num): # this function generates expression when any button is clicked
    global expression
    expression = expression + str(num)
    input_box.set(expression)
    return

def Button_Clear(): # clears the contents of the entry box
    global expression
    expression = ""
    input_box.set(expression)
    return

def Button_Equal(): # evaluates the expression in the entry box and displays the result
    global expression
    result = str(eval(expression))
    expression = result
    input_box.set(expression)
    return

def  factorial(num):
    num1=int(num)
    prod = num1
    while num1 > 1:
        prod=prod*(num1-1)
        num1=num1-1
    global expression
    expression=str(prod)
    input_box.set(expression)

def factors():
    List1=[]
    num=int(e.get())
    e.delete(0,END)
    for i in range(1,num+1):
        if num%i==0:
            List1.append(i)
            List1.append(',')
    List1.pop()
    input_box.set(List1)

def Abs():
    global expression
    ab=abs(eval(expression))
    e.delete(0,END)
    expression=ab
    input_box.set(expression)
    pass

def pn():
    global expression
    listfactors=[]
    for i in range(1,eval(expression)+1):
        if eval(expression)%i==0:
            listfactors.append(i)
    if len(listfactors)==2:
        input_box.set(expression  =' is a prime number,')
    else :
        input_box.set(expression+' is a composite number.')
    if len(listfactors)==1:
        input_bpx.set(expression+' is neither a prime nor a compsite number.')

def Sqrt():
    global expression
    sqr=sqrt(eval(expression))
    expression=sqr
    input_box.set(expression)

def sqr:
    global expression
    Sqr=eval(expression)*eval(expression)
    expression=Sqr
    input_box.set(expression)
  
#Defining Buttons (what they should display and what they should do)
button_1 = Button(win, text="1", padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(win, text="2", padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(win, text="3", padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(win, text="4", padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(win, text='5', padx=40,pady=20, command = lambda: button_click(5))
button_6 = Button(win, text='6', padx=40,pady=20, command = lambda: button_click(6))
button_7 = Button(win, text='7', padx=40,pady=20, command = lambda: button_click(7))
button_8 = Button(win, text='8', padx=40,pady=20, command = lambda: button_click(8))
button_9 = Button(win, text='9', padx=40,pady=20, command = lambda: button_click(9))
button_0 = Button(win, text='0', padx=40,pady=20, command = lambda: button_click(0))
button_add = Button(win, text='+', padx=40,pady=20,command = lambda: button_click('+'))
button_min = Button(win, text='-', padx=40,pady=20,command = lambda: button_click('-'))
button_mul = Button(win, text='x', padx=40,pady=20,command = lambda: button_click('*'))
button_div = Button(win, text='/', padx=40,pady=20,command = lambda: button_click('/'))
button_div1 = Button(win, text='//', padx=40,pady=20,command = lambda: button_click('//'))
button_equ = Button(win, text='=', padx=40,pady=20,command = lambda: Button_Equal())
button_del = Button(win, text='C', padx=40,pady=20, command = lambda: Button_Clear())
button_dot=Button(win,text='.', padx=40,pady=20, command = lambda: button_click('.'))
button_factors=Button(win,text='fact', padx=40,pady=20, command = lambda: factors())
button_factorial=Button(win,text='factorial', padx=40,pady=20, command = lambda: factorial(str(eval(expression))))
button_brack1=Button(win,text='(', padx=40,pady=20, command = lambda: button_click('('))
button_brack2=Button(win,text=')', padx=40,pady=20, command = lambda: button_click(')'))
button_Abs1=Button(win,text='Abs', padx=40,pady=20, command = lambda: Abs())
button_Pn=Button(win,text='P/C', padx=40,pady=20, command = lambda: pn())
button_Sqt=Button(win,text='√', padx=40,pady=20, command = lambda: Sqrt())
button_Sqr=Button(win,text='sqr', padx=40,pady=20, command = lambda: sqr())

#The following code displays the buttons created
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_add.grid(row=1, column=3)
button_min.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_equ.grid(row=4, column=2)
button_del.grid(row=4,column=0)
button_factors.grid(row=5,column=0)
button_factorial.grid(row=5,column=1)
button_brack1.grid(row=5,column=2)
button_brack2.grid(row=5,column=3)
button_dot.grid(row=6,column=0)
button_div1.grid(row=6,column=1)
button_Abs1.grid(row=6,column=2)
button_Pn.grid(row=6,column=3)
button_Sqt.grid(row=7,column=0)
button_Sqr.grid(row=7,column=1)
win.mainloop()
# I am making a change to calculator file and trying to push it to my local repo
