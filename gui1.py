import tkinter

root = tkinter.Tk()  # creating a root window

'''title of the window and the dimensions'''
root.title("GUI Shiv")  
root.geometry("400x300")


'''label - used to display short pieces of text, which cannot be directly mutated
 by the user'''

label = tkinter.Label(root, text='Mahadev!')
label.pack() # used to arrange the widget inside the parent(in this case-root) and
# resize if necessary

root.mainloop() # start the main loop.
