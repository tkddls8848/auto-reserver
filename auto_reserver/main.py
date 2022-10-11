from tkinter import Tk, Button, ttk # 파이썬 GUI 모듈
import function_auto # run_auto 함수를 불러오기 위한 import

#버튼 기능 구현
def button_text():
    s = "Search End"
    btn.config(text=s)
    # function_auto.py의 run_auto()
    function_auto.run_auto()

#GUI 박스
window = Tk()
window.geometry("800x400")
window.title("검색기")
#GUI 박스 내 텍스트(Label), 라디오버튼(Radiobutton), 버튼(Button) 객체 구현
label = ttk.Label(window, text="해상도 1920 x 1080 필수")
action = ttk.Radiobutton(window, text="1", value=1)
action1 = ttk.Radiobutton(window, text="2", value=2)
btn = Button(window, text="Search Start!!", width="50", command=button_text)
label1 = ttk.Label(window, text="Developed by PSI")
#GUI 구현된 객체를 박스내 배치
label.grid(column=0, row=0)
action.grid(column=1, row=1)
action1.grid(column=2, row=1)
btn.grid(column=0, row=2)
label1.grid(column=0, row=8)
#GUI 실행
window.mainloop()
