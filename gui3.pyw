import tkinter as tk

'''TOP-LEVEL : another top level window'''

def create_window(parent = None):
    window = tk.Toplevel(parent)
    window.title('Brand New Window')
    window.geometry('450x250')
    tk.Button(window, text='Create new window', \
              command = lambda: create_window(window)).pack()
    tk.Button(window, text='Destroy this window', \
              command = lambda: destroy_window(window)).pack()

def destroy_window(window):
    window.destroy()


'''ROOT WINDOW'''    
root = tk.Tk()
root.title('GUI Shiv')
root.geometry('250x450')

'''BUTTON'''
tk.Button(root, text='Feel the magic', \
          command = lambda: create_window()).pack()
tk.Button(root, text='Bye Bye', \
          command = lambda: destroy_window(root)).pack()
          

root.mainloop()
