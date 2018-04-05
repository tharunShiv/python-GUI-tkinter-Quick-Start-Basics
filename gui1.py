import tkinter

root = tkinter.Tk()  # creating a root window

'''TITLE of the window and the dimensions'''
root.title("GUI Shiv")  
root.geometry("350x650")


'''LABEL - used to display short pieces of text, which cannot be directly mutated
 by the user'''
label = tkinter.Label(root, text='Mahadev!')
label.pack() # used to arrange the widget inside the parent(in this case-root) and
# resize if necessary

'''FRAMES - they are widgets that contain other widgets
Not visible on the screen but are used to organize other widget'''



root.mainloop() # start the main loop.
