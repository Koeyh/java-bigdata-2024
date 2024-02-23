# file: p18_fileRead.py
# desc: 텍스트 파일 읽기

f = open('./day03/PFRO.log', mode='r', encoding='utf-8')
f2 = open('./dest.txt', mode='w', encoding='utf-8')

read = f.readlines()
print('파일에서 읽은 내용 > ', read)

while True:
    read = f.readline()
    if not read : break
    print(read.replace('\n', ''))

f.close()
#f2.close()