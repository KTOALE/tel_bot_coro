from json import dumps
from telebot import TeleBot
# from src.messages_handlers import say_hi
# from bot_listenner.settings import TOKEN #, redis
from bot_listenner.settings import TOKEN, redis
from bot_listenner.src.msgs_data import DEMO_MSG


def main():
    bot = TeleBot(TOKEN)
    # action = bot.reply_to
    # say_hi_handler = insert_send_msg_back(action, "Hi, MTHRFKR!!!")(say_hi)
    @bot.message_handler()
    def input_msgs(incomming_msg):
        msg_dict = {
            "text": incomming_msg.text,
            "chat_id": incomming_msg.chat.id,
            "username": incomming_msg.from_user.username,
            "firstname": incomming_msg.from_user.first_name,
        }
        # redis.set("commands", dumps(msg_dict))
        commands = redis.get("commands")
        print(f"commands: {commands}")
        new_cmd = dumps(msg_dict)
        if commands:
            commands.append(new_cmd)
        else:
            redis.set("commands", [new_cmd,])
        for key in redis.keys():
            print(f"element: {redis.get(key)}")
        demo_reply = DEMO_MSG.format(msg_dict.get("firstname"))
        bot.reply_to(incomming_msg, demo_reply)
        print(f"NEW MSG RECIEVED: {msg_dict}")

    bot.polling(none_stop=True)

if __name__=="__main__":
    main()