import ast as nk
from nksama import REDIS_DB

try:
    nk.literal_eval(REDIS_DB.get("KUKIBOT"))
except BaseException:
    REDIS_DB.set("KUKIBOT", "[]")

def is_kuki(chat_id):
    chat = nk.literal_eval(REDIS_DB.get("KUKIBOT"))	
    if chat_id in chat:
    	return True
    return False
	   
def set_kuki(chat_id):
    chat = nk.literal_eval(REDIS_DB.get("KUKIBOT"))
    if chat_id not in chat:
    	chat.append(chat_id)
    	REDIS_DB.set("KUKIBOT", str(chat))
    return 
	
def rm_kuki(chat_id):
	chat = nk.literal_eval(REDIS_DB.get("KUKIBOT"))
	if chat_id in chat:
		chat.remove(chat_id)
		REDIS_DB.set("KUKIBOT", str(chat))
	return 
