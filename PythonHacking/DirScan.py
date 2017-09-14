from ftplib import FTP

directory = "dir"
serverName = 'name'
serverId = "pjya0"
serverPw = "qwer"

#서버에서 디렉터리 목록을 가져옴
def getDirList(ftp, name):
    dirList = []
    if("." not in name): #파일 확장자에 들어가는 쩜이 있으면 파일로 간주
        if(len(name)==0):
            dirList = ftp.nlst()
        else:
            dirList = ftp.nlst(name)
        return dirList

def checkDir(dir1, dir2):
    if(dir1.lower().find(directory)>=0):
        print(dir1)
    if(dir2.lower().find(directory)>=0):
        print(dir1+"/"+dir2)

ftp = FTP(serverName,serverId,serverPw)#ftp로긴
dirList1 = getDirList(ftp,"")

for name1 in dirList1:
    checkDir(name1,"")
    dirList2 = getDirList(ftp,name1)
    for name2 in dirList2:
        checkDir(name1,name2)
        dirList3 = getDirList(ftp,name1+"/"+name2)

