import yt_dlp
import sys

def download_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',  # 最高音質の音声を選択
        'extractaudio': True,         # 音声抽出を有効化
        'audioformat': 'mp3',         # 音声形式をMP3に指定
        'outtmpl': '%(title)s.%(ext)s',  # ファイル名を動画タイトルに
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # URLをリストで渡す

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用法: python youtube_mp3.py <YouTubeのURL>")
    else:
        video_url = sys.argv[1]  # コマンドライン引数からURLを取得
        download_audio(video_url)
