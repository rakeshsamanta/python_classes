import tkinter as tk
window1 =tk.Tk()
canvas1 = tk.Canvas(window1,height="750",width="550")
canvas1.pack()
def newwindow():
    window2 = tk.Tk()
    canvas2 = tk.Canvas(window2, width=200, height=200)
    canvas2.pack()
    label2 = tk.Label(window2, text="kittiyot", fg='red', font=('helvetica','10','bold'))
    canvas2.create_window(100,100,window=label2)

label1 = tk.Label(window1, text="what is your name", fg='green', font=('calibra',12,'bold'))
canvas1.create_window(100,100,window=label1)
button1 = tk.Button(text="click here for answer", command=newwindow, bg='pink', fg='yellow')
canvas1.create_window(350,200, window=button1)
window1.mainloop()
