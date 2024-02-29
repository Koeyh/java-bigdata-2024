# file : p42_jsonHandle.py
# desc : json 읽고 쓰기

import json

# file 읽어서 쓸 객체변수 f, file, fp
# with문으로 작업하면 fp.close() 불필요
with open('./day07/p40_testData.json', mode='r', encoding='utf-8') as fp:
    data = json.load(fp)

# data로 출력 -> 파이썬 딕셔너리 출력 / json.dumps(data) -> json형태로 출력 / indent='\t'는 보기좋게 출력
print(json.dumps(data, indent='\t'))

#json 데이터 접근은 파이썬 딕셔너리와 동일
print(data['name'])
print(data['freinds'][1]) # 


## 쓰기
# 딕셔너리를 만들고, json으로 dump후 저장
superCars = dict() # 딕셔너리 생성
Audi = dict()
Audi['price'] = 80_000_000
Audi['year'] = '2020'
Audi['type'] = 'sports'
superCars['Audi'] = Audi

Porsche = dict()
Porsche['price'] = 160_000_000
Porsche['year'] = '2022'
Porsche['type'] = 'SUV'
superCars['Porsche'] = Porsche

# json 파일 저장
with open('./day07/superCars.json', mode='w', encoding='utf-8') as fp:
    json.dump(superCars, fp, indent='\t', ensure_ascii=True) # dumps : dump후 문자열로 변경
