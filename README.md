# Leitnerapy
## A software developed with Python's tkinter and sqlite packages for learning new words efficiently based on Leitner method


### Python solution
The software is an object-oriented program containing four python scripts working together:
- Leitnerapy.py... starts the program.
- AddNewWord.py... adds a new word and its meaning into a sql database
- ShowWord.py... retrieves a word from database (randomly or based on Leitner method),
 asking the word from the user, and updating the word's Leitner group based on the user's response
- DataBase.py... contains some functions to manage data in the database

### other needed files
The file "w.ico" is simply an icon file and "Words.db" is the sqlite database file containing some initial words.
Having these two files in the same directory as other python files is necessary for using the software.
If needed, programs such as SQLiteStudio can be used to investigate the contents of "Words.db" file.

### Making an executable:
Below two files have been provided for making a stand-alone executable (for use in computers without a python installation):
- ExeSetup.py... contains the settings needed to make a exe using Python's cx_Freeze package
- MakeExe.bat... A batch file to run the "ExeSetup.py" file using a python installation




