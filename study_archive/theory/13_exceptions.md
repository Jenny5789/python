# 13. 예외 처리 (try / except / else / finally / raise / assert)

> 이미지: [note_48](assets/note_48_exception_try_except_finally.jpg) · [note_49](assets/note_49_object_class_custom_exception.jpg) · [note_53](assets/note_53_file_io_open_with_os.jpg) · [note_47](assets/note_47_calculator_min_max_avg_class.jpg)

> note_48은 "4/9 File IO" 수업의 첫 부분이고, 같은 내용이 note_53의 마지막 칸(error and exceptions)에서도 시작됨.

## 1. 오류의 종류 (note_53)
- 문법적 오류: 코드를 실행하기 전에 인터프리터가 잡아냄 (`SyntaxError`)
- 실행 중 발생하는 오류: 실행해봐야 알 수 있음 -> `try ... except`로 처리

## 2. try ~ except (note_48)
- `try`: 실행 명령문, `except`: 오류 발생 시 예외처리
- 인터프리터가 오류를 판단해서 처리
- 상황별로 정리 가능

```python
try:
    x = int("abc")           # 오류 발생
except ValueError:
    print("숫자로 바꿀 수 없습니다")
```

### 여러 가지 예외 (try ~ except ~ except)
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다"
    except TypeError:
        return "숫자가 아닙니다"

print(divide(10, 2))     # 5.0
print(divide(1, 0))      # 0으로 나눌 수 없습니다
print(divide(1, "a"))    # 숫자가 아닙니다
```

## 3. try ~ raise (note_48)
- 문법적으로는 이상이 없지만 개발자가 오류로 설정하고 싶을 때 `raise`로 직접 발생시킴

```python
def set_age(age):
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없습니다")
    return age

try:
    set_age(-1)
except ValueError as e:
    print("오류:", e)    # 오류: 나이는 음수가 될 수 없습니다
```

## 4. try / except / else / finally 전체 구조 (note_48)

| 블록 | 의미 (노트 표기) |
|---|---|
| `try` | 실행문 (입력값 문제 여부) |
| `except` | 예외처리 (입력값에 문제가 있을 때) |
| `else` | 입력값 문제가 없을 때 수행됨 |
| `finally` | 오류와 상관없이 무조건 동작 |

```python
def parse(text):
    try:
        n = int(text)
    except ValueError:
        print("except:", text, "는 숫자가 아님")
    else:
        print("else:", n, "변환 성공")
    finally:
        print("finally: 항상 실행")

parse("12")
parse("x")
```

## 5. assert (note_48)
- `assert 조건`: 조건이 `True`면 통과, `False`이면 `AssertionError`(노트: assert alarm)
- 노트 메모: "but 추천 X". 조건은 `if` 같은 조건문으로 판단하는 방식을 권장
- 보충: `assert`는 개발 중 점검용이고, 파이썬을 `-O` 옵션으로 실행하면 무시되므로 입력 검증에는 `if` + `raise`가 안전

```python
try:
    assert 1 + 1 == 3, "계산이 맞지 않음"
except AssertionError as e:
    print("AssertionError:", e)
```

## 6. 사용자 정의 예외 클래스 (note_49, "Customizing exception class")
- `class CustomError(Exception): pass` 형태로 만들고, `class` 뒤에는 `pass`만 둬도 됨 (노트: 조건문이 있으면 동작되는지 한번 해보자)
- 노트 구조: `while` 안에 `try`, `if ... else break`, 조건에 맞지 않으면 `raise`, 바깥에서 `except`로 받아서 다시 입력

```python
class CustomError(Exception):
    pass

def check_qty(qty):
    if qty < 1:
        raise CustomError("수량은 1 이상이어야 합니다")
    return qty

inputs = iter([0, -3, 5])        # input() 대신 미리 정한 입력
while True:
    try:
        qty = check_qty(next(inputs))
    except CustomError as e:
        print("재입력:", e)
    else:
        print("수량 확정:", qty)
        break
```
- 출력: `재입력`이 2번 나오고 `수량 확정: 5`
- 쓰임새: [12_shopping_cart_sales_system](12_shopping_cart_sales_system.md)의 구매 개수 검증, [14_classes_oop](14_classes_oop.md)의 계산기에서 "숫자/문자 확인 후 예외처리"

## 7. 계산기에서의 예외처리 설계 (note_47)
- 계산기: 리스트로 입력받음. 목표: 더하기, 빼기, 곱하기, 나누기, `avg`, `max`, `min`
- 숫자와 문자(연산자)를 구분해서 입력 -> 규칙에 어긋나면 예외처리
  1. 숫자, 숫자 확인: `if not` -> 오류 알림
  2. 초기화 설정
  3. 연산 -> 평균, 최대, 최소 구해
- 숫자는 숫자대로, 연산자는 연산자대로 입력
- 구현은 [14_classes_oop](14_classes_oop.md)의 계산기 예제
