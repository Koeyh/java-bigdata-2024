# file: p31_externalLib.py
# desc: 외부 라이브러리 사용법

# > pip install LibName(라이브러리 명) # 설치
# Successfully installed / Requirement already satisfied가 나와야 함.
# > pip uninstall LibName # 삭제
# Successfully uninstalled 나와야 함.

# from faker import Faker

# fake = Faker('ko-KR') # 한국어 설정
# print(fake.name())
# print(fake.address())
# # print(fake.phone_number())
# # print(fake.profile())]

# dummyData = [fake.profile() for i in range(10)]
# print(dummyData)



#요청(request) > 응답(response)
# from urllib.request import Request, urlopen

# req = Request('https://naver.com')
# res = urlopen(req)

# print(res.status)
# print(res.read())

## urllib3 외부 웹페이지 분석 모듈
#import requests

res = requests.get('https://www.naver.com')
print(res.status_code)

# import sys

# print(sys.path)
