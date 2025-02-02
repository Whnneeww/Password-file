import socket
import json  
# DNSサーバーのIPとポート 
HOST = '0.0.0.0' # すべてのインターフェースでリッスン 
PORT = 2559 FORWARD_DNS = '1.1.1.1' 
FORWARD_PORT = 53  # JSONファイルからDNSレコードを読み込む
with open('dns.json', 'r') as file:
  dns_records = json.load(file) 
  def create_response(transaction_id, question, record_type, record_info):
    response = bytearray() 
    response.extend(transaction_id) # トランザクションID 
response.extend(b'\x81\x80') # 標準のレスポンス 
response.extend(b'\x00\x01') # 質問数 
response.extend(b'\x00\x01') # 応答数 
response.extend(b'\x00\x00')# 権威数 
response.extend(b'\x00\x00')# 追加数  # 質問セクション
response.extend(question) # オリジナルのリクエストをそのまま 
response.extend(b'\xC0\x0C') # 指示名 (example.com)
response.extend(record_type) # タイプ (A, CNAME) 
response.extend(b'\x00\x01') # クラス (IN)
response.extend(socket.htons(record_info['ttl']).to_bytes(4, byteorder='big'))
# TTL  # レコードの追加 
if record_type == b'\x00\x01': # Aレコード 
  response.extend(socket.inet_aton(record_info['address'])) 
elif record_type == b'\x05': # CNAMEレコード 
  cname = record_info['address']
  response.extend(cname.encode('utf-8') + b'\x00') # CNAMEはNULL終端 
return response  
def forward_request(data):
  with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
  as forward_sock: 
    forward_sock.sendto(data, (FORWARD_DNS, FORWARD_PORT)) 
    return forward_sock.recv(512)
# 応答を待つ  
    def start_dns_server(): 
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
      sock.bind((HOST, PORT)) print(f"DNSサーバーがポート {PORT} で起動しました。")  
      while True: data, addr = sock.recvfrom(512) # DNSパケットの最大サイズは512バイト 
transaction_id = data[:2] question_start = 12 # 質問セクションの開始位置 
question_end = data.find(b'\x00', question_start) + 5 
question = data[question_start:question_end] 
qtype = data[question_end-4:question_end-2] # タイプ 
domain = question.decode('utf-8').rstrip('.')  # レコードの存在をチェック 
if domain in dns_records: record_info = dns_records[domain] 
  if qtype == b'\x00\x01' and 'CNAME' in record_info: 
    print("エラー: AレコードとCNAMEレコードが同時に設定されています。") continue 
    if qtype == b'\x05' and 'A' in record_info:
      print("エラー: CNAMEレコードとAレコードが同時に設定されています。") continue  
      if qtype in record_info:
        response = create_response(transaction_id, question, qtype, record_info[qtype]) 
      else:
        response = forward_request(data) # 外部DNSに問い合わせ 
      else:
        response = forward_request(data) # 外部DNSに問い合わせ  # レスポンスをクライアントに送信 
sock.sendto(response, addr)  if __name__ == "__main__": 
start_dns_server()
