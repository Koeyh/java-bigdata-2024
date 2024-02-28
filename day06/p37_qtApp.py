# file: p37_qtApp.py
# desc: pyQt5 앱 만들기
'''
설치 > pip install PyQt5
시그널 == 이벤트 / 위젯 == 컨트롤
메시지 박스, 이벤트에 따른 메시지박스 생성
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow, QPushButton

class qtApp(QWidget): # QWidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self)-> None: 
        super().__init__() # 생성자, 부모 클래스의 생성자 함수도 실행되어야 한다
        self.initUI()

    def initUI(self):
        self.setGeometry((1920-300)//2, (1080-300)//2, 320, 230) # 해상도 1920*1080에서 정중앙에 위치
        self.setWindowTitle('세번째 Qt 앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 화면 UI에서 추가/변경할 것
        btn1 = QPushButton('클릭', self)
        btn1.setGeometry(210, 180, 100, 40)
        btn1.clicked.connect(self.btn1Clicked) # 버튼 클릭 시그널이 발생하면 이를 처리하는 함수 연결

        self.show() # 윈도우 창 그리기

    def btn1Clicked(self):
        QMessageBox.about(self, '버튼 클릭','버튼을 눌렀습니다.')

    def closeEvent(self, QCloseEvent) -> None: # 원하는 방식으로 오버라이드 실행
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



app = QApplication(sys.argv)  
inst = qtApp()
app.exec_()