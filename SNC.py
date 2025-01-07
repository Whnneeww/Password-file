from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET'])
def forward_request(path):
    # sitedeta.i-i.f5.siへのリクエストを送信
    response = requests.get(f"https://sitedeta.i-i.f5.si/{path}")
    
    # 元の応答をそのまま返す
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

@app.route('/', methods=['GET'])
def root_request():
    # /へのリクエストもsitedeta.i-i.f5.siにリダイレクトする
    return forward_request('')  # 空のパスを渡すことでリクエストを転送

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
