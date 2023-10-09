

import time, os
from pyrogram import Client, filters, enums
from hero.prog import progress_message,humanbytes

async def progress(current, total):
  await sts.edit_text(f"{current * 100 / total:.1f}%")

@Client.on_message(filters.command("rename"))
async def rename(bot,msg):
  if len(msg.text) <= 7:
    return await msg.reply_text("Please Type New name with /rename command.",quote=True)
  reply = msg.reply_to_message
  new_name = msg.text.split(" ",1)[1]
  if reply != None:
    try:
      sts = await reply.reply_text("Wait lemme Check 😊", quote=True)
      c_time = time.time()
      await bot.download_media(reply,file_name=new_name,progress=progress_message,progress_args=("Downloading Started 😎",sts,c_time))
      path = f"downloads/{new_name}"
      await reply.reply_document(document=path,thumb="hero/thumb.jpg",force_document=True,progress=progress_message,progress_args=("Uploading Started 😎",sts,c_time))
      await sts.delete()
      os.remove(path)
    except:
      await msg.reply("Error Occured. Maybe you replied to a message")
    


