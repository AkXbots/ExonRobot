Skip to content
Yonko9770
/
AkenoBot
Public
forked from YeahKakashi/Kakashibot
Code
Pull requests
Actions
Projects
Security
Insights
AkenoBot/Shikimori/modules/image_reverse_search.py
@Yonko9770
Yonko9770 Create image_reverse_search.py
 1 contributor
221 lines (189 sloc)  6.65 KB

import os
import re
import urllib
import urllib.parse
import urllib.request
from urllib.error import URLError, HTTPError

import requests
from bs4 import BeautifulSoup
from telegram import InputMediaPhoto, TelegramError

from Shikimori import dispatcher
from Shikimori.modules.disable import DisableAbleCommandHandler
from Shikimori.modules.helper_funcs.alternate import typing_action

opener = urllib.request.build_opener()
useragent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.38 "
    "Safari/537.36 "
)
# useragent = 'Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/52.0.2743.98 Mobile Safari/537.36'
opener.addheaders = [("User-agent", useragent)]


@typing_action
def reverse(update, context):
    if os.path.isfile("okgoogle.png"):
        os.remove("okgoogle.png")

    msg = update.effective_message
    chat_id = update.effective_chat.id
    rtmid = msg.message_id
    args = context.args
    imagename = "okgoogle.png"

    reply = msg.reply_to_message
    if reply:
        if reply.sticker:
            file_id = reply.sticker.file_id
        elif reply.photo:
            file_id = reply.photo[-1].file_id
        elif reply.document:
            file_id = reply.document.file_id
        else:
            msg.reply_text("Reply to an image or sticker to lookup.")
            return
        image_file = context.bot.get_file(file_id)
        image_file.download(imagename)
        if args:
            txt = args[0]
            try:
                lim = int(txt)
            except BaseException:
                lim = 2
        else:
            lim = 2
    elif args:
        splatargs = msg.text.split(" ")
        if len(splatargs) == 3:
            img_link = splatargs[1]
            try:
                lim = int(splatargs[2])
            except BaseException:
                lim = 2
        elif len(splatargs) == 2:
            img_link = splatargs[1]
            lim = 2
        else:
            msg.reply_text("/reverse <link> <amount of images to return.>")
            return
        try:
            urllib.request.urlretrieve(img_link, imagename)
        except HTTPError as HE:
            if HE.reason == "Forbidden":
                msg.reply_text(
                    "Couldn't access the provided link, The website might have blocked accessing to the website by "
                    "bot or the website does not existed. "
                )
                return
            if HE.reason == "Not Found":
                msg.reply_text("Image not found.")
                return
        except URLError as UE:
            msg.reply_text(f"{UE.reason}")
            return
        except ValueError as VE:
            msg.reply_text(f"{VE}\nPlease try again using http or https protocol.")
            return
    else:
        msg.reply_markdown(
            "Please reply to a sticker, or an image to search it!\nDo you know that you can search an image with a "
            "link too? /reverse [picturelink] <amount>. "
        )
        return

    try:
        searchUrl = "https://www.google.com/searchbyimage/upload"
        multipart = {
            "encoded_image": (imagename, open(imagename, "rb")),
            "image_content": "",
        }
        response = requests.post(searchUrl, files=multipart, allow_redirects=False)
        fetchUrl = response.headers["Location"]

        if response != 400:
            xx = context.bot.send_message(
