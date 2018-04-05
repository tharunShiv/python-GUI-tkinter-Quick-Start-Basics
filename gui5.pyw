import tkinter as tk

root = tk.Tk()
root.title('GUI Shiv')
root.geometry('350x650')

'''EVENT BINDING : associated method is called when an event happens'''
'''Implementing using the lambda functions'''

data = tk.StringVar()  # datatype and initialization
data.set('0')

up = tk.Button(root, text = "+", \
               command = lambda : data.set(str(int(data.get())+1))).grid(row=0, column=0)

point_label = tk.Label(root, \
                       textvariable = data).grid(row = 0, column = 1)

down = tk.Button(root, text="-", \
                 command = lambda : data.set(str(int(data.get())-1))).grid(row=0, column=2)


root.mainloop()
