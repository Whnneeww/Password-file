import yt_dlp
import sys

def download_video(url):
    ydl_opts = {
        'format': 'best',  # 最高品質でダウンロード
        'outtmpl': '%(title)s.%(ext)s',  # ファイル名を動画タイトルに
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # URLをリストで渡す

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用法: python youtube.py <YouTubeのURL>")
    else:
        video_url = sys.argv[1]  # コマンドライン引数からURLを取得
        download_video(video_url)
