# file : p44_nothreadApp.py
# desc : PyQt5 스레드 학습용(스레드 사용안함)


import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow, QPushButton

class qtApp(QWidget): 
    def __init__(self)-> None: 
        super().__init__()
        self.initUI()

    def initUI(self): # UI파일 로드해서 화면 디자인 사용
        uic.loadUi('./day07/testthread.ui', self)
        self.setWindowTitle('No Thread App')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일내 위젯은 자동완성 X

        self.show() 


    def btnStartClicked(self):
        self.pgbTask.setValue(0) # 재설정(확인)
        self.pgbTask.setRange(0, 999_999) # 프로그레스바 범위 설정
        self.btnStart.setDisabled(True)
        # UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)
        for i in range(0, 1_000_000): # 0 ~ 999,999
            print(f'No Thread 진행 >> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'No Thread 진행 >> {i}')
        
        self.btnStart.setEnabled(True)

    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



app = QApplication(sys.argv)  
inst = qtApp()
app.exec_()