from telegram.ext import Updater, CommandHandler, PicklePersistence, ConversationHandler
from flask import Flask
import threading
import datetime
import time
import logging

latest_update = datetime.datetime.now()
updater = None

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="بیا بَخورش")

app = Flask(__name__)
log = logging.getLogger("werkzeug")
log.disabled = True

@app.route("/")
def salman():
    global latest_update
    latest_update = datetime.datetime.now()
    return "big"

def alive_checker():
    while(True):
        now = datetime.datetime.now()
        if (now - latest_update).seconds > 60:
            try:
                updater.bot.send_message(chat_id="ID", text="چوآوآ")
            except Exception as error:
                print(error)
        time.sleep(5)


def main():
    TOKEN = "TOKEN"
    global updater
    updater = Updater(token=TOKEN, use_context=True)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    # threading.Thread(target=main).start()
    # app.run()
    threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8333, "debug": True, "use_reloader": False}).start()
    threading.Thread(target=alive_checker).start()
    main()