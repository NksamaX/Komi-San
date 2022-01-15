from requests import get
from bs4 import BeautifulSoup
from pyrogram import Client , filters
from pyrogram.types import Message

def define(word : str):
    url = "http://urbandictionary.com/define.php?term=" + word
    response = get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    content = soup.find("div", {"class": "p-5 md:p-8"})
    word = content.find("div" , class_="sm:flex sm:flex-row-reverse")
    meaning = content.find("div", class_="meaning my-4")
    
    return {"word": word.text, "meaning": meaning.text}



@bot.on_message(filters.regex(r"(?i)^define (.*)$"))
def ok(client, m : Message):
    word = m.text.replace(m.text.split(" ")[0], "").strip()
    data = define(word)
    m.reply(f"**{data['word']}**\n\n{data['meaning']}")
