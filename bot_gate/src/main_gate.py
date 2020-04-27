from json import dumps
from telebot import TeleBot
from bot_gate.settings import TOKEN, publisher

from bot_gate.utils.redis_topics import CMD_COLL_NAME


def main():
    bot = TeleBot(TOKEN)

    @bot.message_handler()
    def input_msgs(incomming_msg):
        msg_dict = {
            "text": incomming_msg.text,
            "chat_id": incomming_msg.chat.id,
            "username": incomming_msg.from_user.username,
            "firstname": incomming_msg.from_user.first_name,
        }

        new_cmd = dumps(msg_dict)
        print(f"NEW COMMAND: {new_cmd}")
        publisher.publish(CMD_COLL_NAME, new_cmd)
        # build_send_demo_msg(msg_dict)

    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
