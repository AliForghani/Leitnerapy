from tkinter import *
import tkinter.messagebox
from DataBase import Database

db = Database()

class New_word(Frame):
    def __init__(self, master):
        super(New_word, self).__init__(master)
        self.Frame1=Frame(master)
        self.Frame1.pack(fill=BOTH, expand=1)# the parameters make sure the frame is the same size as windows always

        #self.create_widgets()
        self.master.geometry("400x300")
        self.master.title("Enter new word")  #
        self.input1label = Label(self.Frame1, text="Enter word:")
        self.input1label.pack()
        self.input1 = Entry(self.Frame1, font="-weight bold")
        self.input1.pack()

        self.input2label = Label(self.Frame1, text="Enter meaning:")
        self.input2label.pack()
        self.input2=Text(self.Frame1,  width=40, height=10, wrap=WORD, font="-weight bold")
        self.input2.pack()

        self.button1 = Button(self.Frame1, text="Save the word ", bg="red", fg="white",command=self.saveword,font=6)
        self.button1.pack()

    def saveword(self):
        InsertedWord = self.input1.get()
        InsertedMeaning = self.input2.get("1.0",END)
        if InsertedWord=="":
            tkinter.messagebox.showinfo("Warning!", "Enter the word!", parent=self.master)
        elif len (InsertedMeaning)==1: #note that text box has length=1 if empty
            tkinter.messagebox.showinfo("Warning!", "Enter its meaning!", parent=self.master)
        else:
            db.insertNewWord(InsertedWord,InsertedMeaning)
            self.input1.delete(0, END)  # note that here we input "0" and not "0.0
            self.input2.delete(0.0, END)



