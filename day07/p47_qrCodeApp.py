# file : p47_qrCodeApp.py
# desc : PyQt QR코드앱
# pip install qrcode

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow, QPushButton
import qrcode

class qtApp(QWidget): 
    def __init__(self)-> None: 
        super().__init__()
        self.initUI()

    def initUI(self): # UI파일 로드해서 화면 디자인 사용
        uic.loadUi('./day07/qrApp.ui', self)
        self.setWindowTitle('QR코드 생성기')
        self.setWindowIcon(QIcon('./images/qrCode.png'))
        # 버튼 시그널 처리
        self.btnGenerate.clicked.connect(self.btnGenerateClicked) # ui파일내 위젯은 자동완성 X

        self.show() 


    def btnGenerateClicked(self):
       data = self.txtQrData.text()
        # 예외 점검
       if len(data.strip()) == 0:
           QMessageBox.about(self, '경고', '데이터를 입력하시오')
           return
       else:
           imgPath = ('./day07/qr.png')
           qrImage = qrcode.make(data)
           qrImage.save(imgPath)
           img = QPixmap(imgPath)
           self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(300))

    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



app = QApplication(sys.argv)  
inst = qtApp()
app.exec_()