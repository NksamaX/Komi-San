import threading
from sqlalchemy import Column, String
from nksama.plugins.sql import BASE, SESSION
class KukiChats(BASE):
    __tablename__ = "kuki_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id

KukiChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_kuki(chat_id):
    try:
        chat = SESSION.query(KukiChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()

def set_kuki(chat_id):
    with INSERTION_LOCK:
        kukichat = SESSION.query(KukiChats).get(str(chat_id))
        if not kukichat:
            kukichat = KukiChats(str(chat_id))
        SESSION.add(kukichat)
        SESSION.commit()


def rm_kuki(chat_id):
    with INSERTION_LOCK:
        kukichat = SESSION.query(KukiChats).get(str(chat_id))
        if kukichat:
            SESSION.delete(kukichat)
        SESSION.commit()
