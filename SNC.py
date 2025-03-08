import logging 
from dnslib import DNSRecord, DNSHeader, DNSQuestion, RR, A 
from socketserver import UDPServer, BaseRequestHandler  
# ロギングの設定 
logging.basicConfig(level=logging.INFO)  
class DNSHandler(BaseRequestHandler): 
  def handle(self): 
    data = self.request[0] 
    socket = self.request[1]  # DNSリクエストのパース 
    request = DNSRecord.parse(data)  # クエリを表示 
    logging.info(f"Received query for {request.q.qname} ({request.q.qtype})")  # DNSレスポンスの作成 
    response = DNSRecord(DNSHeader(id=request.header.id, qr=1, aa=1), q=request.q)  # 特殊ドメインの名前解決処理 
    if str(request.q.qname) == "example.onion.": 
        response.add_answer(RR(rname=request.q.qname, rtype=A, rclass=1, ttl=60, rdata=A("127.0.0.1"))) 
        logging.info("Resolution: example.onion -> 127.0.0.1") 
    else: 
        # 一般的な応答（例が存在しない場合） 
        response.header.rcode = 3 # NXDOMAIN  # レスポンスの送信 
socket.sendto(response.pack(), self.client_address)  
if __name__ == "__main__": # UDPサーバーをローカルネットワークに開放（すべてのインターフェース） 
    server = UDPServer(('0.0.0.0', 2554), DNSHandler) # バインドアドレスを'0.0.0.0'に変更 
    logging.info("Starting DNS server on 0.0.0.0:2554") 
    server.serve_forever()
