# file: p17_fileIo.py
# desc: 파일 입출력 학습

# 컴퓨터에서 열면 반드시 닫아야 하는 것
# 1. 파일 open(), close() / 파이썬에서는 닫지 않아도 크게 지장없음
# 2. 통신(네트워크) open(), close()
# 3. DB connect(), close()

# w, r, a / 쓰기, 읽기, 추가(수정)
# 언어체계 추가 ASCII(한글, cp949), 유니코드(utf-8)
# 상대경로, 절대경로
# 'w'는 매번 새로 파일생성, 'a'는 기존 내용에 추가
# 로그 등을 남길땐 'a'로 작업해야

f = open('./sample.txt', mode='a', encoding='utf-8')
# 파일쓰기 실행
f.write('안녕하세요. 파이썬.\n')
f.write('화이팅\n')

f.close() # 파이썬에서만 옵션, 다른 언어에서는 필수적인 사항 