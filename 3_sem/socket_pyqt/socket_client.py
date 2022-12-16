from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import socket
from threading import Thread


class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(600, 300, 400, 300)
        self.setWindowTitle("Chat")
        palette = QtGui.QPalette()
        icon = QtGui.QPixmap(r'./img/1.jpg')
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))
        self.setPalette(palette)

        self.addUI()
        client = socket.socket()
        client.connect(('127.0.0.1', 9009))
        self.client = client
        self.begin_thread()


    def on_click(self):
        self.send_msg()
        self.text2.clear()

    def addUI(self):

        self.text = QTextBrowser(self)
        self.text.setGeometry(30, 30, 300, 100)
        self.text.setStyleSheet('QWidget{background-color:rgb(255,255,255,0%)}')

        self.text2 = QLineEdit(self)
        self.text2.setPlaceholderText(u'Text')
        self.text2.setGeometry(30, 160, 300, 30)
        self.text2.setStyleSheet('QWidget{background-color:rgb(255,255,255,0%)}')

        self.button = QPushButton('Submit', self)
        self.button.setFont(QFont('微软雅黑', 10, QFont.Bold))
        self.button.setGeometry(270, 220, 60, 30)

    def send(self):
        self.button.clicked.connect(self.on_click)

    def begin_thread(self):
        Thread(target=self.send).start()
        Thread(target=self.recv_msg).start()

    def send_msg(self):
        msg = self.text2.text()
        print(msg)
        self.client.send(msg.encode())
        if (msg.upper() == "QUIT"):
            self.client.close()
        self.text2.clear()

    def recv_msg(self):
        while 1:
            try:
                data = self.client.recv(1024).decode()
                data = data + "\n"
                self.text.append(data)
            except:
                exit()

    def closeEvent(self, QCloseEvent):
        self.client.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Login()
    dialog.show()
    sys.exit(app.exec())