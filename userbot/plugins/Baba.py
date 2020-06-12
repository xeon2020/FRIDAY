
import os

from datetime import datetime

from PIL import Image, ImageDraw, ImageFont

from pySmartDL import SmartDL

from telethon.tl import functions

from userbot.utils import admin_cmd

import asyncio

import shutil 

import random, re



FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
                         "https://telegra.ph/file/8a99501b93f1d0146edc5.jpg",
                         "https://telegra.ph/file/96c0e2986231d8e495a3a.jpg",
                         "https://telegra.ph/file/74deb7bdc0c79efb48860.jpg",
                         "https://telegra.ph/file/896315995995b1a54c3e2.jpg",
                         "https://telegra.ph/file/fb154ccfe1d8b216d72a3.jpg",
                         "https://telegra.ph/file/f2c5b1a634f39c64b9f7a.jpg",
                         "https://telegra.ph/file/7009fcde40bff2c150b0d.jpg",
                         "https://telegra.ph/file/330cd551708e43c430cf0.jpg",
                         "https://telegra.ph/file/81c25b411595baae659db.jpg",
                         "https://telegra.ph/file/0a24f5e97311b761edcc6.jpg",
                         "https://telegra.ph/file/d331fd7696ff39f2a2901.jpg",
                         "https://telegra.ph/file/74ada8c575fc09f4438c5.jpg"
                        ]
@borg.on(admin_cmd(pattern="baba ?(.*)"))
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./FRIDAY/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("\n \n \n \n \n \n \n  \n \n \n \n \n \n \n \n \n                   Time: %H:%M:%S \n                   Date: %d/%m/%y ")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 23)
        drawn_text.text((200, 250), current_time, font=fnt, fill=(230,230,250))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(60)
        except:
            return
