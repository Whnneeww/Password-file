from flask import Flask, request, Response
import requests

app = Flask(__name__)
target_url = "https://sitedeta.i-i.f5.si"

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def forward_request(path):
    # 元のリクエストのメソッドとデータを保持する
    method = request.method
    data = request.get_data()
    headers = {key: value for key, value in request.headers}

    # target_urlにリクエストを送信
    response = requests.request(method, f"{target_url}/{path}", data=data, headers=headers)

    # 応答をそのまま返す
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == '__main__':
    app.run(debug=True)
