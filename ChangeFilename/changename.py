import os


# 변경 함수
def changeFilename(filelist, size, change):
    number = 0

    print('-' * 50)
    for name in filelist:
        if name[-4:] == '.png':
            number += 1
            strnumber = str(number).zfill(size)
            newname = "새이름"+strnumber + '.png'
            if change:
                os.rename(path + name, path + newname)
            print(name, '->', newname)
    print('-' * 50)


# 프로그램 시작
while True:
    print("프로그램 종료를 원하면 'exit'를 입력하시오")

    path = input('경로를 입력해주세요(ex: D:/programing/) : ')

    if path == 'exit':  # exit입력하면 종료
        break
    elif path == "":  # 경로 입력안하면 디폴트값으로 디드라이브
        path = 'D:/'
    elif path[-1] != '/':
        path += '/'  # 마지막이 '/'로 안끝나면 삽입

    # 폴더에서 파일명 리스트가져오기
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except:
        print('경로를 확인해주세요.')
        continue

    # 파일 정보 확인하기
    go = input('해당 폴더의 파일이 맞나요? (y/n): ').lower()
    if go == 'n':
        continue
    elif go == 'q':
        break

    size = len(input('숫자부분의 자릿수에 맞춰 0을 넣어주세요: '))

    # 파일 변경 전 마지막 확인하기

    changeFilename(files, size, False)

    go = input('이대로 변경할까요? (y/n): ').lower()
    if go == 'n':
        continue
    elif go =='exit':
        break

    #파일 명 변경하기
    changeFilename(files, size, True)
    print('파일명 변경 완료')


    #재실행 / 종료
    ans = input('또 다른 파일명을 수정할까요?(y/n): ').lower()

    if ans=='y':
        continue
    else:
        print('-'*24 ,'종료', "-"*24)
        break

    #종료

