# 암호해제 앱 (무차별대입공격), zip파일에 적용되어 있는 비밀번호를 찾는데 사용할 수 있움
import itertools
import time
import zipfile

#passwd_string= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' # 패스워드에 영문자도 들어 있으면 이걸 사용
#특수문자까지 있으면 답없음
passwd_string= '0123456789'# 비밀번호에 사용된 문자열
file = zipfile.ZipFile('./studyPython/passwordZip.zip') # 비밀번호를 풀 대상 파일
isFind = False # 암호를 찾았는지

for i in range(1, 5):# 범위를 1에서 5로 해놓으면 비번 자릿수는 4자릿수
    attempts = itertools.product(passwd_string, repeat = i)
    for attempt in attempts:
        try_pass = ''.join(attempt)
        print(try_pass)
        #time.sleep(0.005) # 사실 이건 필요 없음
        try:
            file.extractall(pwd=try_pass.encode(encoding = 'utf-8'))
            print(f'암호는 {try_pass} 입니다.')
            isFind = True; break
        except:
            pass
    if isFind == True : break