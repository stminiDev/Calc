
import tkinter.font
from tkinter import messagebox as msg
from tkinter import *

root = tkinter.Tk()
root.title("Calculator")

# set size & Font
root.geometry("327x408")
root.resizable(False, False)
font = tkinter.font.Font(family="Helvetica", size=20, weight="bold")
btn_font = tkinter.font.Font(family="Helvetica",size=9,weight="bold")

record = ""                           #stores calculation histories
init_strnumber = ""                   #stores users standard input as string
input_text  = StringVar()
record_text = StringVar()             # effects " AttributeError: 'str' object has no attribute 'get'  "
                                      # without using StringVar()


def btn_click(item):
    global init_strnumber
    if not init_strnumber == '0':    # exceptions
        init_strnumber += str(item)
        input_text.set(init_strnumber)

    if len(init_strnumber) >= 3:
        record = f"{init_strnumber}={str(eval(init_strnumber))}"
        record_text.set(record)

    elif init_strnumber =='0' and not item == '0':
        init_strnumber = str(item)
        input_text.set(init_strnumber)



def btn_clear():
    global record
    global init_strnumber
    record = ""
    record = init_strnumber = ""
    record_text.set("")
    input_text.set("")

def btn_equal():
    global init_strnumber
    input_text.set(str(eval(init_strnumber)))
    init_strnumber = str(eval(init_strnumber))

def btn_stdin(item):
    global init_strnumber
    item = repr(item.char).strip("'")

    if   item == '\\r'  :    btn_equal()
    elif item == '\\x1b':    btn_clear()
    elif item == '\\x08':
        init_strnumber = init_strnumber[0:len(init_strnumber)-1]
        input_text.set(init_strnumber)
        record_text.set(init_strnumber)

    else:btn_click(item)




root.bind('<Key>',btn_stdin)

input_frame = tkinter.Frame(root,width=30, height=40, bd=4,highlightbackground="#FFACAC",bg="#FFACAC",highlightthickness=3)
input_frame.pack(side="top")

hist_frame = tkinter.Frame(root,width=30,height=40,bd=1,highlightbackground="#FFACAC",bg="#FFACAC",highlightthickness=1)
hist_frame.pack(side="top")

input_field = tkinter.Entry(input_frame, justify='right', font=font, state="normal",textvariable=input_text, width=21, bg="#E8E8E8", bd=3)
input_field.pack(ipady=12)

hist_field = tkinter.Entry(hist_frame,textvariable = record_text,justify="right",state="disabled",width=29,bd=6,font=tkinter.font.Font(size=15))
hist_field.pack(ipady=2,pady=1,padx=4)

btns_frame = tkinter.Frame(root, width=30, height=40, background="#FFACAC",bd=2)
btns_frame.pack()



btn_0 = Button(btns_frame, text="0", foreground="black", width=22, height=3, bd=1, bg="#fff", cursor="hand2",font=tkinter.font.Font(weight="bold",size=9),command=lambda: btn_click(0)).grid(row=5, column=0, columnspan=2, padx=0, pady=2)
btn_1 = Button(btns_frame, text="1", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(1)).grid(row=4, column=0, padx=1, pady=1)
btn_2 = Button(btns_frame, text="2", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(2)).grid(row=4, column=1, padx=1, pady=1)
btn_3 = Button(btns_frame, text="3", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(3)).grid(row=4, column=2, padx=1, pady=1)
btn_4 = Button(btns_frame, text="4", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(4)).grid(row=3, column=0, padx=1, pady=1)
btn_5 = Button(btns_frame, text="5", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(5)).grid(row=3, column=1, padx=1, pady=1)
btn_6 = Button(btns_frame, text="6", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(6)).grid(row=3, column=2, padx=1, pady=1)
btn_7 = Button(btns_frame, text="7", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(7)).grid(row=2, column=0, padx=1, pady=1)
btn_8 = Button(btns_frame, text="8", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(8)).grid(row=2, column=1, padx=1, pady=1)
btn_9 = Button(btns_frame, text="9", foreground="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(9)).grid(row=2, column=2, padx=1, pady=1)
btn_dot = Button(btns_frame, text=".", fg="black", width=10, height=3, bd=1, bg="#fff", cursor="hand2",font=btn_font,command=lambda: btn_click(".")).grid(row=5, column=2, padx=1, pady=1)



btn_clr = Button(btns_frame, text="CLEAR", fg="black", width=33, height=3, bd=1, bg="#FFD6D6", cursor="hand2",command=lambda: btn_clear()).grid(row=1, columnspan=3,pady=1,padx=2)
btn_div = Button(btns_frame, text="/", fg="black", width=10, height=3, bd=1, bg="#E8E8E8", cursor="hand2", command=lambda: btn_click("/")).grid(row=1, column=3,padx=1, pady=1)
btn_mul = Button(btns_frame, text="x", fg="black", width=10, height=3, bd=1, bg="#E8E8E8", cursor="hand2",command=lambda: btn_click("*")).grid(row=2, column=3, padx=1, pady=1)
btn_sub = Button(btns_frame, text="-", fg="black", width=10, height=3, bd=1, bg="#E8E8E8", cursor="hand2",command=lambda: btn_click("-")).grid(row=3, column=3, padx=1, pady=1)
btn_add = Button(btns_frame, text="+", fg="black", width=10, height=3, bd=1, bg="#E8E8E8", cursor="hand2",command=lambda: btn_click("+")).grid(row=4, column=3, padx=1, pady=1)
btn_eql = Button(btns_frame, text="=", fg="black", width=10, height=3, bd=1, bg="#FFD6D6", cursor="hand2",command=lambda: btn_equal()).grid(row=5, column=3, padx=1, pady=1)


root.mainloop()
