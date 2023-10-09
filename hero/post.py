from pyrogram import Client,filters

@Client.on_message(filters.command("post"))
async def post(bot,msg):
  new = msg.text.split(" ",1)[1]
  await msg.reply_document(new)
                     
  
  
  
