import tkinter as tk

root = tk.Tk()
root.title('GUI Shiv')
root.geometry('350x650')

'''EVENT BINDING : associated method is called when an event happens'''

data = tk.StringVar()  # datatype and initialization
data.set('0')

def up_count():
    
    num = int(data.get())  # get the current value and cast it into a int
    data.set(str(num + 1)) # set the incremented value and cast it to string


def down_count():
    
    num = int(data.get())
    data.set(str(num - 1))


up = tk.Button(root, text = "+", \
               command = up_count).grid(row=0, column=0)

point_label = tk.Label(root, \
                       textvariable = data).grid(row = 0, column = 1)

down = tk.Button(root, text="-", \
                 command = down_count).grid(row=0, column=2)


root.mainloop()
