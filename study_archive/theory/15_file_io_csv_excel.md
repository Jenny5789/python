# 15. 파일 입출력: open, with, os, csv, 엑셀

> 이미지: [note_53](assets/note_53_file_io_open_with_os.jpg) · [note_48](assets/note_48_exception_try_except_finally.jpg) · [note_54](assets/note_54_excel_pandas_class_method.jpg) · [note_55](assets/note_55_csv_module_dictreader.jpg)

> note_48이 4/9(목) "File IO" 수업 첫 페이지이고, note_55는 4/15 표기. "텍스트(.txt)에 저장 후 찾아오는 연습"이 이 단원의 목표 (note_48 메모).

## 1. File I/O 개념 (note_53)
- 외부로부터 정보를 가지고 와서 사용하거나, 정보를 내보냄
- `open()`: 파일을 불러온다 (나만 사용), `close()`: 파일을 닫는다 (다른 사람도 사용 가능하도록)
- 짝(쌍)으로 기억: 열었으면 닫아야 함
- 문법: `f = open("text.txt", mode="r", encoding="cp1252")`
  - 함수 `open` / 파일명 / 확장자 포함 / `mode`는 권한 부여 (default: `r`)
  - `encoding`: 어떤 방식으로 만들어졌는지 알려줌 (노트 예 `cp1252`)
  - 객체(`f`)에 내장 함수가 들어 있음, `f.close()`는 객체를 닫아 변수를 닫아줌

## 2. mode 종류 (note_53)

| mode | 의미 |
|---|---|
| `r` | read, default |
| `w` | write, 새로 만든다. 기존에 있던 문서를 지워버린다 |
| `x` | 덮어쓰기? (실행 권한?) -> 보충: 새 파일을 만들며, 이미 있으면 `FileExistsError` |
| `a` | 작성된 내용 끝에 붙여서 두는 것 (기존 문서에 이어서). 기존 문서가 없으면 새로 만든다 |
| `+` | 업데이트용으로 파일을 가져온다 (읽기+쓰기 조합, 예 `r+`) |

- `write()`: mode가 `w`, `a`, `x`, `+` 조합일 때 / `read()`: mode가 `r`, `+` 조합일 때

## 3. 쓰기와 읽기 (note_53)
- `f.read(4)`: 4개 data만 읽어옴 / `f.read()`: 전체 읽어옴
- `f.tell()`: 현재 위치 / `f.seek(0)`: 위치 이동 (처음으로 간다)
- `for` loop로 읽으면 줄마다 `\n`이 붙은 형태로 나옴
- `readline()`: 한 줄, `readlines()`: 모든 줄을 리스트로 (숫자도 되나? 문자 `\n`, `\t` 등은? -> 노트 메모, 아래 보충)
- file method 정리: `close`, `read`, `readline`, `readlines`, `seek`, `tell`, `write` (노트 별표 표시, list/random 등 툴로 목차 다뤄보기)

```python
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    old = os.getcwd()
    os.chdir(tmp)                       # 임시 폴더에서 실습
    try:
        f = open("text.txt", mode="w", encoding="utf-8")
        f.write("first\n")
        f.write("second\n")
        f.close()                       # 닫기

        f = open("text.txt", mode="a", encoding="utf-8")
        f.write("third\n")              # 이어쓰기
        f.close()

        f = open("text.txt", mode="r", encoding="utf-8")
        print(f.read(4))                # firs  (4개만)
        print(f.tell())                 # 4
        f.seek(0)                       # 처음으로
        s1 = f.read()                   # 전체 읽기
        print(repr(s1))                 # 'first\nsecond\nthird\n'
        f.seek(0)
        print(f.readline())             # first\n  (한 줄)
        print(f.readlines())            # ['second\n', 'third\n']  (남은 줄 전부)
        f.seek(0)
        for line in f:                  # for loop: 줄마다 '\n'이 붙어 나옴
            print(repr(line))
        f.close()

        try:
            open("text.txt", mode="x")  # 이미 있으면 오류
        except FileExistsError:
            print("x 모드: 이미 있는 파일")
    finally:
        os.chdir(old)
```
- 보충: `readlines()`는 문자열 리스트를 돌려주고, 숫자로 쓰려면 `int()`로 변환해야 함. `\n`(줄바꿈), `\t`(탭)은 문자열 안에 그대로 들어 있어 `strip()`으로 제거
- 사용 라이브러리: 표준 라이브러리 `os`, `tempfile`

## 4. try / finally 와 with (note_53)
- 파일을 연 뒤 오류가 나도 닫히게: `try: f = open(...)` + `finally: f.close()`
- `with open(...) as f:`: 내부적으로 동작이 끝나면 `end`, 코드 블록을 벗어나는 순간 `f`를 벗어남 -> `.close()` 별도 명령 없이도 끝낸다

```python
import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "text.txt")

    # try / finally 방식
    f = None
    try:
        f = open(path, "w", encoding="utf-8")
        f.write("hello\n")
    finally:
        if f:
            f.close()

    # with 방식 (권장)
    with open(path, "a", encoding="utf-8") as f:
        f.write("world\n")
    print(f.closed)                     # True (블록을 벗어나면 자동으로 닫힘)

    with open(path, encoding="utf-8") as f:
        print(f.readlines())            # ['hello\n', 'world\n']
```
- 같은 방식은 [13_exceptions](13_exceptions.md)의 `try` / `finally` 정리와 연결됨

## 5. os 모듈과 shutil (note_53)
- `os.getcwd()`: 현재 작업 폴더 (`getcwdb()`는 bytes 버전)
- `os.chdir('../home')`: 작업 폴더 이동
- `import shutil`: 노트에 "완전삭제 (임시저장 후 삭제X)"라고 적혀 있음 -> 보충: `shutil.rmtree()`는 휴지통 없이 폴더를 통째로 지움. 파일 복사/이동은 `shutil.copy`, `shutil.move`

```python
import os
import shutil
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    old = os.getcwd()
    os.chdir(tmp)
    try:
        print(os.getcwd() == os.path.realpath(tmp))   # True
        with open("a.txt", "w", encoding="utf-8") as f:
            f.write("data")
        shutil.copy("a.txt", "b.txt")                 # 복사
        print(sorted(os.listdir(".")))                # ['a.txt', 'b.txt']
        os.makedirs("sub")
        shutil.rmtree("sub")                          # 폴더 통째로 삭제 (되돌릴 수 없음)
        print(sorted(os.listdir(".")))                # ['a.txt', 'b.txt']
    finally:
        os.chdir(old)
```

## 6. csv 모듈 (note_55, 4/15)
- CSV: comma separated value. 엑셀로도 열 수 있음
- 사용: `import csv`, `with open(파일, mode=..., encoding=..., newline='') as f:`
  - `encoding`: `cp949` (MS/OS 한글), `utf-8` (mac)
  - `newline=''`: CSV일 때 꼭 지정해야 함 (줄바꿈이 두 번 들어가는 문제 방지)
  - 노트: "CSV일 때 set로 생각하기" `[판독 불확실]`
- `csv.writer(f)`: 권한 부여 후 `csv_writer = csv.writer(f)`, `writerow(...)`: 한 행씩 기록할 것
- `for 물건, 정보 in 물건정보들.items():`: `.items()`만 적으면 key와 value 쌍이 전달됨
- `csv.DictReader`: key값을 `header`로 자동 설정. 파일로 저장하면 모두 "문자"로 저장되므로 불러와 활용할 때는 문자/숫자 확인 필요
- 노트 메모: 모듈 사용법, 예시 코드는 내장 함수(공식 문서)에서 확인, GitHub에 정리하기

```python
import csv
import os
import tempfile

items = {"apple": {"단가": 1500, "재고": 60}, "milk": {"단가": 2500, "재고": 55}}

with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "db.csv")

    with open(path, mode="w", encoding="utf-8", newline="") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(["품명", "단가", "재고"])           # header
        for name, info in items.items():                      # 쌍으로 전달
            csv_writer.writerow([name, info["단가"], info["재고"]])

    with open(path, mode="r", encoding="utf-8", newline="") as f:
        for row in csv.reader(f):
            print(row)          # ['품명', '단가', '재고'] ...

    with open(path, mode="r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):       # header가 key로 자동 설정
            print(row["품명"], row["단가"], type(row["단가"]))
            # 값은 모두 str -> 계산하려면 int()로 형변환
```
- 보충: 한글 Windows의 엑셀에서 바로 열 때 글자가 깨지면 `encoding="utf-8-sig"` 또는 `cp949`로 저장

## 7. 엑셀 파일 다루기 (note_54)
- 모듈: pandas (엑셀 + 복합, 데이터분석), openpyxl (엑셀 전용)
- 노트: "잠깐잠깐 다뤄보자"
- 활용: DB 품목을 엑셀에서 불러오기. 단가/재고가 문자로 되어 있으면 숫자로 형변환해서 사용
- 계산기, 전화번호 concept: 엑셀 특정 내역에서 계산. 숫자/문자 등. 가정: 어떤 표기법까지 허용해줄 것인지 (예: 리스트 안의 리스트 `# 23, 24 (list, tuple)` 허용해준 것)

```python
import os
import tempfile

import pandas as pd
from openpyxl import load_workbook

with tempfile.TemporaryDirectory() as tmp:
    path = os.path.join(tmp, "db.xlsx")

    df = pd.DataFrame({"품명": ["apple", "milk"], "단가": [1500, 2500], "재고": [60, 55]})
    df.to_excel(path, index=False)              # 엑셀로 저장

    back = pd.read_excel(path)                  # 엑셀 읽기
    print(back.dtypes["단가"])                   # int64 (숫자로 저장된 경우)
    print((back["단가"] * back["재고"]).sum())   # 227500

    wb = load_workbook(path)                    # openpyxl로 셀 접근
    ws = wb.active
    print(ws["A1"].value, ws["A2"].value)       # 품명 apple
    wb.close()
```
- 사용 라이브러리: `pandas`, `openpyxl` (외부 설치 필요: `pip install pandas openpyxl`)
- 보충: `df.to_excel`은 내부적으로 `openpyxl`을 사용함
