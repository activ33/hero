from pyrogram import Client, filters, enums
from AnilistPython import Anilist
anilist = Anilist()

@Client.on_message(filters.command('anime'))
def anime1(bot, msg):
  
  ani = msg.text.split(" ",1)[1]
  info = anilist.get_anime(ani)
  rmj = info["name_romaji"]
  eng = info["name_english"]
  stdt = info["starting_time"]
  year = stdt.split("/",2)[2]
  endt = info["ending_time"]
  type = info["airing_format"]
  status = info["airing_status"]
  episodes = info["airing_episodes"]
  season = info["season"]
  desc = info["desc"]
  score = info["average_score"]
  cover = info["cover_image"]
  gen = info["genres"]
  genr = ' '.join([str(elem) for elem in gen])
  genre = genr.replace(" ",", ")
  img = info["banner_image"]
  orc = cover.replace("medium", "large")
  aniinfo = f"__{rmj}__\n**{eng} ({year})**\n━━━━━━━━━━━━━━━\n**Type : **{type}\n**Episodes : **{episodes}\n**Season : **{season} {year}\n**Genre : **{genre}\n**Status : **{status}\n━━━━━━━━━━━━━━━\n**📥 DOWNLOAD: 720P ENGSUB**\n"
  bot.send_photo(msg.chat.id,photo=orc,caption=aniinfo)

@Client.on_message(filters.command('Manga'))
def manga(bot,msg):
  man = msg.text.split(" ",1)[1]
  info = anilist.get_manga(man)
  rmj = info["name_romaji"]
  eng = info["name_english"]
  stdt = info["starting_time"]
  year = stdt.split("/",2)[2]
  cover = info["cover_image"]
  type = info["release_format"]
  status = info["release_status"]
  chapters = info["chapters"]
  gen = info["genres"]
  genr = ' '.join([str(elem) for elem in gen])
  genre = genr.replace(" ",", ")
  ocr = cover.replace("medium","large")
  maninfo = f"__{rmj}__\n**{eng} ({year})**\n━━━━━━━━━━━━━━━\n**Type : **{type}\n**Chapters : **{chapters}\n**Start date : **{stdt}\n**Genre : **{genre}\n**Status : **{status}\n━━━━━━━━━━━━━━━\n**📥 DOWNLOAD**\n"
  bot.send_photo(msg.chat.id,photo=ocr,caption=maninfo)
