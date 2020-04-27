from telebot import TeleBot
# from src.messages_handlers import say_hi
# from bot_sender.settings import TOKEN
from bot_sender.settings import TOKEN, redis#, OUTPUT_RQ



def main():
    bot = TeleBot(TOKEN)
    # action = bot.reply_to
    # say_hi_handler = insert_send_msg_back(action, "Hi, MTHRFKR!!!")(say_hi)

    while(True):
        redis.si
        if
        bot.send_message(incomming_msg.chat.id, reply_message, parse_mode=HELLO_MSG_MODE[1])


if __name__=="__main__":
    main()