
import tkinter as tk

'''PROGRAM NOT WORKING< FIXING SOON, ANY HELP is appreciated'''

root = tk.Tk()
root.title('GUI Shiv')
root.geometry('400x650')

'''MULTIPLE SCREENS AND NAVIGATING BETWEEN THEM'''
'''# The frames are stacked upon each other
     and the frame which is to be shown is on the top, hiding the
     rest of the frames below it #'''

main_frame = tk.Frame(root) # Create a main frame
tk.Label(main_frame, text='Main Frame').pack()

second_frame = tk.Frame(root) # Create a second frame
tk.Label(second_frame, text='Second Frame').pack()

'''Raise the main frame on button click'''
tk.Button(second_frame, text = "Go to main frame", \
          command = main_frame.tkraise).pack()

'''similarly'''
tk.Button(main_frame, text = "Go to second frame", \
          command = second_frame.tkraise).pack()

second_frame.grid(row=0, column=0, padx=150, pady=120, sticky = 'NSEW')
main_frame.grid(row=0, column=0, padx=150, pady=120, sticky = 'NSEW')

main_frame.lift()

root.mainloop()

