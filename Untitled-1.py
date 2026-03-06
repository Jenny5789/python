###빈 다이얼로그(윈도우) 표시하기###

from tkinter import *

root = Tk()
root.mainloop()








###윈도우 창 설정###

# tk_windowsettings.py
from tkinter import *

root = Tk()

root.title("SISO")
root.geometry("300x200+100+100")
root.resizable(False, False)

root.mainloop()








### Label을 사용하여 Hello World 출력하기###
# tkinter로 hello world 출력하기
# filename : tk_helloworld.py
# coding : utf-8

#tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기
root = Tk()

# 레이블 생성
label = Label(root, text='Hello World')

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시
root.mainloop()






### tkinter 라이브러리 import###
from tkinter import *

# tk 객체 인스턴스 생성하기
root = Tk()
root.title("SISO")
root.geometry("300x200+100+100")
root.resizable(False, False)

# 레이블 생성
label = Label(root, text='Hello World')

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시
root.mainloop()








### Label를 사용하여 라벨의 속성을 설정###
# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기
root = Tk()
root.title("SISO")
root.geometry("300x200+100+100")
root.resizable(False, False)

## 레이블 생성 ##
label = Label(root, text="Hello World", width=10, height = 5, fg = 'red', relief="solid")

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시
root.mainloop()








### Label를 사용하여 라벨의 속성을 설정###
# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기
root = Tk()
root.title("SISO")
root.geometry("300x200+100+100")
root.resizable(False, False)

## 레이블 생성##
label = Label(root, text="Hello World", width = 100, height = 50, fg='red', relief = "solid", bitmap = "info", compound = "top")

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시
root.mainloop()







### Label를 사용하여 라벨의 속성을 설정###
# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기
root = Tk()
root.title("SISO")
root.geometry("300x200+100+100")
root.resizable(False, False)


##버튼 위젯을 사용하는 예제##
count = 0

def countplus():
    global count
    count += 1
    label.config(text=str(count))

def countminums():
    global count
    count -= 1
    label.config(text=str(count))

#레이블 생성
label = Label(root, text = "0")
label.pack()

#버튼 생성
button1 = Button(root, width=10, text="plus", overrelief="solid", command=countplus)
button1.pack()

button2 = Button(root, width=10, text="minus", overrelief="solid", command=countminums)
button2.pack()

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시
root.mainloop()







###텍스트를 입력받거나 출력하기 위한 입력창을 생성###
# tkinter 라이브러리 import
from tkinter import *

def calc(event) :
    label.config(text = "계산결과: " + str(eval(entry.get())))

# tk 객체 인스턴스 생성하기
root = Tk()
root.title("SISO")
root.geometry("300x200+100+100")
root.resizable(False, False)

# 레이블 생성
label = Label(root, text="0")
label.pack()

# Entry 생성
entry = Entry(root, width = 30)
entry.bind("<Return>", calc)
entry.pack()

# 메인 화면 표시
root.mainloop()
