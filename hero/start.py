

from pyrogram import Client,filters

# Start Message
@Client.on_message(filters.command("start"))
async def start(bot,msg):
  await msg.reply("Hello!",quote=True)