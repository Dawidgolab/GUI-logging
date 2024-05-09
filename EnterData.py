from tkinter import *
from tkinter import messagebox

def enter_data(firstNameEntry, lastNameEntry, titleCombobox, ageSpinbox, nationalityCombobox, numCoursesSpinbox, numSemestersSpinbox,regStatusVar,acceptVar):

        #Accept terms
        accepted = acceptVar.get()
        
        if accepted == "Accepted":
                # User info
                firstName = firstNameEntry.get()
                lastName = lastNameEntry.get()

                if firstName and lastName:
                        title = titleCombobox.get()
                        age = ageSpinbox.get()
                        nationatily = nationalityCombobox.get()
                                
                                
                        #Course info
                        registrationStatus = regStatusVar.get()
                        numCourses = numCoursesSpinbox.get()
                        numSemesters = numSemestersSpinbox.get()


                        # show in messagebox
                        messagebox.showinfo(title = "Your saved data", message = f"First name: {firstName}\nLast Name: {lastName}\nTitle: {title}\nAge: {age}\nNationality: {nationatily}\nCourses: {numCourses}\nSemesters: {numSemesters}\n")
                                
                        # show in terminal
                        print("Your data:")
                        print(f"First name: {firstName}, Last Name: {lastName}")
                        print(f"Title: {title}, Age: {age}, Nationality: {nationatily}")
                        print(f"Courses: {numCourses}, Semesters: {numSemesters}")
                        print(f"Registration status: ", registrationStatus)
                        print("----------------------------------------------------------")
                else:
                        messagebox.showwarning(title="Error",message="The first name and last name are required!!!")

        else:
                messagebox.showwarning(title = "Terms", message = "You did not accepted the terms")
        
