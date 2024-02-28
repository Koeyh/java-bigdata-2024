# file : naverSearch.py
# desc : 네이버 검색 API용 클래스

import json # 학습 필요
from urllib.request import Request, urlopen
import datetime
from urllib.parse import quote # 글자를 유니코드(utf-8)로 인코딩 하는 함수
import ssl




class NaverSearch:
    def __init__(self) -> None:
        print('naver API 클래스 생성')

    # URL로 검색 시작하는 함수
    def getRequestUrl(self, url): # 클래스 내에서 사용할 함수
        ssl._create_default_https_context = ssl._create_unverified_context
        req = Request(url)
        req.add_header('X-Naver-Client-Id', 'kSExTarYF0NKI9reCrrE') # 자신의 애플리케이션 클라이언트 ID 입력
        req.add_header('X-Naver-Client-Secret', 'amJSX8mtyK') # 해당 클라이언트 Secret

        try:
            res = urlopen(req)
            if res.status == 200:
                print(f'[{datetime.datetime.now()}] : URL 요청 성공')
                return res.read().decode('utf-8')
        except Exception as e:
            print(f'[{datetime.datetime.noew()}] : URL 요청 오류 ! {e.args}')
            return None # 예외 발생 시 반환값 없음

    # 실제 동작 함수
    def getSearchResult(self, searchWord): #https://openapi.naver.com/v1/search/news
        baseUrl = 'https://openapi.naver.com/v1/search/news.json'
        params = f'?query={quote(searchWord)}&start=1&display=20'
        finalUrl = baseUrl + params
        result = self.getRequestUrl(finalUrl)
        if result != None: # 예외가 발생하지 않을 때
            return json.loads(result)
        else:
            return None
    