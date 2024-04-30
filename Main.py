from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Login form")
window.geometry('340x440')
window.config(bg = "#3d3d29")
windologin = 'dawid'
password = '12345'

def correct_login():
    messagebox.showinfo(title = "Login", message = "Login went through correctly !")
def wrong_login():
    messagebox.showinfo(title = "Login", message= "Incorrect login or password !")


# Creating widgets
loginLabel = Label(window, text="Login",bg = "#3d3d29",fg = "white",font = ("Arial",30))

usernameLabel = Label(window, text="Username",bg = "#3d3d29",fg = "white",font = ("Arial",16))
usernameEntry = Entry(window,font = ("Arial",16))

passwordLabel = Label(window, text="Password",bg = "#3d3d29",fg = "white",font = ("Arial",16))
passwordEntry = Entry(window, show="*",font = ("Arial",16))

loginButton = Button(window, text="Login", command = wrong_login)

'''if usernameEntry == login and passwordEntry == password:
    Button(window, command=correct_login).grid()
else:
    Button(window, command=wrong_login)'''

# Placing widgets on the screen
loginLabel.grid(row=0, column=0, columnspan=2, sticky= "news")
usernameLabel.grid(row=1, column=0)  # You need to specify the row and column for each widget
usernameEntry.grid(row=1, column=1)
passwordLabel.grid(row=2, column=0)
passwordEntry.grid(row=2, column=1)
loginButton.grid(row=3, column=0, columnspan=2)

window.mainloop()
