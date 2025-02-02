import sys 
import os 
import json 
import subprocess 
from PyQt5.QtWidgets import QApplication, QMainWindow 
from PyQt5.QtWebEngineWidgets import QWebEngineView 
from PyQt5.QtCore import QUrl, QTimer, Qt 
from PyQt5 import QtGui
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ウェブエンジンビューを初期化
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)

        #ウィンドウの情報を取得
        with open('ada.json', 'r', encoding='utf-8') as file: 
          data = json.load(file)
          windtitle = data['title']
          windresizex = data['x']
          windresizey = data['y']
          mintl = data['deta']
        # ウィンドウタイトルを設定
        self.setWindowTitle(windtitle)   
        self.resize(windresizex, windresizey)  # ウィンドウサイズの設定
        icon_path = os.path.join(os.getcwd(), 'icon.ico') # 同階層のアイコンを参照 
        self.setWindowIcon(QtGui.QIcon(icon_path))
        self.show()  # 先にUIを表示する
        if mintl=="info":
                pass
        else:
                batch_file = mintl  # バッチファイルを実行 
                result = subprocess.run(batch_file, capture_output=True, text=True, shell=True)
    

    def load_url(self, start_url):
        # タイマーを使用してURLを読み込む
        QTimer.singleShot(1, lambda: self.browser.setUrl(QUrl(start_url)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 現在の作業ディレクトリを取得 
    current_directory = os.getcwd() # 現在の作業ディレクトリを取得  
    # www/index.htmlへの絶対パスを生成 
    start_url = QUrl.fromLocalFile(os.path.join(current_directory, 'www', 'index.html')) # 絶対パスを生成
    window = Browser()  # 初期化しただけのブラウザを作成
    window.load_url(start_url)  # ここで初めてURLを読み込む
    sys.exit(app.exec_())
