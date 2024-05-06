from tkinter import *

def open_main_window():
    main_window = Tk()
    main_window.title("Personal Data")
    main_window.geometry('640x440')
    
    frame = Frame(main_window)
    frame.pack()

    # User info
    userInfoFrame = LabelFrame(frame, text = "User Information")
    userInfoFrame.grid(row=0, column=0,padx = 20, pady = 20)

    firstNameLabel = Label(userInfoFrame, text="First Name")
    firstNameLabel.grid(row=0, column=0)
    lastNameLabel = Label(userInfoFrame, text="Last Name")
    lastNameLabel.grid(row=0, column=1)

    firstNameEntry = Entry(userInfoFrame)
    lastNameEntry = Entry(userInfoFrame)
    firstNameEntry.grid(row=1, column=0)
    lastNameEntry.grid(row=1, column=1)

    main_window.mainloop()

























    
open_main_window()


