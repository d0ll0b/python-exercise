import tkinter as tk


def sub():
    global msg, name, date
    msg1 = tk.StringVar()
    msg.set("{}, Thanks for Your Information".format(name.get()))
    Iblmsg.pack()

    label1.forget()
    label2.forget()
    item1.forget()
    item2.forget()
    item3.forget()
    item4.forget()
    item5.forget()
    item6.forget()
    item7.forget()
    label3.forget()
    entry.forget()
    button.forget()

    label4 = tk.Label(win, fg="blue", text="\nYour Favorite Date:{}".format(
        choice1.get()), font=("Times", 25))
    label4.pack()
    Iblmsg1 = tk.Label(win, fg="green", textvariable=msg1, font=("Times", 25))
    str = "Your Favorite Meal:"
    a = 0
    for i in range(0, len(choice)):
        if(choice[i].get() == 1):
            if a == 0:
                str = str + " " + meal[i]
            else:
                str = str + ", " + meal[i]
            a = a+1

    msg1.set(str)
    Iblmsg1.pack()


win = tk.Tk()
win.geometry("800x600")

choice = [0, 0, 0, 0]
date = ["FRI", "SAT", "SUN"]
meal = ["Steak", "Burger", "Pizza", "BBQ"]
msg = tk.StringVar()
name = tk.StringVar()
choice1 = tk.StringVar()

label1 = tk.Label(
    win, fg="blue", text="Choose Your Favorite Date:", font=("Times", 25))
label1.pack()

item1 = tk.Radiobutton(
    win, fg="blue", text=date[0], value=date[0], variable=choice1, font=("Times", 20))
item1.pack()
item1.select()
item2 = tk.Radiobutton(
    win, fg="blue", text=date[1], value=date[1], variable=choice1, font=("Times", 20))
item2.pack()
item3 = tk.Radiobutton(
    win, fg="blue", text=date[2], value=date[2], variable=choice1, font=("Times", 20))
item3.pack()


label2 = tk.Label(
    win, fg="green", text="Choose Your Favorite Meal:", font=("Times", 25))
label2.pack()

choice[0] = tk.IntVar()
choice[1] = tk.IntVar()
choice[2] = tk.IntVar()
choice[3] = tk.IntVar()
item4 = tk.Checkbutton(
    win, fg="green", text=meal[0], variable=choice[0], font=("Times", 20))
item4.pack()
item5 = tk.Checkbutton(
    win, fg="green", text=meal[1], variable=choice[1], font=("Times", 20))
item5.pack()
item6 = tk.Checkbutton(
    win, fg="green", text=meal[2], variable=choice[2], font=("Times", 20))
item6.pack()
item7 = tk.Checkbutton(
    win, fg="green", text=meal[3], variable=choice[3], font=("Times", 20))
item7.pack()

label3 = tk.Label(win, text="Name:", font=("Times", 25))
label3.pack()

entry = tk.Entry(win, textvariable=name, font=("Times", 20))
entry.pack()

button = tk.Button(win, text="submit", command=sub, font=("Times", 20))
button.pack()

Iblmsg = tk.Label(win, fg="red", textvariable=msg, font=("Times", 25))
Iblmsg.pack()

win.mainloop()
