import http.server import socketserver # ホストとポート番号の設定 
HOST = "0.0.0.0" 
PORT = 2855 
DIRECTORY = "storage"  
class CustomHandler(http.server.SimpleHTTPRequestHandler): 
def translate_path(self, path):  
  # リクエストによるパスを変更し、storageフォルダを公開する 
  path = super().translate_path(path) 
  return DIRECTORY + path  
  # サーバーの設定 
handler = CustomHandler 
with socketserver.TCPServer((HOST, PORT), handler) 
as httpd:
  print(f"サーバーが {HOST} のポート {PORT} で起動しました。")
  httpd.serve_forever()
