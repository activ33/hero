import tqdm
import os,time
from hero.kwik_token import get_dl_link
import hero.pahe as pahe  # Import animepahe module
from colorama import Fore
from pyrogram import Client,filters
from hero.prog import progress_message,humanbytes
import anipie
# Function to replace special characters in a string
def replace_special_characters(input_string, replacement="_"):
    special_characters = "!@#$%^&*()_+{}[]|\\:;<>,.?/~`"
    for char in special_characters:
        input_string = input_string.replace(char, replacement)
    return input_string

@Client.on_message(filters.command("pahe"))
async def nonee(bot,msg):
  hero = msg.text.split(",")
  query = hero[1]
  choice = int(hero[2])
  episode_range = hero[3].split("-")
  lang = "jpn"
  quality = int(hero[4])
  sts = await msg.reply("Processing")
  list_of_anime = pahe.search_apahe(query)
  anime_id = list_of_anime[choice][6]
  episode_range = (
    [int(episode_range[0]), int(episode_range[1]) + 1]
    if len(episode_range) == 2
    else [int(episode_range[0]), int(episode_range[0]) + 1]
)
  await sts.edit_text("Finding Episode Ids")
  episode_ids = pahe.mid_apahe(session_id=anime_id, episode_range=episode_range)
  episodes_data = pahe.dl_apahe1(anime_id=anime_id, episode_ids=episode_ids)
  await sts.edit_text("Organising Episodes Links")
  episodes = {}
  index = episode_range[0]
  for key, value in episodes_data.items():
    sorted_links = {}
    for link_info in value:
      link, size, lang = link_info
      size = int(size.split('p')[0])
      if lang == '':
         lang = 'jpn'
      if lang not in sorted_links:
         sorted_links[lang] = {}
      if size not in sorted_links[lang]:
         sorted_links[lang][size] = []
      sorted_links[lang][size].append(link)
    episodes[index] = sorted_links
    index += 1
  await sts .edit_text("Finding Downloas Links")
  for key, items in episodes.items():
    backup_quality = list(episodes[key][lang])[-1]
    try:
       episodes[key] = episodes[key][lang][quality][0]
    except:
      try:
         episodes[key] = episodes[key][lang][backup_quality][0]
      except:
       pass
  await sts.edit_text("Downloading will Starting soon..")
  for key, value in tqdm.tqdm(episodes.items(), desc="Parsing links"):
    episodes[key] = pahe.dl_apahe2(value)
    print(episodes[key])
  info = anipie.SearchAnime(query)
  rmj = info.getAnimeRomajiName()
  eng = info.getAnimeEnglishName()
  stdt = info.getAnimeStartDate()
  year = stdt.split("/",2)[2]
  type = info.getAnimeFormat()
  status = info.getAnimeStatus()
  episodess = info.getAnimeEpisodes()
  season = info.getAnimeSeason()
  cover = info.getAnimeCoverImage()
  genre = info.getAnimeGenres()
  img = info.getAnimeCoverImage()
  orc = cover.replace("medium", "large")
  ID = info.getAnimeID()
  aniinfo = f"__{rmj}__\n**{eng} ({year})**\n━━━━━━━━━━━━━━━\n**Type : **{type}\n**Episodes : **{episodess}\n**Season : **{season} {year}\n**Genre : **{genre}\n**Status : **{status} #A{ID}\n━━━━━━━━━━━━━━━\n**📥 DOWNLOAD: {quality}P ENGSUB**\n"
  aif = await bot.send_photo(-1001963887250,photo=orc,caption=aniinfo)
  await aif.copy(-1001972977023)
  title = replace_special_characters(list_of_anime[choice][0])
  if not os.path.exists("Anime"):
     os.makedirs("Anime")
  for key, value in tqdm.tqdm(episodes.items(), desc="Downloading Episodes"):
    destination = os.path.join("Anime",f"{key} - {eng} [{quality}P] @AnimeFiles.mkv")
    download_link = get_dl_link(value)
    print("download_link")
    await sts.edit_text(f"**EPISODE {key} Downloading Started**")
    anime = pahe.download_file(url=download_link, destination=destination)
    c_time = time.time()
    upl = await bot.send_document(-1001963887250,document=destination,thumb="thumb.jpg")
    await upl.copy(-1001972977023)
    os.remove(destination)
