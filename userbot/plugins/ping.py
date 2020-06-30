# special thanks to Sur_vivor 
# first on friday by leobrownlee 




from telethon import events
from datetime import datetime
from userbot.utils import admin_cmd
from userbot.__init__ import StartTime
import time

#@command(pattern="^.ping$")
@borg.on(admin_cmd(pattern="ping$"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("🏓 Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    await event.edit(f"🏓PONG!\nPing speed: {ms}\n🤖Userbot Uptime: {uptime}")
