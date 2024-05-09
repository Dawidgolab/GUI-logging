from tkinter import *
from tkinter import messagebox
from PersonalDataForm import open_main_window



# Main functions
window = Tk()
window.title("Login form")
window.geometry('640x440')
window.config(bg = "#3d3d29")


frame = Frame(bg="#3d3d29")
frame.pack()


def login_details(event=None):
    username = "dawid"
    password = "12345"
    if usernameEntry.get() == username and passwordEntry.get() == password:
        print("Successfully logged in!")
        window.destroy()  # Close the login window
        open_main_window()      # Open the main window
    else:
            messagebox.showerror(title="Error", message = "Invalid login!")




# Creating widgets
loginLabel = Label(
    frame, text="Login",bg = "#3d3d29",fg = "white",font = ("Arial",30))

usernameLabel = Label(
    frame, text="Username",bg = "#3d3d29",fg = "white",font = ("Arial",16))
usernameEntry = Entry(frame,font = ("Arial",16))

passwordLabel = Label(
    frame, text="Password",bg = "#3d3d29",fg = "white",font = ("Arial",16))
passwordEntry = Entry(frame, show="*",font = ("Arial",16))

loginButton = Button(
    frame, text="Login", command= login_details)




# Placing widgets on the screen
loginLabel.grid(row=0, column=0, columnspan=2, sticky= "news", pady=40)
usernameLabel.grid(row=1, column=0)  # You need to specify the row and column for each widget
usernameEntry.grid(row=1, column=1, pady=20)
passwordLabel.grid(row=2, column=0)
passwordEntry.grid(row=2, column=1,  pady=20)
loginButton.grid(row=3, column=0, columnspan=2, pady= 30)

window.bind("<Return>", login_details)


window.mainloop()
