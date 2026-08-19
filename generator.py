import os

OUTPUT_FILE = "zala_auto.m3u"

# Готовый рабочий шаблон плейлиста ZALA (расширяемый)
PLAYLIST_CONTENT = """#EXTM3U url-tvg="http://epg.it999.ru/epg2.xml.gz" refresh="24"

#EXTINF:-1 group-title="Беларуские", Беларусь 1
http://iptv.zala.by/stream/belarus1/index.m3u8
#EXTINF:-1 group-title="Беларуские", Беларусь 2
http://iptv.zala.by/stream/belarus2/index.m3u8
#EXTINF:-1 group-title="Беларуские", Беларусь 3
http://iptv.zala.by/stream/belarus3/index.m3u8
#EXTINF:-1 group-title="Беларуские", ОНТ
http://iptv.zala.by/stream/ont/index.m3u8
#EXTINF:-1 group-title="Беларуские", СТВ
http://iptv.zala.by/stream/stv/index.m3u8
#EXTINF:-1 group-title="Познавательные", Discovery Channel
http://iptv.zala.by/stream/discovery/index.m3u8
#EXTINF:-1 group-title="Фильмы", еврокино
http://iptv.zala.by/stream/eurokino/index.m3u8
"""

def generate():
    try:
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(PLAYLIST_CONTENT.strip())
        print("Плейлист успешно сформирован.")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

if __name__ == "__main__":
    generate()
