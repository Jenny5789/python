'''
### 1. 기본 구조 - 모든 GUI의 출발점###

##첫 번째 창 만들어보기##
# src/chapter2/01_basic_window.py
import tkinter as tk

# 1단계 : 기본 창 만들기
root = tk.Tk()
root.title("내 첫 번째 GUI 프로그램")  #창 제목 설정
root.geometry("300x200")   #창 크기 설정(가로 x 세로)

# 2단계: 창 보여주기
root.mainloop()


## 창 설정 옵션##
import tkinter as tk

root = tk.Tk()
root.title("창 설정 연습")      #제목
root.geometry("300x200")        #크기
root.resizable(True, False)     #창 크기 조절(가로, 세로) 
root.minsize(200, 100)          #최소크기
root.maxsize(800, 600)          #최대크기
root.configure(bg="lightblue")  #배경색

root.mainloop()

'''



### 2. 텍스트 요소들 - 정보를 보여주고 받기###
##Label - 텍스트와 이미지 표시##
import tkinter as tk

root = tk.Tk()
root.title("Lable 연습")
root.geometry("500x400")
root.configure(bg= "white")

## 기본 라벨
basic_label = tk.Label(root, text = "안녕하세요! 이것은 기본 라벨입니다.")
basic_label.pack(pady=10)

#스타일이 적용된 라벨
styled_label = tk.Label(
    root,
    text="예쁘게 꾸민 라벨",
    font=("맑은고딕", 16, "bold"),   #폰트 설정
    fg="blue",                       #글자색
    bg="lightyellow",                #배경색
    width=20,                        #너비(글자 수)
    height=2                         #높이(줄 수)
)
styled_label.pack(pady=10)

# 여러 줄 라벨
multiline_label = tk.Label(
    root,
    text="여러 줄로 된 라벨입니다. \n두 번째 줄\n세 번째 줄",
    font=("맑은고딕", 12),
    justify=tk.LEFT,                   #텍스트 정렬
    bg="lightgreen"
)
multiline_label.pack(pady=10)

root.mainloop()