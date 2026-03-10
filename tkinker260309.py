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

# 동적으로 변하는 라벨
dynamic_var = tk.StringVar()
dynamic_var.set("변경 가능한 텍스트")

dynamic_label = tk.Label(
    root,
    textvariable=dynamic_var,           #StringVar 사용
    font=("맑은 고딕", 14),
    fg="red"
)
dynamic_label.pack(pady=10)

# 텍스트를 변경하는 버튼
def change_text():
    import random
    texts = ["안녕하세요!", "Hello!", "こんにちは!", "Bonjour!", "¡Hola!"]
    dynamic_var.set(random.choice(texts))

change_button = tk.Button(root, text="텍스트 변경", command=change_text)
change_button.pack(pady=10)


root.mainloop()





##Entry_ 한 줄 텍스트 입력
# 1단계: 기본 entry 만들기
import tkinter as tk

root = tk.Tk()
root.title("Entry 기본 사용법")
root.geometry("400x200")

#기본 입력창
tk.Label(root, text="이름을 입력하세요:", font=("맑은 고딕", 12)).pack(pady=10)
name_entry = tk.Entry(root, font=("맑은 고딕", 12), width=30)
name_entry.pack(pady=5)

#입력값 가져오기
def show_input():
    user_input = name_entry.get()    #Entry에서 텍스트 가져오기
    result_label.config(text=f"입력하신 내용: {user_input}")

tk.Button(root, text="입력값 확인", command=show_input).pack(pady=10)

result_label = tk.Label(root, text="", font=("맑은 고딕", 11), fg="blue")
result_label.pack()


root.mainloop()



# 2단계: 다양한 entry 스타일
import tkinter as tk

root = tk.Tk()
root.title("Entry 다양한 스타일")
root.geometry("500x300")

# 일반 텍스트 입력창
tk.Label(root, text="이름:", font=("맑은 고딕", 12)).pack(pady=5)
name_entry = tk.Entry(root, font=("맑은 고딕", 12), width=30)
name_entry.pack(pady=5)

# 비밀번호 입력창(별표로 숨김)
tk.Label(root, text="비밀번호:", font=("맑은 고딕", 12)).pack(pady=5)
name_entry =tk.Entry(root, font=("맑은 고딕", 12), width=30)
name_entry.pack(pady=5)

# 비밀번호 입력창 (별표로 숨김)
tk.Label(root, text="읽기 전용:", font=("맑은 고딕", 12)).pack(pady=5)
readonly_entry = tk.Entry(root, font=("맑은 고딕", 12), width=30, state="readonly")
readonly_entry.insert(0, "이 텍스트는 수정할 수 없습니다")
readonly_entry.pack(pady=5)

root.mainloop()





# 3단계: 입력값 검증과 처리
import tkinter as tk
import tkinter.messagebox as msgbox

root = tk.Tk()
root.title("Entry 입력과 검증")
root.geometry("500x400")

# 입력 필드들
tk.Label(root, text="이름:", font=("맑은 고딕", 12)).pack(pady=5)
name_entry = tk.Entry(root, font=("맑은 고딕", 12), width = 30)
name_entry.pack(pady=5)

tk.Label(root, text="나이 (숫자만):", font=("맑은 고딕", 12)).pack(pady=5)
age_entry = tk.Entry(root, font=("맑은 고딕", 12), width=30)
age_entry.pack(pady=5)

# 입력갑 처리 함수
def process_input():
    name = name_entry.get()
    age = age_entry.get()

    # 입력값 검증
    if not name:
        msgbox.showwarning("입력 오류", "이름을 입력해주세요!")
        return
    
    if age and not age.isdigit():
        msgbox.showerror("입력 오류", "나이는 숫자만 입력해주세요!")
        return
    
    # 결과 표시
    result = f"안녕하세요, {name}님!"
    if age:
        result += f"\n나이: {age}세"

    msgbox.showinfo("입력 결과", result)

# 버튼과 기능
tk.Button(root, text="입력 처리", command=process_input, font=("맑은 고딕", 12), bg="lightgreen").pack(pady=10)

def clear_all():
    name_entry.delete(0, tk.END)    #Entry 내용 지우기
    age_entry.delete(0, tk.END)

tk.Button(root, text="모두 지우기", command=clear_all, font=("맑은 고딕", 12), bg="lightcoral").pack(pady=5)

# Enter 키로 입력 처리
root.bind('<Return>', lambda event: process_input())

root.mainloop()




## Text - 여러 줄 텍스트 입력/표시
# 1단계 : 기본 Text 위젯
import tkinter as tk

root = tk.Tk()
root.title("Text 기본 사용법")
root.geometry("500x300")

tk.Label(root, text=" 여러 줄 텍스트 입력:", font = ("맑은 고딕", 12, "bold")).pack(pady=5)

# 기본 text 위젯
text_widget = tk.Text(
    root,
    height = 10,
    width = 50,
    font=("맑은 고딕", 11),
    wrap=tk.WORD,               #단어 단위로 줄바꿈
    bg="lightyellow"
)
text_widget.pack(pady=10)

# 초기 텍스트 넣기
text_widget.insert(tk.END, "여기에 여러 줄의 텍스트를 입력할 수 있습니다.\n")
text_widget.insert(tk.END, "Enter를 눌러서 줄을 바꿀 수 있습니다.\n")
text_widget.insert(tk.END, "Text 위젯은 긴 문서 작성에 적합합니다.")

root.mainloop()

'''

# 2단계: 스크롤이 있는 text
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title("스크롤 가능한 Text")
root.geometry("500x400")

tk.Label(root, text="스크롤 가능한 텍스트:", font=("맑은 고딕", 12, "bold")).pack(pady = 5)

# 스크롤바가 있는 text 위젯
text_area = scrolledtext.ScrolledText(
    root,
    height=15,
    width=60,
    font=("맑은 고딕", 11),
    wrap=tk.WORD
)
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


#많은 양의 텍스트 추가
for i in range(50):
    text_area.insert(tk.END, f"이것은 {i+1}번째 줄입니다. 스크롤해서 아래 내용을 확인해보세요!\n")

root.mainloop()



# 3단계: Text 조작 기능들
import tkinter as tk

root = tk.Tk()
root.title("Text 조작 기능")
root.geometry("600x400")

# text 위젯
text_widget = tk.Text(root, height=15, width=60, font=("맑은 고딕", 11))
text_widget.pack(padx=10, pady=10)

# 초기 텍스트


root.mainloop()