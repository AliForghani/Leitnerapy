from tkinter import *
import tkinter.messagebox

class Checkentryclass(Frame):
    def __init__(self, master):
        super(Checkentryclass, self).__init__(master)




    def ShowingMeaning(self, word):

        if word == "":
            tkinter.messagebox.showinfo("Warning!", "Please select a word!", parent=self.master)

        else:
            return True

    def ApplyChange(self, SelectedValue, TotalValue):
        def check_number(s):
            try:
                float(s)
                return False
            except ValueError:
                return True
        if check_number(SelectedValue):
            tkinter.messagebox.showinfo("Warning!", "Enter a valid integer value!", parent=self.master)

        elif (int(SelectedValue) <1 or int(SelectedValue)> int(TotalValue) ):
            tkinter.messagebox.showinfo("Warning!", "Enter a valid integer value in the range of 1 to %s!"%(TotalValue), parent=self.master)

        else:
            return True