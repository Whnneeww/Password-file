from smbserver import SMBServer 
from pyftpdlib.authorizers 
import DummyAuthorizer from pyftpdlib.handlers 
import FTPHandler from pyftpdlib.servers 
import FTPServer 
import threading  
storage_path = "./storage" 
def start_smb_server():
  smb_server = SMBServer()  
  smb_server.add_share('storage', storage_path)  
  smb_server.start('0.0.0.0', 2556)  
  print("SMBサーバーが起動しました。")  
  def start_ftp_server(): 
    authorizer = DummyAuthorizer() 
    authorizer.add_user("user", "12345", storage_path, perm="elradfmwMT") 
    authorizer.add_anonymous(storage_path)   
    handler = FTPHandler  
    handler.authorizer = authorizer  
    server = FTPServer(("0.0.0.0", 2557), handler) 
    server.serve_forever()  print("FTPサーバーが起動しました。")  
    if __name__ == "__main__": 
      smb_thread = threading.Thread(target=start_smb_server)  
      ftp_thread = threading.Thread(target=start_ftp_server)   
      smb_thread.start()  
      ftp_thread.start()   
      smb_thread.join()  
      ftp_thread.join()
