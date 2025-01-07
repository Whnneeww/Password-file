from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy', methods=['GET'])
def proxy():
    # sitedeta.i-i.f5.siへのリクエストを送信
    response = requests.get('https://sitedeta.i-i.f5.si')
    
    # 元の応答をそのまま返す
    return (response.content, response.status_code, response.headers.items())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
