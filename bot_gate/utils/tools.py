from bot_gate.utils.msgs_data import DEMO_MSG
from bot_gate.utils.redis_topics import REPLY_COLL_NAME
from bot_gate.settings import publisher


# def build_send_demo_msg(msg_data):
#     demo_reply = DEMO_MSG.format(msg_data.get("firstname"))
#     publisher.publish(REPLY_COLL_NAME, demo_reply)
#     print(f"DEMO MSG PUBLISHED!!!")
