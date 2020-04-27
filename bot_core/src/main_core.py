from json import loads
from bot_core.utils.redis_topics import CMD_COLL_NAME
from bot_core.utils.action_tools import cmd_analysis, pub_sub



def main():
    pub_sub.subscripe(CMD_COLL_NAME)
    while (True):
        msg_data = pub_sub.get_message().get("data", None)
        if msg_data:
            cmd_analysis(
                loads(msg_data)
            )


if __name__ == "__main__":
    main()
