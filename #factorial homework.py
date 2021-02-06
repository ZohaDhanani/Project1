#factorial app
from tkinter import*
off=Tk()
off.title('factorial')
f=Entry(off,width=45,borderwidth=10)
f.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def button_click(num):
    current = str(f.get())
    f.delete(0,END)
    f.insert(0, current + str(num))
    global num1
    num1=int(f.get())
    return
def factorial(num):
    f.delete(0,END)
    if num==1:
        f.insert(0,num)
        return 
    else :
        fac=num*factorial(num-1)
        f.insert(0,fac)
        return
button_1 = Button(off, text="1", padx=40, pady=20, command = lambda: button_click(1))
button_2 = Button(off, text="2", padx=40, pady=20, command = lambda: button_click(2))
button_3 = Button(off, text="3", padx=40, pady=20, command = lambda: button_click(3))
button_4 = Button(off, text="4", padx=40, pady=20, command = lambda: button_click(4))
button_5 = Button(off, text='5', padx=40,pady=20, command = lambda: button_click(5))
button_6 = Button(off, text='6', padx=40,pady=20, command = lambda: button_click(6))
button_7 = Button(off, text='7', padx=40,pady=20, command = lambda: button_click(7))
button_8 = Button(off, text='8', padx=40,pady=20, command = lambda: button_click(8))
button_9 = Button(off, text='9', padx=40,pady=20, command = lambda: button_click(9))
button_0 = Button(off, text='0', padx=40,pady=20, command = lambda: button_click(0))
button_clear=Button(off,text='clear',padx=40,pady=20,command=lambda:f.delete(0,END))
button_factorial=Button(off,text='factorial',padx=40,pady=20,command=lambda:factorial(num1))

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=1)
button_clear.grid(row=4,column=0)
button_factorial.grid(row=4,column=2)
off.mainloop()
