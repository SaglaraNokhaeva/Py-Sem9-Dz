from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def repeat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg=update.message.text
    await update.message.reply_text(f'{msg}')    


app = ApplicationBuilder().token("5808065349:AAFUUJN0bF6xkzjtl3lIEhszP90yuhboFLY").build()

app.add_handler(CommandHandler("repeat", repeat))
app.run_polling()