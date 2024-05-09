from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from EnterData import enter_data

def open_main_window():


    mainWindow = Tk()
    mainWindow.title("Personal Data")

    frame = Frame(mainWindow)
    frame.pack()

    # User info

    # Info Frame
    userInfoFrame = LabelFrame(frame, text="User Information")
    userInfoFrame.grid(row=0, column=0, padx=20, pady=10)

    # labels
    firstNameLabel = Label(userInfoFrame, text="First Name")
    firstNameLabel.grid(row=0, column=0)

    lastNameLabel = Label(userInfoFrame, text="Last Name")
    lastNameLabel.grid(row=0, column=1)

    titleLabel = Label(userInfoFrame, text="Title")
    titleCombobox = ttk.Combobox(userInfoFrame, value=[" ", "Mr.", "Ms.", "Dr."])
    titleLabel.grid(row=0, column=2)

    ageLabel = Label(userInfoFrame, text="Age")
    ageSpinbox = Spinbox(userInfoFrame, from_=18, to=110)
    ageLabel.grid(row=2, column=0)

    nationalityLabel = Label(userInfoFrame, text="Nationality")
    nationalityCombobox = ttk.Combobox(userInfoFrame, value=["Africa", "Antarctica", "Asia", "Europe", "North America", "South America"])
    nationalityLabel.grid(row=2, column=1)

    # entries
    firstNameEntry = Entry(userInfoFrame)
    firstNameEntry.grid(row=1, column=0)

    lastNameEntry = Entry(userInfoFrame)
    lastNameEntry.grid(row=1, column=1)

    titleCombobox.grid(row=1, column=2)

    ageSpinbox.grid(row=3, column=0)

    nationalityCombobox.grid(row=3, column=1)

    for widget in userInfoFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # secound frame
    secoundFrame = LabelFrame(frame)
    secoundFrame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

    registeredLabel = Label(secoundFrame, text='Registration Status')

    # possibility to change the string after click on check button
    regStatusVar = StringVar(value="Not Registered")
    registeredCheck = Checkbutton(secoundFrame, text='Currently Registered', 
                                            variable=regStatusVar, onvalue="Registered" , offvalue="Not registered")
    
    registeredLabel.grid(row=0, column=0)
    registeredCheck.grid(row=1, column=0)

    numCoursesLabel = Label(secoundFrame, text="# Completed Courses")
    numCoursesSpinbox = Spinbox(secoundFrame, from_=0, to='infinity')
    numCoursesLabel.grid(row=0, column=1)
    numCoursesSpinbox.grid(row=1, column=1)

    numSemesterLabel = Label(secoundFrame, text="# Semesters")
    numSemestersSpinbox = Spinbox(secoundFrame, from_=0, to='infinity')
    numSemesterLabel.grid(row=0, column=2)
    numSemestersSpinbox.grid(row=1, column=2)

    for widget in secoundFrame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    # third frame
    thirdTermsFrame = LabelFrame(frame, text="Terms & Conditions")
    thirdTermsFrame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

    acceptVar = StringVar(value="Not Accepted")
    acceptConditionsLabel = Checkbutton(thirdTermsFrame, text="I accept the term and conditions",
                                        variable=acceptVar, onvalue="Accepted",offvalue="Not Accepted")
    acceptConditionsLabel.grid(row=0, column=0)

    # accept button

    acceptButton = Button(frame, text="Enter data", command=lambda: enter_data(firstNameEntry, lastNameEntry, titleCombobox, ageSpinbox, nationalityCombobox, numCoursesSpinbox, numSemestersSpinbox, regStatusVar,acceptVar))
    acceptButton.grid(row=3, column=0, sticky="news", padx=20, pady=20)

    mainWindow.mainloop()