from tkinter import *
import random
from Checks import *
from DataBase import Database
from tkinter.font import Font
import tkinter.messagebox
db = Database()

class Show_word(Frame):

    def __init__(self, master):

        super(Show_word, self).__init__(master)
        self.grid()
        ChangeFont = Font(size=10)

        self.master.geometry("630x450")
        self.master.title("Show a word")

        self.labeloption = Label(self, text="Choose your option:")
        self.labeloption.grid(row=0, column=0)

        self.unit = StringVar()
        self.unit.set("random")
        self.unit0 = Radiobutton(self, text="Random", variable=self.unit, value="random", command=self.ActivateRandom)
        self.unit0.grid(row=1, column=0, sticky=W)
        # self.unit1 = Radiobutton(self, text="Ordered", variable=self.unit, value="ordered",command=self.ActivateOrdered)
        # self.unit1.grid(row=2, column=0, sticky=W)
        self.unit2 = Radiobutton(self, text="Leitner", variable=self.unit, value="Leitner",command=self.ActivateLeitner)
        self.unit2.grid(row=3, column=0, sticky=W)


        # self.StartFromLabel = Label(self, text="Start from:")
        # self.StartFromLabel.grid(row=2, column=1, sticky=W)
        # self.StartFromValue = Entry(self)
        # self.StartFromValue.grid(row=2, column=2, sticky=W)
        # self.StartFromValue.insert(0, 1)
        # self.StartFromValue.configure(state='disabled')


        #here we define a global variable..becausue we did not know how to update the numerator for "ordered" option
        self.globnum=IntVar()
        self.globnum.set(0)
        self.button1 = Button(self, text="Show a word ", bg="red", fg="white",command=  self.showword,font=6)
        self.button1.grid(row=4, column=2)

        # self.applychanges = Button(self, text="Apply changes! ", bg="red", fg="white",command=  self.applychangefunc,font=4)
        # self.applychanges.grid(row=2, column=3)
        # self.applychanges.configure(state='disabled')# because by default "random" option is selected

        # self.LeitnerGroupLabel = Label(self, text="group:")
        # self.LeitnerGroupLabel.grid(row=3, column=1, sticky=W)

        Group_Choices = ['Group 1', 'Group 2','Group 3', 'Group 4','Group 5','Group 6','Group 7' ,'Group 8','Group 9 (done)']

        self.LeitnerGroup_var = StringVar()
        self.LeitnerGroup_var.set('Group 1')
        self.LeitnerGroupOptionButton = OptionMenu(self, self.LeitnerGroup_var, *Group_Choices, command=self.Group9Selection)
        self.LeitnerGroupOptionButton.grid(row=3, column=1, sticky=W, columnspan=2)
        self.LeitnerGroupOptionButton.configure(state='disabled')

        self.WordNameInput = Entry(self,font="-weight bold")
        self.WordNameInput.grid(row=5, column=2)

        self.IKnowItButton = Button(self, text="I know!", bg="red", fg="white", font=ChangeFont,command=self.IKnowIt)
        self.IKnowItButton.grid(row=5, column=3)
        self.IKnowItButton.configure(state='disabled')

        self.CannotRememberButton = Button(self, text="Don't know!", bg="red", fg="white", font=ChangeFont, command=self.CannotRemember)
        self.CannotRememberButton.grid(row=5, column=1)
        self.CannotRememberButton.configure(state='disabled')

        self.dummylabel = Label(self, text="")
        self.dummylabel.grid(row=6, column=0)


        self.button2 = Button(self, text="Show the meaning ", bg="red", fg="white", command=self.showmeaning, font=6)
        self.button2.grid(row=7, column=2)

        self.WordMeaningDisplay=Text(self,  width=40, height=10, wrap=WORD, font="-weight bold")
        self.WordMeaningDisplay.grid(row=8, column=1, columnspan=3)

        # self.WordNoLabel = Label(self, text="Word number:")
        # self.WordNoLabel.grid(row=10, column=1)
        self.WordNoDisplay = Entry(self,state="readonly",width=25)
        self.WordNoDisplay.grid(row=10, column=2)
        # self.WordNoDisplay.configure(state='readonly')


        self.meaningchanges = Button(self, text="Modify Meaning ", bg="red", fg="white", command=self.meaningchangefunc,font=ChangeFont)
        self.meaningchanges.grid(row=10, column=3,columnspan=2)

        self.DeleteButton = Button(self, text="Delete word!", bg="red", fg="white",command=self.DeleteTheWord,font=ChangeFont)
        self.DeleteButton.grid(row=10, column=1)

        # make it by default inactive so user accidentally will not erase all meanings. only activate it after showing the meaning
        self.meaningchanges.configure(state='disabled')

    def Group9Selection(self, value):
        if value == "Group 9 (done)":
            self.IKnowItButton.configure(state='disabled')
            self.CannotRememberButton.configure(state='disabled')

        else:
            self.IKnowItButton.configure(state='normal')
            self.CannotRememberButton.configure(state='normal')

    def ActivateRandom(self):
        # self.StartFromValue.configure(state='disabled')
        # self.applychanges.configure(state='disabled')
        self.IKnowItButton.configure(state='disabled')
        self.CannotRememberButton.configure(state='disabled')
        self.LeitnerGroupOptionButton.configure(state='disabled')
        self.WordNameInput.delete(0, END)
        self.WordNoDisplay.configure(state='normal')
        self.WordNoDisplay.delete(0, END)
        self.WordMeaningDisplay.delete(0.0, END)
        self.WordNoDisplay.configure(state='readonly')

    def ActivateOrdered(self):
        # self.StartFromValue.configure(state='normal')
        # self.applychanges.configure(state='normal')
        self.IKnowItButton.configure(state='disabled')
        self.CannotRememberButton.configure(state='disabled')
        self.LeitnerGroupOptionButton.configure(state='disabled')

    def ActivateLeitner(self):
        # self.StartFromValue.configure(state='disabled')
        # self.applychanges.configure(state='disabled')
        self.IKnowItButton.configure(state='normal')
        self.CannotRememberButton.configure(state='normal')
        self.LeitnerGroupOptionButton.configure(state='normal')
        self.WordNameInput.delete(0, END)
        self.WordNoDisplay.configure(state='normal')
        self.WordNoDisplay.delete(0, END)
        self.WordMeaningDisplay.delete(0.0, END)
        self.WordNoDisplay.configure(state='readonly')

    # def applychangefunc(self):
    #     checkobject = Checkentryclass(self.master)
    #     if (checkobject.ApplyChange(self.StartFromValue.get(), str(db.DB_len()))):
    #         self.globnum.set(0)

    def meaningchangefunc(self):
        WordMeaning = self.WordMeaningDisplay.get("1.0", END)
        WordName = self.WordNameInput.get()
        db.UpdateMeaning(WordName,WordMeaning)

    def DeleteTheWord(self):
        checkobject = Checkentryclass(self.master)
        if (checkobject.ShowingMeaning(self.WordNameInput.get())):
            WordName = self.WordNameInput.get()
            db.DeleteTheWord(WordName)
            self.WordNameInput.delete(0, END)
            self.WordNoDisplay.configure(state='normal')
            self.WordNoDisplay.delete(0, END)
            self.WordMeaningDisplay.delete(0.0, END)
            self.WordNoDisplay.configure(state='readonly')

    def IKnowIt(self):
        checkobject = Checkentryclass(self.master)
        if (checkobject.ShowingMeaning(self.WordNameInput.get())):
            WordName = self.WordNameInput.get()
            #increase group number by 1
            db.UpdateLeitnerGroup(WordName, int(self.SelectedGroup)+1)
            self.WordNameInput.delete(0, END)  # note that here we input "0" and not "0.0
            self.WordNoDisplay.configure(state='normal')
            self.WordNoDisplay.delete(0, END)
            self.WordMeaningDisplay.delete(0.0, END)
            self.WordNoDisplay.configure(state='readonly')




    def CannotRemember(self):
        checkobject = Checkentryclass(self.master)
        if (checkobject.ShowingMeaning(self.WordNameInput.get())):
            WordName = self.WordNameInput.get()
            db.UpdateLeitnerGroup(WordName,  1)
            self.WordNameInput.delete(0, END)  # note that here we input "0" and not "0.0
            self.WordNoDisplay.configure(state='normal')
            self.WordNoDisplay.delete(0, END)
            self.WordMeaningDisplay.delete(0.0, END)
            self.WordNoDisplay.configure(state='readonly')


    def showword(self):
        self.WordNameInput.delete(0, END)  # note that here we input "0" and not "0.0
        self.WordNoDisplay.configure(state='normal')
        self.WordNoDisplay.delete(0, END)
        self.WordMeaningDisplay.delete(0.0, END)
        self.WordNoDisplay.configure(state='readonly')
        self.meaningchanges.configure(state='disabled')  # here again we activate this option
        selected_option = self.unit.get()

        count = db.DB_len()
        if count==0:
            tkinter.messagebox.showinfo("Warning!", "There is no word in the database. Please add some new words.", parent=self.master)
        else:

            if selected_option== 'random':
                WordInfo=db.SelectRandomWord()
                wordName, wordMeaning=WordInfo[1],WordInfo[2]
            # elif selected_option== 'ordered' :
            #     FirstSelectedvalue = int(self.StartFromValue.get())
            #     count = db.DB_len()
            #
            #     #here we update the global variable
            #     # global globnum
            #
            #     # SelectedID = FirstSelectedvalue+self.globnum.get()
            #     # if self.globnum.get()+FirstSelectedvalue <count:
            #     #     self.globnum.set(self.globnum.get()+1)
            #     # else:
            #     #     self.globnum.set(0)
            #
            #     SelectedID = FirstSelectedvalue+db.OrderCounter
            #     if db.OrderCounter+FirstSelectedvalue <count:
            #         db.OrderCounter += 1
            #     else:
            #         db.OrderCounter =0
            #
            #     print(db.OrderCounter)
            #     WordInfo = db.SelectOneWord(SelectedID)
            #     wordName, wordMeaning = WordInfo[1], WordInfo[2]

            else:
                GroupsLagOfTime=[1,2,3,5,7,10,20,30,1e-15]
                SelectedGroupString=self.LeitnerGroup_var.get().split()[1]
                self.SelectedGroup=int(SelectedGroupString)
                DurationInSecond = GroupsLagOfTime[self.SelectedGroup - 1] * 24 * 3600
                ThisGroupSelectedDF = db.SelectAGroup(self.SelectedGroup, DurationInSecond)

                if len(ThisGroupSelectedDF) > 0:
                    if self.SelectedGroup == 9:
                        wordName, wordMeaning = ThisGroupSelectedDF.iloc[db.Group9Id, 1], ThisGroupSelectedDF.iloc[db.Group9Id, 2]
                        if db.Group9Id< len(ThisGroupSelectedDF)-1:
                            db.Group9Id+=1
                        else:
                            db.Group9Id=0

                    else:

                        wordName, wordMeaning = ThisGroupSelectedDF.iloc[0, 1], ThisGroupSelectedDF.iloc[0, 2]

                else:
                    tkinter.messagebox.showinfo("Error",
                                                "no word for this group. Check another group!.\n",
                                                parent=self.master)




            self.WordNameInput.delete(0, END)  # note that here we input "0" and not "0.0
            self.WordNameInput.insert(0, wordName)  # note that here we input "0" and not "0.0
            self.WordNoDisplay.configure(state='normal')
            self.WordNoDisplay.delete(0, END)
            if selected_option== 'random':
                self.WordNoDisplay.insert(0, "%d total words"%(count))
            else:
                if self.SelectedGroup<9:
                    self.WordNoDisplay.insert(0, "%d more words in group %d" % (len(ThisGroupSelectedDF)-1,self.SelectedGroup))
                else:
                    self.WordNoDisplay.insert(0, "%d words in group 9" % (len(ThisGroupSelectedDF)))


            self.WordMeaningDisplay.delete(0.0, END)
            self.WordNoDisplay.configure(state='readonly')






    def showmeaning(self):
        checkobject = Checkentryclass(self.master)
        if (checkobject.ShowingMeaning(self.WordNameInput.get())):
            self.meaningchanges.configure(state='normal') # here we activate the option of editing meanings

            # WordInfo = db.SelectOneWord(int(self.WordNoDisplay.get().split()[1].split("/")[0]))
            WordName = self.WordNameInput.get()
            wordMeaning = db.GetMeaning(WordName)

            self.WordMeaningDisplay.delete(0.0,END)
            self.WordMeaningDisplay.insert(0.0, wordMeaning)




