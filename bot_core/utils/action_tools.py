import re
from bot_core.utils.msg_literals import HELLO_MSG_MODE
from bot_core.settings import cov_info, redis


def redis_pop(coll_name):
    return redis.lpop(coll_name)


def get_status_by_countries(*countries):
    return str(
        {
            country_name: cov_info.get_status_by_country_name(country_name)
            for country_name in countries
        }
    )


def cmd_analysis(msg_data):
    print(f"MSG DATA: {msg_data}")
    text = msg_data.get("text")
    chat_id = msg_data.get("chat_id")
    username = msg_data.get("username")
    firstname = msg_data.get("firstname")
    reply_msg = ""
    if len(text.split("/")) > 1:
        _, cmd, *countries = re.split("/|,| ")
        reply_msg = {
            "start": HELLO_MSG_MODE.format(firstname),
            "get": get_status_by_countries(countries),
        }.get(cmd)
        print(f"FINAL REPLY: {reply_msg}")

    redis.rpush("replies", reply_msg)
