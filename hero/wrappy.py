

import anipie

def anipie_anime(anime_name):
  search_anime = anipie.SearchAnime(anime_name)
  
  romanji_title = search_anime.getAnimeRomajiName()
  english_title = search_anime.getAnimeEnglishName()
  return romanji_title,english_title
  

anime = anipie_anime('Weathering with you')
print(anime)
  
