import tkinter as tk

root = tk.Tk()  # creating a root window

'''TITLE of the window and the dimensions'''
root.title("GUI Shiv")  
root.geometry("350x650")


'''LABEL - used to display short pieces of text, which cannot be directly mutated
 by the user'''
label = tk.Label(root, text='Mahadev!')
label.pack() # used to arrange the widget inside the parent(in this case-root) and
# resize if necessary

'''FRAMES - they are widgets that contain other widgets
Not visible on the screen but are used to organize other widget'''
f = tk.Frame(root) # the parent of the frame is the root
custom_label = tk.Label(f, text='Sabapathi') #the parent of this label is f, not root
custom_label_0 = tk.Label(f, text='Kabali') 
# don't forget to pack it
custom_label.pack()
custom_label_0.pack()
f.pack()

root.mainloop() # start the main loop.
