import os
import requests

# URL источника (m3u/api) или локальный список базовых потоков Zala
SOURCE_URL = "https://raw.githubusercontent.com/user/repository/main/base_zala.m3u"
OUTPUT_FILE = "zala_auto.m3u"

HEADER = """#EXTM3U url-tvg="http://epg.it999.ru/epg2.xml.gz" refresh="24"\n"""

def fetch_and_generate():
    try:
        response = requests.get(SOURCE_URL, timeout=15)
        response.raise_for_status()
        content = response.text

        # Валидация и фильтрация битых тегов/потоков
        lines = content.splitlines()
        output_lines = [HEADER]
        
        for line in lines:
            if line.startswith("#EXTINF") or line.startswith("http"):
                output_lines.append(line)

        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(output_lines))
            
        print("Плейлист успешно обновлен.")

    except Exception as e:
        print(f"Ошибка при обновлении плейлиста: {e}")

if __name__ == "__main__":
    fetch_and_generate()
