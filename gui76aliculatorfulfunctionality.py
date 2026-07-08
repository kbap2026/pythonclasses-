# in this tutorial we will learn about creating a claiculator using tikenter

from tkinter import *

mw = Tk()
mw.title("calculator")


def clear():
    db.delete(0, END)


def btn_clk(num):
    cur_num = db.get()  # logic
    clear()  # clears display
    f_num = cur_num + num  # concanate
    db.insert(0, f_num)


first_num = 0  # global variable


def calc(math_type):  # global value ni user enter chesindhi first number ki tiskuntundhi
    global first_num, math
    math = math_type
    first_num = db.get()  # display lo unna number ni first number lo padestunhi
    clear()


def equal():
    result = ""
    second_num = db.get()
    clear()
    if math == "add":
        result = int(first_num) + int(second_num)
    elif math == "sub":
        result = int(first_num) - int(second_num)
    elif math == "mul":
        result = int(first_num) * int(second_num)
    elif math == "div":
        result = int(first_num) / int(second_num)
        result = round(result,3)
    db.insert(0, str(result))


# creating widgets
db = Entry(mw, width=14, font=("Arial", 28), justify=RIGHT)
# taking grid system

# buttons create chestunam
btn_0 = Button(mw, text="0", padx=36, pady=10, font=("Arial", 14),
               command=lambda: btn_clk("0"))  # caliculator button kolatalu mesurments
btn_1 = Button(mw, text="1", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("1"))
btn_2 = Button(mw, text="2", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("2"))
btn_3 = Button(mw, text="3", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("3"))
btn_4 = Button(mw, text="4", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("4"))
btn_5 = Button(mw, text="5", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("5"))
btn_6 = Button(mw, text="6", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("6"))
btn_7 = Button(mw, text="7", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("7"))
btn_8 = Button(mw, text="8", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("8"))
btn_9 = Button(mw, text="9", padx=36, pady=10, font=("Arial", 14), command=lambda: btn_clk("9"))

btn_clear = Button(mw, text="clear", padx=74, pady=10, font=("Arial", 14), command=clear)
btn_div = Button(mw, text="/", padx=38, pady=10, font=("Arial", 14), command=lambda: calc("div"))
btn_mul = Button(mw, text="*", padx=38, pady=10, font=("Arial", 14), command=lambda: calc("mul"))
btn_sub = Button(mw, text="-", padx=38, pady=10, font=("Arial", 14), command=lambda: calc("sub"))
btn_add = Button(mw, text="+", padx=36, pady=10, font=("Arial", 14), command=lambda: calc("add"))
btn_equal = Button(mw, text="=", padx=36, pady=40, font=("Arial", 14), command=equal)
# showing widgets


# displaying buttons as per caliculator  model
btn_equal.grid(row=5, column=2, rowspan=2, padx=2, pady=2)
btn_add.grid(row=6, column=1, padx=2, pady=2)
btn_sub.grid(row=6, column=0, padx=2, pady=2)
btn_mul.grid(row=5, column=1, padx=2, pady=2)
btn_div.grid(row=5, column=0, padx=2, pady=2)

btn_clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)
btn_0.grid(row=4, column=0, padx=2, pady=2)

btn_1.grid(row=3, column=0, padx=2, pady=2)
btn_2.grid(row=3, column=1, padx=2, pady=2)
btn_3.grid(row=3, column=2, padx=2, pady=2)

btn_4.grid(row=2, column=0, padx=2, pady=2)
btn_5.grid(row=2, column=1, padx=2, pady=2)
btn_6.grid(row=2, column=2, padx=2, pady=2)

btn_7.grid(row=1, column=0, padx=2, pady=2)
btn_8.grid(row=1, column=1, padx=2, pady=2)
btn_9.grid(row=1, column=2, padx=2, pady=2)

db.grid(row=0, column=0, columnspan=3, padx=10,
        pady=10)  # display box#cloumn span 3 iste buttons equalent ga share avtubndhi

mw.mainloop()
