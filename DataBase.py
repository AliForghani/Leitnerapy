import sqlite3
import datetime
import pandas as pd


class Database():
    def __init__(self ):
        self.conn = sqlite3.connect( "Words.db")
        self.cur = self.conn.cursor()
        self.Group9Id=0

    def insertNewWord(self,Word, MeaningString):
        now = datetime.datetime.now()
        now_string = now.strftime("%m/%d/%Y %H:%M:%S")
        self.cur.execute("INSERT INTO words VALUES (NULL, ?, ?, 1, ?)", (Word, MeaningString,now_string))
        self.conn.commit()

    def DB_len(self):
        LenOfDB=len(self.cur.execute("SELECT * FROM words").fetchall())
        return LenOfDB

    def SelectRandomWord(self):
        Wordinfo=self.cur.execute("SELECT * FROM words ORDER BY RANDOM() LIMIT 1").fetchone()
        return Wordinfo

    def UpdateMeaning(self,WordName, NewMeaning):
        self.cur.execute("UPDATE words SET Meaning = ? WHERE Word=?",(NewMeaning,WordName))
        self.conn.commit()

    def GetMeaning(self,WordName):
        Wordinfo = self.cur.execute("SELECT * FROM words WHERE Word=?", (WordName,)).fetchone()
        return Wordinfo[2]

    def UpdateLeitnerGroup(self, WordName, NewGroup):
        now = datetime.datetime.now()
        now_string = now.strftime("%m/%d/%Y %H:%M:%S")
        self.cur.execute("UPDATE words SET GroupId = ?, Date=? WHERE Word=?", (int(NewGroup),now_string, WordName))
        self.conn.commit()

    def DeleteTheWord(self,WordName):
        self.cur.execute("DELETE FROM words WHERE Word=?",(WordName,))
        self.conn.commit()

    def SelectAGroup(self,GroupId, DurationInSecond):
        ThisGroupInfo = self.cur.execute("SELECT * FROM words WHERE GroupId=?", (int(GroupId),)).fetchall()
        ThisGroupDF=pd.DataFrame(ThisGroupInfo, columns=["Id", "Word", "Meaning", "GroupId", "CurrentDate"])
        if len(ThisGroupDF)>0:
            ThisGroupDF['DateFormat'] = ThisGroupDF['CurrentDate'].astype('datetime64[ns]')
            # print(ThisGroupDF)
            now = datetime.datetime.now()
            ThisGroupDF["DiffInTime"]= ThisGroupDF.apply(lambda x : (now-x.DateFormat).total_seconds(), axis=1)#  abs(ThisGroupDF['DateFormat']-now).seconds
            # print(ThisGroupDF)
            ThisGroupSelected=ThisGroupDF[ThisGroupDF["DiffInTime"]>=DurationInSecond]
            return ThisGroupSelected

        else:

            return ThisGroupDF




