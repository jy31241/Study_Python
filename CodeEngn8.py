def CodeAd8_1(a):#첫글자
    a*=0x772
    c=a
    a*=a
    c+=a
    c*=0x474
    c+=c
    return c
def CodeAd8_2(b,res):#두번째글자 + 첫번째 결과값
    a=res+b
    a*=0x772
    c=a
    a*=a
    c+=a
    c*=0x474
    c+=c
    return c

for i in range(0x30,0x7A,0x01):
    result=CodeAd8_1(i)
    for j in range(0x30,0x7A,0x01):
        print('='*20)
        print("첫글자:",hex(i),"=",chr(i))
        result2=CodeAd8_2(j,result)
        h = hex(result2)
        print("두번째글자:",hex(j),"=",chr(j))
        print("16진수 연산값:",h)








