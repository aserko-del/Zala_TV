import os

OUTPUT_FILE = "zala_auto.m3u"

PLAYLIST_CONTENT = """#EXTM3U url-tvg="http://epg.it999.ru/epg2.xml.gz" refresh="24"

#EXTINF:-1 group-title="Беларуские", Беларусь 1
https://hls.belarus24.by/b24/index.m3u8
#EXTINF:-1 group-title="Беларуские", Беларусь 2
https://stream.voka.tv/live/belarus2/index.m3u8
#EXTINF:-1 group-title="Беларуские", Беларусь 3
https://stream.voka.tv/live/belarus3/index.m3u8
#EXTINF:-1 group-title="Беларуские", Беларусь 4
https://stream.voka.tv/live/belarus4/index.m3u8
#EXTINF:-1 group-title="Беларуские", Беларусь 5
https://stream.voka.tv/live/belarus5/index.m3u8
#EXTINF:-1 group-title="Беларуские", ОНТ
https://ont.by/hls/stream.m3u8
#EXTINF:-1 group-title="Беларуские", СТВ
https://ctv.by/hls/stream.m3u8
#EXTINF:-1 group-title="Беларуские", МИР
https://mir24.tv/hls/stream.m3u8

#EXTINF:-1 group-title="Информационные", НТВ
https://ntv.ru/hls/stream.m3u8
#EXTINF:-1 group-title="Информационные", Россия 1
https://live.russia.tv/hls/stream.m3u8

#EXTINF:-1 group-title="Кино и Сериалы", Амедиа
https://stream.voka.tv/live/amedia/index.m3u8
#EXTINF:-1 group-title="Развлекательные", Домашний
https://domashniy.ru/hls/stream.m3u8
#EXTINF:-1 group-title="Кино и Сериалы", Дом Кино
https://domkino.tv/hls/stream.m3u8
#EXTINF:-1 group-title="Кино и Сериалы", Феникс плюс Кино
https://fenix.tv/hls/stream.m3u8
#EXTINF:-1 group-title="Кино и Сериалы", ТВ 1000 Русское кино
https://stream.voka.tv/live/tv1000rk/index.m3u8
#EXTINF:-1 group-title="Развлекательные", ТВ3
https://tv3.ru/hls/stream.m3u8

#EXTINF:-1 group-title="Музыка", Шансон TV
https://shanson.tv/hls/stream.m3u8
"""

def generate():
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(PLAYLIST_CONTENT.strip())
    print("Плейлист успешно сформирован.")

if __name__ == "__main__":
    generate()
