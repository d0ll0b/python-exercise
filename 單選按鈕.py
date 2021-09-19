def choose():
  msg.set("Your Favorite Sport is " + choice.get())

import tkinter as tk

win = tk.Tk()
win.geometry("800x400")

choice = tk.StringVar()
msg = tk.StringVar()

label = tk.Label(win, fg="blue", text="Choose Your Favorite Sport", font=("Times", 25))
label.pack()

ball = ["Football", "Basketball", "Baseball"]

for i in range(len(ball)):
  item = tk.Radiobutton(win, text=ball[i], value=ball[i], variable=choice, command=choose, font=("Times", 20))
  item.pack()

  if i == 0:
    item.select()
    choose()
 
Iblmsg = tk.Label(win, fg="red", textvariable=msg, font=("Times", 25))
Iblmsg.pack()

win.mainloop()