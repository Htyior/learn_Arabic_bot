from telegram import *
from telegram.ext import *

from ..Buttons.button import btn
from ..DataBase.database_handler import gather

button = btn
database = gather()

class msg:
    def __init__(self) -> None:
        pass

    
    def welcomeMsg(update: Update, context: CallbackContext):
        button.main_btn(update, context)
        database.botStart(update, context)

    
    def help(update: Update, conext: CallbackContext):
        update.message.reply_text("use the buttons")

    
#    def cancel(update: Update, context: CallbackContext):
#        update.message.reply_text("از فرایند خارج شدید.", reply_markup=ReplyKeyboardRemove())
#        btn.main_btn(update, context)


    def response(self, update: Update, context: CallbackContext):

        if update.message.text == "Teach me":
            update.message.reply_text(database.lesson(update, context))

        if update.message.text == "Question":
            button.question_btn(update, context)

#        if update.message.text == "Cancel" :
#            msg.cancel(update, context)

        if str(update.message.text) == database.right_answer(update, context):
            update.message.reply_text("آفرین، درست جواب دادی. میتونی بری سراغ درس بعدی، ولی یادت نره که همین درس رو هم مرور بکنی ;)")
            database.level_up(update, context)
            button.main_btn(update, context)
