from tkinter import *
from tkinter import ttk

def open_main_window():
    main_window = Tk()
    main_window.title("Personal Data")
    main_window.geometry('640x440')
    
    frame = Frame(main_window)
    frame.pack()

# User info

#Info Frame
    userInfoFrame = LabelFrame(frame, text = "User Information")
    userInfoFrame.grid(row=0, column=0,padx = 20, pady = 20)

#labels
    firstNameLabel = Label(userInfoFrame, text="First Name")
    firstNameLabel.grid(row=0, column=0)

    lastNameLabel = Label(userInfoFrame, text="Last Name")
    lastNameLabel.grid(row=0, column=1)

    titleLabel = Label(userInfoFrame,text = "Title")
    titleCombobox = ttk.Combobox(userInfoFrame, value=[" ","Mr.","Ms.","Dr."])
    titleLabel.grid(row=0, column=2)
    

    ageLabel = Label(userInfoFrame, text="Age")
    ageSpinbox = Spinbox(userInfoFrame, from_=18 , to=110)
    ageLabel.grid(row=2, column=0)

    nationalityLabel = Label(userInfoFrame, text="Nationality")
    nationalityCombobox = ttk.Combobox(userInfoFrame, value=["Africa","Antarctica","Asia","Europe","North America","South America"])
    nationalityLabel.grid(row=2, column=1)


# entries
    firstNameEntry = Entry(userInfoFrame)
    firstNameEntry.grid(row=1, column=0)

    lastNameEntry = Entry(userInfoFrame)
    lastNameEntry.grid(row=1, column=1)
    
    titleCombobox.grid(row=1, column=2)

    ageSpinbox.grid(row=3,column=0)

    nationalityCombobox.grid(row=3, column=1)



    for widget in userInfoFrame.winfo_children():
        widget.grid_configure(padx=10,pady=5)

# secound frame
    secoundFrame = LabelFrame(frame)
    secoundFrame.grid(row=1, column=0, sticky="news",padx = 20, pady = 20)




















    main_window.mainloop()

    
open_main_window()


