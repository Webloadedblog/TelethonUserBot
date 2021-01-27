from telethon import events

@bot.on(events.NewMessage(incoming=True))
async def transfer(event):
    target_channel = -1001288631370
    my_channel = -1001371876881
    event.message.text = "\n".join(event.message.text.split("\n")[:1])
    if event.chat_id == target_channel:
        await borg.send_message(my_channel, event.message)
