import tkinter as tk

root = tk.Tk()
root.title('GUI Shiv')
root.geometry('150x300')

'''BUTTONS - you know it'''
btn1 = tk.Button(root , text = "Click Me")
btn2 = tk.Button(root , text = "Click Me not")
# arrange the widgets in  grid fashion by specifying the row and column
btn1.grid(row = 0, column = 1)
btn2.grid(row = 0, column = 3)

root.mainloop()
