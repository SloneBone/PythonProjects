#   Python Version: 3.9
#   
#   
#   Author:          Drew Slone
#
#
#
#
#   Purpose:        Create a simple Web Generating script that Utilizes Tkinter and webbrowser modules 
#                   which will allow users to change the Body of the corresponding html file
#                   and load new web page in browser via input


#importing native modules
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import webbrowser as web
import os

#initializing Parent Class for tkinter 
class Web_Page_Gen(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Defining the parameters of Frame 
        self.master = master
        self.master.minsize(800, 500)
        self.master.maxsize(1000,600)
        self.master.title("Web Page Generator")
        self.master.configure(bg= "#7CACAB")
        self.master.protocol("WM_DELETE_WINDOW")
        arg = self.master
        #Calling a Fx to control buttons, txt box, and label
        Display_Layout(self)
        
def Display_Layout(self):
    #Label for text box
    self.lbl_Input = tk.Label(self.master, text = "Enter new Website text here: ", bg= "gold")
    self.lbl_Input.grid(row=0, column=0, padx=(15,15), pady=(15,15), sticky=N+W)
    #User input text box
    self.Input = tk.Entry(self.master,text='')
    self.Input.grid(row=1,column=0, ipadx=100, ipady=40, padx=(30,40),pady=(0,25),sticky=N+S+E+W)
    #submit button
    self.Submit = tk.Button(self.master, width=25, height=3, text='Submit',bg="green", command=lambda:User_Input(self))
    self.Submit.grid(padx=(15,15), pady=(15,15), sticky=S+W)
    #Adding delete button
    self.Delete = tk.Button(self.master, width= 25, height=3, text='Delete', bg='red', command=lambda:Delete_Text(self))
    self.Delete.grid(padx=(15,15), pady=(15,15), sticky=S+E)




#Setting up a function that creates the displayable html file using webbrowser that we can call with Tkinter button
def Create(self):
    url = "web_page_gen.html"
    web.open_new(url)
#Creating a function that takes user input and passes it into Create() function
def User_Input(self):
    Gen = open("web_page_gen.html", "w")
    User_Input = self.Input.get()

    if User_Input != "":
        Gen.write("\n<html>\n\t<body>\n\t\t<h1>{}\n\t\t</h1>\n\t</body>\n</html>".format(User_Input))
        Gen.close()
        Create(self)
    else:
        tk.messagebox.showerror("Error", "You need to enter at least one character to Submit!")

#Adding a delete option for easy use
def Delete_Text(self):
    self.Input.delete(0,END)





if __name__ == "__main__":
    root = tk.Tk()
    App = Web_Page_Gen(root)
    root.mainloop()
    
    
