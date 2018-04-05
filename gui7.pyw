import tkinter as tk

root = tk.Tk()
root.title("GUI Shiv")
root.geometry("250x400")

'''MUTABLE VARIABLES- update the contents on certain events'''
label1 = tk.Label(root, text="This text will change")
label1.pack()

tk.Button(root, text="Click to change it", \
          command = lambda: label1.config(text = "Hurray! The text has changed")).pack()


root.mainloop()
