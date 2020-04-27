from bot_core.utils.constants import CMD_COLL_NAME
from bot_core.utils.action_tools import redis_pop, cmd_analysis


def main():
    msg_data = redis_pop(CMD_COLL_NAME)
    while (True):
        if msg_data:
            cmd_analysis(msg_data)
        msg_data = redis_pop(CMD_COLL_NAME)


if __name__ == "__main__":
    main()
