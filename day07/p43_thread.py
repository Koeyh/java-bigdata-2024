# file : p43_thread.py
# desc : 스레드 기본

from threading import Thread, current_thread
import time

class BackgroundWorker(Thread):
    def __init__(self, name) -> None:
        super().__init__(name = name)
        self._name = f'{current_thread().getName()} : {name}'

    def run(self) -> None:
        print(f'백그라운드워커 시작 : {self._name}')
        time.sleep(3)
        print(f'백그라운드워커 종료 : {self._name}')

print('메인 스레드 시작')
for i in range(5):
    name = f'서브 스레드 {i}'
    th = BackgroundWorker(name)
    th.start() # run이 실행됨

print('메인 스레드 종료')    