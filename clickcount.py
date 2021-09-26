def clickme1():
  global count1
  count1 += 1
  labeltext.set("Clicked "
     + str(count1) + " times")
  if(btntext.get() == "ON"):
    btntext.set("OFF")
  else:
    btntext.set("ON")

def clickme2():
  global count2
  count2 += 1
  labeltext2.set("Clicked "
     + str(count2) + " times")
  if(btntext2.get() == "ON"):
    btntext2.set("OFF")
  else:
    btntext2.set("ON")

import tkinter as tk

win = tk.Tk()
win.geometry("800x200")

labeltext = tk.StringVar()
btntext = tk.StringVar()
labeltext2 = tk.StringVar()
btntext2 = tk.StringVar()
count1 = 0
count2 = 0

label1 = tk.Label(win, fg="red", textvariable=labeltext, font=("times", 25))
labeltext.set("Welcome to Tkinter")
label1.pack()

button1 = tk.Button(win, textvariable = btntext, command = clickme1, font=("Times", 20))
btntext.set("ON")
button1.pack()

label2 = tk.Label(win, fg="blue", textvariable=labeltext2, font=("times", 25))
labeltext2.set("Welcome to Tkinter")
label2.pack()

button2 = tk.Button(win, textvariable = btntext2, command = clickme2, font=("Times", 20))
btntext2.set("ON")
button2.pack()

win.mainloop()
      