from functools import wraps


def insert_send_msg_back(send_msg_back, msg):
    def decorated_func(func):
        @wraps(func)
        def inner(message):
            chat_id = func(message)
            send_msg_back(chat_id, msg)
        return inner
