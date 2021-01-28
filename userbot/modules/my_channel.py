from telethon import events

@bot.on(events.NewMessage(incoming=True))
async def transfer(event):
    target_channel = -1001473633317
    my_channel = -1001371876881
    if event.chat_id == target_channel:
        await borg.send_message(my_channel, event.message)
