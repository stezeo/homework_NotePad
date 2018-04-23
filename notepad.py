# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:36:46 2018

@author: Kasutaja
"""


import sys
from tkinter import *
import tkinter.filedialog
import tkinter.messagebox as msg

#import ctypes  # An included library with Python install.


class TextEditor:
 
    # Quits the TkInter app when called
    @staticmethod
    def quit_app(event=None):
        root.quit()
        root.destroy()
        exit()
        
        
        
        
    def help_file (self, event=None):
        p = sys.version
        text_version ="Author: Stanley Ezeoke\n\n Python version: " + p
        help_display= msg.showinfo("About Python", text_version)
        return help_display
		
		
	

    def open_file(self, event=None):
 
        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                                                      initialdir='C:\\Users\\Kasutaja\\Documents\\python_class_project')
 
        if txt_file:
 
            self.text_area.delete("1.0", 'end-1c')
 
            # Open file and put text in the text widget
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())
 
                # Update the text widget
                root.update_idletasks()
 
    def save_file(self, event=None):
 
        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            # Get text in the text widget and delete the last newline
            data = self.text_area.get('1.0', 'end-1c')
 
            # Write the text and close
            file.write(data)
            file.close()
 
    def __init__(self, root):
 
        self.text_to_write = ""
 
        # Define title for the app
        root.title("Text Editor")
 
        # Defines the width and height of the window
        root.geometry("600x550")
 
        frame = tkinter.Frame(root, width=600, height=550)
 
        # Create the scrollbar
        scrollbar = tkinter.Scrollbar(frame)
 
        # yscrollcommand connects the scroll bar to the text
        # area
        self.text_area = tkinter.Text(frame, width=600, height=550,yscrollcommand=scrollbar.set,padx=10, pady=10)
 
        # Call yview when the scrollbar is moved
        scrollbar.config(command=self.text_area.yview)
 
        # Put scroll bar on the right and fill in the Y direction
        scrollbar.pack(side="right", fill="y")
 
        # Pack on the left and fill available space
        self.text_area.pack(side="left", fill="both", expand=True)
        frame.pack()
 
        # Create the menu object
        the_menu = tkinter.Menu(root)
 
        # Create a pull down menu that can't be removed
        file_menu = tkinter.Menu(the_menu, tearoff=0)
 
        # Add items to the menu that show when clicked
        # compound allows you to add an image
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
 
        # Add a horizontal bar to group similar commands
        file_menu.add_separator()
 
        # Call for the function to execute when clicked
        file_menu.add_command(label="Close", command=self.quit_app)
 
        # Add the pull down menu to the menu bar
        the_menu.add_cascade(label="File", menu=file_menu)
       
        
        help_menu = tkinter.Menu(the_menu, tearoff=0)
        help_menu.add_command(label="About", command=self.help_file)
        the_menu.add_cascade(label="Help", menu=help_menu)


 
        # Display the menu bar
        root.config(menu=the_menu)
 
root = tkinter.Tk()
 
text_editor = TextEditor(root)
 
root.mainloop()

print(sys.version)
