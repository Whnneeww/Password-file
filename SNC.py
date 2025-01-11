from flask import Flask, request, send_file
from pytube import YouTube
import os
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <form method="POST" action="/download">
        YouTube URL: <input type="text" name="url">
        <input type="submit" value="Download">
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f'video_{timestamp}.mp4'

        stream.download(output_path='downloads', filename=filename)

        return send_file(f'downloads/{filename}', as_attachment=True)

    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(port=2554)
