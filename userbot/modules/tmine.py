from userbot.util import admin_cmd
from telethon import events
import asyncio
somto = 331210651
cj = -1001377775174

@bot.on(events.NewMessage(pattern="", incoming=True))
async def handler(event):
    me = await event.client.get_me()
    if event.message.from_id != somto:
        return
    if "> exhausted miners:" not in event.message.message:
        return
    if me.first_name in event.message.message:
        return
    await asyncio.sleep(5)
    await event.client.send_message(TCOIN, "!mine")
