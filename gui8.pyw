import tkinter as tk

root = tk.Tk()
root.title("GUI Shiv")
root.geometry("250x400")

'''MUTABLE VARIABLES- update the contents on certain events'''
text_data = tk.StringVar()
text_data.set('This is the text that will change')

label1 = tk.Label(root, textvariable=text_data)
label1.pack()

tk.Button(root, text="Click to change it", \
          command = lambda: text_data.set("Hurray! the text has changed")).pack()


root.mainloop()
