import tkinter as tk
win = tk.Tk()
#win.geometry("800x600")

red = 0
black = 0
def redvote():
  global red
  red = red+1
  label1text.set("Red Team:{} votes".format(red))
def blvote():
  global black
  black = black+1
  label2text.set("Black Team:{} votes".format(black))
def stopvote():
  msg = tk.StringVar()
  frame1.forget()
  frame2.forget()
  label3.forget()
  if red>black:
    Iblmsg = tk.Label(win, fg="red", textvariable=msg, font=("Times", 25))
    msg.set("Total votes(RED:BLACK) = ({} : {})\nRED team WINS".format(red,black))
  elif red<black:
    Iblmsg = tk.Label(win, fg="black", textvariable=msg, font=("Times", 25))
    msg.set("Total votes(RED:BLACK) = ({} : {})\nBLACK team WINS".format(red,black))
  else:
    Iblmsg = tk.Label(win, fg="blue", textvariable=msg, font=("Times", 25))
    msg.set("Total votes(RED:BLACK) = ({} : {})\nTwo teams tied".format(red,black))
  Iblmsg.pack(padx=20, pady=5)
  label4=tk.Label(win, text="", font=("Times", 20), width=20)
  label4.pack()
  
label1text = tk.StringVar()
label2text = tk.StringVar()

label3=tk.Label(win, text="", font=("Times", 20), width=20)
label3.pack()

frame1 = tk.Frame(win)
label1=tk.Label(frame1, fg="red", textvariable=label1text, font=("Times", 20), width=23)
button1 = tk.Button(frame1, fg="red", text="VOTE", command = redvote, font=("Times",20), width=10)
label2=tk.Label(frame1, textvariable=label2text, font=("Times", 20), width=23)
button2 = tk.Button(frame1, text="VOTE", command = blvote, font=("Times",20), width=10)
label1text.set("Please vote RED team!")
label2text.set("Please vote BLACK team!")

label1.grid(row=0, column=0, padx=5, pady=5)
button1.grid(row=1, column=0, padx=5, pady=5)
label2.grid(row=0, column=1, padx=5, pady=5)
button2.grid(row=1, column=1, padx=5, pady=5)
frame1.pack()

frame2 = tk.Frame(win)
button3 = tk.Button(frame2, fg="blue", text="Stop voting!", command = stopvote, font=("Times",20), width=10)
button3.grid(row=2, column=0, padx=5, pady=5)
frame2.pack()

label3=tk.Label(win, text="", font=("Times", 20), width=20)
label3.pack()

win.mainloop()
