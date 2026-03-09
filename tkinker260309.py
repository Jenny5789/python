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