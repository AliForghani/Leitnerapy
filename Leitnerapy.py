from tkinter import *

from AddNewWord import *
from ShowWord import *


class Welcome(Frame):

    def __init__(self, master): #by choosing name "master" in this line, the parent window is called "master" in subsequent lines
        super(Welcome,self).__init__(master)
        self.Frame1=Frame(master)
        self.Frame1.pack(fill=BOTH,expand=1)
        self.Frame2=Frame(master)
        self.Frame2.pack(fill=BOTH,expand=1)

        self.button1 = Button(self.Frame1, text=" Enter new words!", bg="red", fg="white", font=6,command=self.newword)
        self.button1.pack(fill=BOTH,expand=1)

        self.button2 = Button(self.Frame2, text=" Have fun with words!", bg="red", fg="white", font=6,command=self.showword)
        self.button2.pack(fill=BOTH,expand=1)

        self.master.title("Words database")
        self.master.geometry("400x300")

    def newword(self):
        root1 = Toplevel(self.master)
        New_word(root1)


    def showword(self):
        root2 = Toplevel(self.master)
        Show_word(root2)





root = Tk()
myGUIWelcomeWindow=Welcome(root)#we are saying to go to class Welcome and use "root" as the Farme of that class
root.iconbitmap(default='w.ico')
root.mainloop()








