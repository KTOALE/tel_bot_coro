from json import loads
from telebot import TeleBot
from bot_replier.settings import TOKEN, redis_sub
from bot_replier.utils.redis_topics import REPLY_COLL_NAME



def main():
    bot = TeleBot(TOKEN)

    redis_sub.subscribe(REPLY_COLL_NAME)

    while(True):
        reply_msg = redis_sub.get_message().get("data", None)
        if reply_msg:
            reply_msg_data = loads(reply_msg)
            bot.send_message(
                reply_msg_data.get("chat_id"),
                reply_msg_data.get("reply_msg")
            )


if __name__=="__main__":
    main()