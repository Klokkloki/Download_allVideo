import yt_dlp

def download_rutube_video(url):
    try:
        # Настройки для yt-dlp, эквивалентные команде
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Выбираем лучшее качество видео и аудио
            'merge_output_format': 'mp4',         # Объединяем в MP4
            'outtmpl': '/Users/dzavansirmahmudov/Videos/%(title)s.%(ext)s',  # Сохраняем в папку Videos
            'quiet': False,                       # Вывод логов
            'no_warnings': False,
            'noplaylist': True,                   # Игнорируем плейлисты
        }

        # Инициализация yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Скачиваю видео: {url}")
            ydl.download([url])

        print("Скачивание завершено!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Функция для регулирования и ввода ссылки 
if __name__ == "__main__":
    video_url = input("Введите URL видео: ")
    download_rutube_video(video_url)