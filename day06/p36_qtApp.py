# file: p36_qtApp.py
# desc: pyQt5 앱 만들기
'''
PyQt : Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt   : C, C++에서 사용하는 GUI 프레임워크(멀티 플랫폼)

설치 > pip install PyQt5

'''

import sys
# QApplication 만들 앱 전체 관리 클래스, QWidget 메뉴가 없는 윈도우 앱, QMainWindow 메뉴가 있는 윈도우 앱
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
#QMainWindow, QLabel, QPushButton 등은 QWidget을 상속한 자식 클래스(부모 클래스의 기능들을 모두 사용할 수 있음)
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow, QPushButton

class qtApp(QWidget): # QWidget이 가지고 있는 속성, 변수, 함수를 다 사용가능
    def __init__(self)-> None: 
        super().__init__() # 생성자, 부모 클래스의 생성자 함수도 실행되어야 한다
        self.initUI()

    def initUI(self):
        label = QLabel() # 라벨위젯(Qt) == 라벨컨트롤(MFC, C#, Java Fx, Android)

        self.setGeometry(300, 200, 800, 400) #바탕화면 정해진 위치에 넓이와 높이로 그릴지 설정 x, y, w, z
        self.setWindowTitle('두번째 Qt 앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        self.text = '빵빵아 !'
        label.setText(self.text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet(('color: red;'
                             'background-color: black;')) # 라벨의 색상 스타일 설정 html, css와 동일


        font = label.font()
        font.setFamily('Bauhaus 93')
        font.setPointSize(40)

        label.setFont(font)

        layout= QVBoxLayout()
        layout.addWidget(label)

        self.setLayout(layout)

        self.show() # 윈도우 창 그리기

    def paintEvent(self, event) -> None:
        paint = QPainter() # 윈도우 창 위에 그림 그리는 객체
        paint.begin(self) # 그림을 그리기 시작하면
        paint.setPen(QColor(200, 0, 0)) # 색상, RGB / R 200
        paint.setFont(QFont('Bauhaus 93', 40)) # '폰트명', 폰트 사이즈
        paint.drawText(250, 400//2, 'Hello PyQt!') # 글자 위치(x,y축), 출력할 텍스트 입력
        paint.end() # 반드시 끝에 닫아줘야 함
    
app = QApplication(sys.argv) # 
inst = qtApp() # 객체 생성
app.exec_() # 실제 실행
