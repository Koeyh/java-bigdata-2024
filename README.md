# 빅데이터 언어 2024 
빅데이터 자바 개발자 파이썬 학습 리포티토리

## 1일차
- 파이썬 개발 환경 설정
    - [깃헙]( https://github.com/) 가입
    - [깃](https://git-scm.com/download/win) 설치
    - [깃헙 데스크탑](https://desktop.github.com/) 설치
    - [파이썬](https://python.org) 설치
    - [Visual Studio Code](https://code.visualstudio.com/download) 설치
    - [나눔 고딕 코딩 글자체](https://github.com/naver/nanumfont) 설치

- 파이썬 학습
    - 파이썬 개요
        - 1990년 네덜란드 "귀도 반 로섬" 개발
        - 쉽고 간결한 문법, 무료, 빠른 개발속도
    - 파이썬 기초 문법
        - 숫자형(정수, 실수, 진수)
        ```Python  # '`' 백택 세개 사용 시 코드 첨부 가능
        ```
        # 변수만 선언, 값만 할당하면 숫자형으로 지정
        # C, C++, Java, C# 처럼 형 지정이 없음
        val = 10 #정수형
        val = 2.15 #실수형

        # 특수 숫자형
        binVal = 0b11111111 #255 (2진수)
        octVal = 0o11 # 9, (8진수)
        hexVal = 0xFF # 65, (16진수)

        - 문자열(특수 형태의 리스트)형(연산, 문자열 포맷, 함수)
            # '', "" 모두 사용 가능
        - 리스트형, 튜플형(연산, 함수)
            - 리스트 :  수정, 삭제 가능
            - 튜플 : 수정, 삭제 불가
            - 수정, 삭제 이외는 서로 동일

            
## 2일차
- 파이썬 학습
    - 파이썬 기초문법
        - 딕셔너리, 집합
        - 부울형
        - None형
        - 제어문(if, for, while)
        - 제어문 연습
        - 함수

## 3일차
- 파이썬 학습
    - 파이썬 기초문법
        - 입출력
        - 객체지향
        - 모듈 / 패키지
        - 예외처리 / 디버깅

## 4일차
- 파이썬 학습
    - 파이썬 기초문법
        - 모듈 / 패키지
        - ★★예외처리, 디버깅 : 디버깅 하면서 예외를 찾아 예외처리 진행
        - 내장 함수

        
## 5일차
- 파이썬 학습
    - 파이썬 응용
        - OS내 디렉토리 검색
        - 아스키 및 유니코드
        - 주소록 앱 만들기

        ```python
        class Contact: # 주소록 클래스
    
        def __init__(self, name, phoneNumber, eMail, addr) -> None: # 생성자
        self.__name = name
        self.__phoneNumber = phoneNumber
        self.__eMail = eMail
        self.__addr = addr

         # 사용자가 원하는 형태로 출력
         def __str__(self) -> str: # 원래출력 <__main__.Contact object at 0x0000024500772150> 
            res = (f'이  름 : {self.__name}\n'
                f'핸드폰 : {self.__phoneNumber}\n'
                f'이메일 : {self.__eMail}\n'
                f'주  소 : {self.__addr}')
            return res

            # 연락처 여부확인
        def isNameExist(self,name):
              if self.__name==name: #찾는 이름 존재
                return True
            else:
                return False
                
            def getInfo(self):
                return self.__name,self.__phoneNumber,self.__eMail,self.__addr

        def setContact(): # 사용자 입력으로 주소록 받기함수
            (name, phoneNumber, eMail, addr) = input('입력(이름,핸드폰,이메일,주소[/])> ').split('/')
            name = name.strip() # 사용자실수로 들어간 스페이스 제거
            phoneNumber = phoneNumber.strip()
            eMail = eMail.strip()
            addr = addr.strip()
            # print(f'"{name}", "{phoneNumber}", "{eMail}", "{addr}"')
            contact = Contact(name, phoneNumber, eMail, addr) # 매개변수명과 동일하게 로컬변수 이름 지정
            return contact

        def delContact(lst, name): #연락처 삭제함수
            for i, item in enumerate(lst):
                if item.isNameExist(name):
                    del lst[i]

        def saveContact(lst): #연락처 저장함수
            with open(file= './contacts.txt', mode='w',encoding='utf-8') as fp:
                for item in lst:
                    name,phoneNumber,eMail,addr = item.getInfo()
                    fp.write(f'{name}/{phoneNumber}/{eMail}/{addr}\n')
                    
        def loadContact(lst): #처음 실행시 연락처 로드함수
            try:
                with open('./contacts.txt', mode='r', encoding='utf-8') as fp:
                    while True:
                        line = fp.readline()
                        if not line: break

                        lines = line.replace('\n','').split('/') #list
                        contact = Contact(name=lines[0],phoneNumber=lines[1],eMail=lines[2],addr=lines[3])
                        lst.append(contact)
            except: # 연락처 파일이 없으면 새로 만들어줌
                f = open('./day05/contacts.txt', mode='r', encoding='utf-8')
                f.close()

        def displayMenu():
            menu = ('주소록 프로그램\n'
                    '1. 연락처 추가\n'
                    '2. 연락처 출력\n'
                    '3. 연락처 삭제\n'
                    '4. 종료\n')
            print(menu)
            try:
                sel = int(input('메뉴입력 : '))
            except: # 1~4가 아닌 잘못된 문자 입력 시 예외처리
                sel = 0

            return sel

        def clearConsole():
            cmd = 'clear' # macOS, Linux, Unix 명령어
            if os.name in ('nt', 'dos'): # window
                cmd = 'cls' # window 명령어

            os.system(cmd) # 명령어 실행

        def getContacts(lst): # 리스트를 받아서 출력함수
            for i, item in enumerate(lst):
                print(f'{i+1}==========>')
                print(item)

        def run():
            # 연락처담을 주소록 리스트
            lstContact = []
            loadContact(lstContact) #연락처 로드

            clearConsole() # 화면을 클리어
            while True:
                selMenu = displayMenu()

                if selMenu == 1: # 연락처 추가라면
                    clearConsole()
                    try:
                        contact = setContact()
                    except: # 시키는대로 입력하지 않을 시
                        contact = None

                    if contact != None:
                        lstContact.append(contact)
                        input('입력 성공!')
                    else:
                        input('입력 실패')
                    clearConsole() # 엔터 입력유도            
                elif selMenu == 2: # 연락처 출력
                    clearConsole()
                    getContacts(lstContact)
                    input(); clearConsole()
                elif selMenu == 3: # 연락처 삭제
                    clearConsole()
                    name=input('삭제할 이름 입력 : ')
                    delContact(lstContact, name)
                    input(); clearConsole()
                elif selMenu == 4:
                    saveContact(lstContact)
                    break
                else:
                    clearConsole() 

        ```

        ![주소록앱](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata01.gif)

        - Windows App 만들기()

        ![QtApp](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata02.png)
        

        

## 6일차 ('24. 2. 28.)
- 파이썬 학습
    - PyQt5 학습 이어하기
        - QWidget 자식 클래스 종류 학습
        
        ![QLabel](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata03.png)

        - Naver 뉴스 API 검색 앱

        ![QLabel](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata04.png)


## 7일차
- 파이썬 학습
    - PyQt5 계속
        - Naver 뉴스 API 검색 앱 마무리
    - json 학습 
    - PyQt5
        - 스레드 개념, 학습
        - 스레드 활용
        ![스레드](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata05.png)

        - QR코드 제작 APP
        ![QR](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata06.png)

        - 구글 번역 APP
        ![구글번역](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata07.png)

        
## 8일차
- 파이썬 응용
    
    - pyAutoGui 모듈(마우스, 키보드, 화면캡처)
    - 슬랙 webhook로 모바일 메시지 전송

    <!-- ![슬랙](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata08.jpg) -->
    <!-- html 태그로 이미지를 삽입하면 문제없음 -->
    <img src ="https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata08.jpg" width="250">

    - Tesseract 프로그램으로 이미지에서 글자 추출(인식률 높이려면 직접 트레이닝을 해서 트레이닝 데이터를 만들어야 함)

    ![OCR](https://raw.githubusercontent.com/Koeyh/java-bigdata-2024/main/images/bigdata09.png)
    
## 9일차
- 파이썬 응용
    - 이미지 처리 OpenCV
    - 플라스크 웹서버
    - 그림에디터 만들기
    - 메모장 만들기
    - Jupyter Notebook 사용법(빅데이터 분석, 코딩테스트)


## 10일차
