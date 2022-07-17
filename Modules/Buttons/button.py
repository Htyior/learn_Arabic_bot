from telegram import *
from telegram.ext import *
import sqlite3

from ..DataBase.database_handler import gather

databse = gather()
class btn():
    def __init__(self) -> None:
        pass


    """Buttons for question games"""
    def question_btn(update: Update, context: CallbackContext):

            # send the button to user
        context.bot.send_message(
            chat_id=update.effective_chat.id, text="با توجه به درس، سوال را پاسخ دهید.", 
            reply_markup=ReplyKeyboardMarkup(databse.question(update, context), one_time_keyboard=True)
            )

    def main_btn(update: Update, context: CallbackContext):
        
        # creating the button
        buttons = [["Teach me"], ["Question"]]

        # send the button to user
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Hello Habibi",
            reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
            )
    
#    def cancel (update: Update, context: CallbackContext):
#                buttons = [["Cancel"]]
#                update.message.reply_text("", reply_markup=ReplyKeyboardMarkup(buttons, one_time_keyboard=True))



                # update.message.from_user