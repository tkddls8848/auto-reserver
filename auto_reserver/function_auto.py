import pyautogui ## 파이썬 자동 키보드 및 마우스 제어
import time ## 실행 타이머
import pyperclip ## 문자 복사 붙여넣기


SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
## 1920 1080 기준
SEARCH_WIDTH, SEARCH_HEIGHT = 1190, 220
KEY_LIST = pyautogui.KEYBOARD_KEYS

# 자동 명령 실행 함수
def run_auto():
    
    # 문자 입력 후 엔터키 기능
    def write_and_enter(s):
        pyautogui.typewrite(s)
        pyautogui.keyDown("enter")
        time.sleep(2)

    # pyautogui.hotkey : 단축키
    # pyautogui.keyDown : 키 누르기
    # pyautogui.moveTo : 해당 픽셀로 이동(x,y,이동시간)
    pyautogui.hotkey("win")
    write_and_enter("chrome")
    pyautogui.hotkey("ctrl", "l")
    pyperclip.copy("naver.com")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.keyDown("enter")
    time.sleep(2)
    write_and_enter("Hello World")
    pyautogui.moveTo(SEARCH_WIDTH, SEARCH_HEIGHT, 0.1)
    pyautogui.doubleClick()
    time.sleep(2)
    
    # 종료
    pyautogui.hotkey('ctrl', 'F4')
    # 화면 가로 세로 해상도를 콘솔에 출력
    print(SCREEN_WIDTH, SCREEN_HEIGHT)
