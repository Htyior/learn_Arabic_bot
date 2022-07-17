import sqlite3
from telegram import *
from telegram.ext import *
from datetime import datetime
import os

current_path = os.getcwd()

class gather:
    def __init__(self) -> None:
        self.conn = sqlite3.connect(f"{current_path}/Modules/DataBase/DataBase.db", check_same_thread=False)
        self.cursor = self.conn.cursor()


    """Creating the database"""
    def createDatabase(self):
        self.conn = sqlite3.connect(f"{current_path}/Modules/DataBase/DataBase.db", check_same_thread=False)
        
        # Create table for users
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users_info(
            user_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
            name char,
            last_name char,
            user_name char,
            level INTEGER,
            chat_id str,
            start_time str
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS level(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            lesson TEXT,
            question TEXT,
            option1 TEXT,
            option2 TEXT,
            option3 TEXT,
            option4 TEXT,
            right_option TEXT
        )""")


    def botStart(self, update: Update, context: CallbackContext):
        self.first_name = update.effective_user.first_name
        self.last_name = update.effective_user.last_name
        self.user_name = update.effective_user.username
        self.chat_id = update.effective_chat.id
        now = datetime.now()
        self.time = now.strftime("%Y-%m-%d %H:%M")

        self.cursor.execute(f"SELECT user_name from users_info WHERE chat_id = ?",(self.chat_id,))
        result = self.cursor.fetchall()
        if str(result) == "[('"+self.user_name+"',)]":
            pass

        else:    
            self.cursor.execute(f"INSERT INTO users_info (name, last_name, user_name, level, chat_id, start_time) VALUES (?, ?, ?, ?, ?, ?)",
            (self.first_name, self.last_name, self.user_name, 1, self.chat_id, self.time))
            self.conn.commit()

            print(f"{self.first_name} {self.last_name} started the bot.(ID: {update.effective_user.username})")


    def question(self, update: Update, context: CallbackContext):
        
        print("1")
        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            self.cursor.execute(f"SELECT question FROM level WHERE id = ?", (row))
            question = self.cursor.fetchall()
            for tow in question:
                update.message.reply_text(tow[0])

            self.cursor.execute(f"SELECT option1, option2, option3, option4  FROM level WHERE id = ?", (row))
            question = self.cursor.fetchall()
            for tow in question:
                return [
                    [tow[0]], [tow[1]],
                    [tow[2]], [tow[3]]
                    ]


    def lesson(self, update: Update, context: CallbackContext):
        
        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            self.cursor.execute(f"SELECT lesson FROM level WHERE id = ?", (row))
            lesson = self.cursor.fetchall()
            for tow in lesson:
                if tow[0] == None:
                    return("The game is over")
                else:
                    for tow in lesson:
                        return(tow[0])


    def level_up(self, update: Update, context: CallbackContext):

        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id = {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            tow = int(row[0]) + 1
            self.cursor.execute(f"UPDATE users_info set level = ({tow}) WHERE chat_id = {update.effective_user.id}")
            self.conn.commit()
            print(f"{update.effective_user.name} leveled up !")

    def right_answer(self, update: Update, context: CallbackContext):

        self.cursor.execute(f"SELECT level FROM users_info WHERE chat_id == {update.effective_user.id}")
        result = self.cursor.fetchall()
        for row in result:
            self.cursor.execute(f"SELECT right_option FROM level WHERE id = {row[0]}")
            question = self.cursor.fetchall()
            for tow in question:
                return str(tow[0])
