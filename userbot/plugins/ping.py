from telethon import events
from datetime import datetime
from userbot.__init__ import StartTime
import time

@command(pattern="^.ping")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    await event.edit(f"PONG!\nPong: {ms}\nUptime: {uptime}")
