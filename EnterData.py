from tkinter import *
from tkinter import messagebox

def enter_data(firstNameEntry, lastNameEntry, titleCombobox, ageSpinbox, nationalityCombobox):
        firstName = firstNameEntry.get()
        lastName = lastNameEntry.get()
        title = titleCombobox.get()
        age = ageSpinbox.get()
        nationatily = nationalityCombobox.get()
        
        # show in messagebox
        messagebox.showinfo(title = "Your saved data", message = f"First name: {firstName}\nLast Name: {lastName}\nTitle: {title}\nAge: {age}\nNationality: {nationatily}\n")
        
        # show in terminal
        print("Your data:")
        print(f"First name: {firstName}, Last Name: {lastName}")
        print(f"Title: {title}, Age: {age}, Nationality: {nationatily}")


        