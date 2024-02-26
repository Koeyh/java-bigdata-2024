# file: p26_exceptionHandle.py
# desc: 예외처리
# 오류(Error) : 코드상에 빨간색(노란색) 밑줄이 그어지는 것
# 예외(Exception) : 프로그램 실행 중에 생기는 오류(비정상정 종료)


try:
    f = open('./sanple.txt', mode='r', encoding= 'utf-8')
    res = f.readline()
    print(res)
    
except:
    print('파일오픈 예외발생!')
finally: # 예외 발생의 유무와 상관없이 파일 close
    try: # try~except는 다중으로 사용할 시 성능이 저하된다.
        f.close()
    except NameError as e:
        print('파일 오픈 실패 !')
#print(5/0)

try:
    print(5/0)
except:
    print('나누기 에러발생!')


a, b = 5, 3
if a == b:
    print(True)