from tkinter import *


def calculator():
    root = Tk()
    root.title("CALCULATOR")

    e = Entry(root, width=50, borderwidth=5)
    e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    def button_add1():
        e.insert(0, 1)

    def button_add2():
        e.insert(0, 2)

    def button_add3():
        e.insert(0, 3)

    def button_add4():
        e.insert(0, 4)

    def button_add5():
        e.insert(0, 5)

    def button_add6():
        e.insert(0, 6)

    def button_add7():
        e.insert(0, 7)

    def button_add8():
        e.insert(0, 8)

    def button_add9():
        e.insert(0, 9)

    def button_add0():
        e.insert(0, 0)

    def button_add(number):
        e.insert(0, number)

    def clear():
        e.delete(0, END)

    def button_click():
        first_number = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        e.delete(0, END)

    def button_equal():

        second_number = e.get()
        e.delete(0, END)
        if math == "addition":
            e.insert(0, f_num + int(second_number))

        if math == "subtraction":
            e.insert(0, f_num - int(second_number))

        if math == "multiplication":
            e.insert(0, f_num * int(second_number))

        if math == "division":
            e.insert(0, f_num / int(second_number))

    def button_sub():
        first_number = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        e.delete(0, END)

    def button_mul():
        first_number = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        e.delete(0, END)

    def button_div():
        first_number = e.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        e.delete(0, END)

    button_1 = Button(root, text="1", padx=75, pady=20, command=button_add1)
    button_2 = Button(root, text="2", padx=75, pady=20, command=button_add2)
    button_3 = Button(root, text="3", padx=75, pady=20, command=button_add3)
    button_4 = Button(root, text="4", padx=75, pady=20, command=button_add4)
    button_5 = Button(root, text="5", padx=75, pady=20, command=button_add5)
    button_6 = Button(root, text="6", padx=75, pady=20, command=button_add6)
    button_7 = Button(root, text="7", padx=75, pady=20, command=button_add7)
    button_8 = Button(root, text="8", padx=75, pady=20, command=button_add8)
    button_9 = Button(root, text="9", padx=75, pady=20, command=button_add9)
    button_0 = Button(root, text="0", padx=75, pady=20, command=button_add0)
    button_add = Button(root, text="+", padx=75, pady=20, command=button_click)
    button_equal = Button(root, text="=", padx=158, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=145, pady=20, command=clear)
    button_subtract = Button(root, text="-", padx=75, pady=20, command=button_sub)
    button_multiply = Button(root, text="*", padx=76, pady=20, command=button_mul)
    button_divide = Button(root, text="/", padx=75, pady=20, command=button_div)

    button_1.grid(row=3,column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

    root.mainloop()
