from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/<path:requested_path>', methods=['GET'])
def proxy(requested_path):
    # sitedeta.i-i.f5.siへのURLを組み立てる
    target_url = f'https://sitedeta.i-i.f5.si/{requested_path}'
    
    try:
        # 指定したパスにリクエストを送信
        response = requests.get(target_url)
        
        # ステータスコードと応答内容をそのまま返す
        return (response.content, response.status_code, response.headers.items())
    
    except requests.exceptions.RequestException as e:
        # エラーが発生した場合の応答
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
