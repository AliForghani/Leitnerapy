# Leitnerapy
## A software developed with Python's tkinter and sqlite packages for learning new words efficiently based on Leitner method




### Python solution
The software is an object-oriented program containing four python scripts working together:
- Leitnerapy.py... Responsible for starting the program.
- AddNewWord.py... Responsible for adding a new word and its meaning into a sql database
- ShowWord.py... Responsible to retrieve a word from database (randomly or based on Leitner method),
 asking the word from the user, and updating the word's Leitner group based on the user's response
- DataBase.py... Containing some functions to manage data in the database


### Making an stand-alone executable:
In addition to above four python codes, two other files have been provided for making an executable:
- ExeSetup.py... Which contains the settings needed to make a exe using Python's cx_Freeze package
- MakeExe.bat... A batch file to run the "ExeSetup.py" file using a python executable

### database file
The file "Words.db" is the sqlite database file containing some sample/initial words. Having this file in the same
 directory as other python files is necessary for using the software. If needed, programs such as SQLiteStudio can be used to
 investigate the contents of "Words.db" file.

### Icon file
w.ico is simply an icon file. Having this file in the same directory as other python files is necessary for using
 the software




