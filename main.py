from telegram.ext import Updater, CommandHandler, PicklePersistence, ConversationHandler
from flask import Flask
import threading
import datetime
import time
import logging
import tokens
import signal

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
        diff = now - latest_update
        diff_secs = diff.seconds
        if diff_secs > (60*5):
            try:
                updater.bot.send_message(chat_id=tokens.chat_id, text="Service is down")
            except Exception as error:
                print(error)
        del diff_secs
        del diff
        del now
        time.sleep(2*60)


def main():
    TOKEN = tokens.my_token
    global updater
    updater = Updater(token=TOKEN, use_context=True)

    updater.start_polling()
    updater.idle()

def handler(signum, frame):
    print('idle point')
    updater.idle()


if __name__ == "__main__":
    # threading.Thread(target=main).start()
    # app.run()
    signal.signal(signal.SIGINT, handler)
    threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 8333, "debug": True, "use_reloader": False}).start()
    threading.Thread(target=alive_checker).start()
    main()
