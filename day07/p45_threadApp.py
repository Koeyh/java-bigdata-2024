# file : p45_threadApp.py
# desc : PyQt5 스레드 학습용(스레드 안함)


import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * # QApplication, QWidget, QMainWindow, QPushButton

class BackgroundWorker(QThread):
    initUiSignal = pyqtSignal(int) # 스레드 진행 시 UI에서 초기화 부분을 시그널로 전달
    setPgbSignal = pyqtSignal(int) # 스레드 진행 시 변경되는 숫자를 UI 로 전달
    setTxbSignal = pyqtSignal(str) # 스레드 진행 시 화면에 출력될 문자열 UI쪽으로 전달

    def __init__(self,parent) -> None: # 부모는 qtApp 클래스
        super().__init__(parent)
        self.parent = parent

    def run(self) -> None:
        maxVal = 1_000_000
        self.initUiSignal.emit(maxVal) # UI(qtApp)에서 처리할 수 있게 값 전달

    
        for i in range(maxVal):
            print(f'스레드 진행 >> {i}')
            self.setPgbSignal.emit(i)
            self.setTxbSignal.emit(f'스레드 진행 >> {i}')
            # self.parent.pgbTask.setValue(i) # UI 스레드의 권한을 백그라운드 스레드에 주지 않음
            # self.parent.txbLog.append(f'스레드 진행 >> {i}') # 사용 불가



class qtApp(QWidget): 
    def __init__(self)-> None: 
        super().__init__()
        self.initUI()

    def initUI(self): # UI파일 로드해서 화면 디자인 사용
        uic.loadUi('./day07/testthread.ui', self)
        self.setWindowTitle('Thread App')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일내 위젯은 자동완성 X

        self.show() 


    def btnStartClicked(self):
        self.btnStart.setDisabled(True)
        th = BackgroundWorker(self)
        th.start() # 스레드 내의 run()함수 실행
        th.initUiSignal.connect(self.initPgbTask)
        th.setPgbSignal.connect(self.setPgbTask)
        th.setTxbSignal.connect(self.setTxbLog)

        self.btnStart.setEnabled(True)
    @pyqtSlot(str)
    def setTxbLog(self, msg):
        self.txbLog.append(msg)

    def setPgbTask(self, val):
        self.pgbTask.setValue(val)

    @pyqtSlot(int) # pyqtSignal에서 넘어온 값을 처리해주는 부분이라 선언
    def initPgbTask(self, maxVal):
        self.pgbTask.setValue(0)
        self.pgbTask.setRange(0, maxVal-1)


    def closeEvent(self, QCloseEvent) -> None: 
        re = QMessageBox.question(self, '종료 확인', '종료하시겠습니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()



app = QApplication(sys.argv)  
inst = qtApp()
app.exec_()