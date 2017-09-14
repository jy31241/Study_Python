import urllib
import urllib2 #이 모듈을 잘쓰면 넘나 좋자냐

#요청값
url = ""
values = {'임의값': '' ,'임의값2': ''}# 바디영역에 들어갈 파라메타 벨류 정해줘여~
headers = {'User-Agent': 'Mozilla/4.0(compatible;MISE 5.5; Windows NT)'}
data = urllib.urlencode(values)#POST값 인코딩

#모듈 써서 리퀘스트 데이터 넣어주고
request = urllib2.Request(url, data, headers)
reponse = urllib2.urlopen(request)#호출

print("주소:%s" % reponse.geturl())
print("코드:%s" % reponse.getcode())
print("정보:%s" % reponse.info())
print("데이터:%s" % reponse.read())



