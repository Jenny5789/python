# 03. 자료형: 숫자, list, tuple, string, set, dict

> 이미지: [note_04](assets/note_04_none_datatypes_number_list.jpg) · [note_05](assets/note_05_list_slicing_tuple_string.jpg) · [note_06](assets/note_06_escape_set_dict_comparison.jpg) · [note_07](assets/note_07_dict_typecasting_print.jpg) · [note_27](assets/note_27_summary_datatypes_print_format.jpg) · [note_35](assets/note_35_tuple_dict_methods_get_pop.jpg) · [note_37](assets/note_37_datatypes_copy_math_random.jpg) · [note_38](assets/note_38_deep_copy_nested.jpg)

## 1. 숫자 (number)
- 정수(int): 메모리가 허용하는 범위까지 표현 가능
- 실수(float): 소수점 이하 약 15자리까지 정확
  - 보충: 실수는 이진 부동소수점이라 `0.1 + 0.2`가 정확히 `0.3`이 되지 않음

```python
print(0.1 + 0.2)          # 0.30000000000000004
print(2 ** 100)           # 정수는 매우 커져도 표현 가능
```

## 2. 리스트 (list)
- 순서가 있고 `[ ]`로 표기
- item의 유형이 서로 달라도 됨 (리터럴, None, 리터럴 모음 모두 가능)
- 변경, 추가, 삭제 가능 (mutable)
- 인덱스는 0부터 시작

### 인덱싱과 슬라이싱
```python
a = [5, 10, 15, 20, 25, 30, 35, 40]
print(a[2])        # 15
print(a[0:3])      # [5, 10, 15]  (3 미만, 즉 0~2번 인덱스)
print(a[5:])       # [30, 35, 40] (a[5:len(a)]와 같음)
print(a[-1])       # 40  (음수 인덱스는 오른쪽 끝이 -1)
```
- `a[시작:끝]`은 끝 인덱스를 포함하지 않음

### 값 변경, 중첩 리스트
```python
a = [1, 2, ["납", 20]]
print(a[2][0])      # 납
print(a[2][1])      # 20

a[0] = 100          # 값 변경

b = [[1, 2], [3, 4]]
print(b[1][0])      # 3  (b[행][열])
```

## 3. 튜플 (tuple)
- list와 비슷하지만 선언 이후 변경 불가
- `( )`로 표기, list보다 처리 속도가 빠름
- 튜플 안에 들어 있는 list는 내부 변경 가능

```python
t = (5, 'program', 1 + 3j)
# t[0] = 10   # TypeError: 'tuple' object does not support item assignment

a = ("a", 1, [1, 2, 3], 4)
a[2][0] = 99   # 튜플 안의 리스트는 변경 가능
print(a)       # ('a', 1, [99, 2, 3], 4)
```

## 4. 문자열 (string)
- 튜플처럼 `[ ]`와 슬라이싱으로 접근 가능하지만 변경 불가 (immutable)
- 공백, 특수문자도 한 글자로 계산
- `len(문자열)`: 글자 수. for 문을 돌릴 때 반복 횟수로 활용

```python
s = 'string'
print(s[0], s[1:3])   # s tr
# s[0] = 'c'          # TypeError
print(len('cold'))    # 4
```

### enumerate()
- 인덱스와 값을 쌍으로 묶어 객체 형태로 반환 (준비 상태)
- 값을 보려면 `list()`로 형변환 필요

```python
print(list(enumerate('cold')))
# [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
```

## 5. 이스케이프 문자
- `\n`: 줄바꿈
- `\t`: 탭

## 6. 집합 (set)
- 고유한 item의 순서 없는 모음 (중복 불가)
- 인덱스 접근 불가 (`a[0]` 불가), 변경 가능한 item(list 등)은 담을 수 없음
- 다양한 내장 메서드 제공: `add()`, `update()`, `discard()`, `remove()`
- 활용 예
  - 설문조사 10만 명 응답에서 중복 제거
  - 아이디 중복 확인

```python
s = {1, 2, 2, 3, 4}
print(s)            # {1, 2, 3, 4}
s.add(5)
s.discard(1)
print(s)            # {2, 3, 4, 5}
```

## 7. 딕셔너리 (dict)
- `{key: value}` 형태. key로 value를 검색
- key: 순서나 문자 등 리터럴, value: 리터럴 또는 리터럴 모음
- 데이터 검색에 최적화 (item이 많아져도 검색 속도가 빠름)
- 코드 유지 관리가 좋음 (추가, 삭제, 수정이 쉬움)

```python
사람 = {
    '홍길동': {'나이': 100, '성별': '남'},
    '심청이': {'나이': 16, '성별': '여'},
}
print(사람['홍길동']['나이'])   # 100
```

### list 대신 dict를 쓰는 이유
- 몇 번째 위치인지 인덱스를 알 필요가 없음
- 정보를 추가해도 기존 코드를 바꿀 필요가 없음

## 8. 자료형 비교

| 자료형 | 순서 | 수정 | 중복 | 표기 |
|---|---|---|---|---|
| list | O | O | O | `[ ]` |
| tuple | O | X | O | `( )` |
| set | X | O | X | `{ }` |
| dict | key로 접근 | O | key 중복 X | `{k: v}` |

> 보충: 노트에는 dict의 순서를 X로 적었으나, Python 3.7부터 dict는 **삽입 순서를 유지**함. 다만 인덱스가 아니라 key로 접근함.

---

# 추가 정리 (4월 노트: note_35, 37, 38)

## 7. 숫자 자료형과 형 확인 (note_37)
- `int`: 파이썬은 메모리가 허용하는 범위까지 표현
- `float`: 소수점 이하 약 15자리까지 정확
- `complex`: 복소수
- `Decimal`: 십진수 (정확한 소수 계산), `Fraction`: 분수
- `type()`: 형태 확인, `isinstance(a, int)`: `a`의 자료형이 `int`인지 `True/False`로 확인
- 형변환: `int()`, `float()`, `complex()` (더 큰 형으로는 암묵적으로도 변환됨)

```python
from decimal import Decimal
from fractions import Fraction

a = 1
print(type(a))               # <class 'int'>
print(isinstance(a, int))    # True
print(0.1 + 0.2)             # 0.30000000000000004
print(Decimal("0.1") + Decimal("0.2"))   # 0.3
print(Fraction(1, 3) + Fraction(1, 6))   # 1/2
print(1 + 2.5)               # 3.5  (int -> float 암묵적 변환)
```
- 보충: `Decimal`은 문자열로 만들어야 정확함 (`Decimal(0.1)`은 이미 부정확한 float 값을 그대로 가져옴)

## 8. math 모듈 (note_37)
- `import math` 후 `ceil`, `floor`, `exp`, `pow`, `sqrt`, `pi`, `e` 등을 사용
- 노트 표기 `import math as math`는 별칭이 같아서 생략 가능
- `random`의 `seed`~`triangular`는 "나중 숙제"로 적혀 있음 (파일 참고해서 만들어보기)

```python
import math

print(math.ceil(2.1), math.floor(2.9))   # 3 2
print(math.sqrt(16), math.pow(2, 10))    # 4.0 1024.0
print(round(math.pi, 4), round(math.e, 4))   # 3.1416 2.7183
```

## 9. 리스트 메서드 (note_37)
- 리스트: 여러 요소를 한 번에 담는 자료형, 요소를 변경/추가할 수 있음
- 추가 메서드 3가지

| 메서드 | 동작 |
|---|---|
| `append(x)` | 맨 뒤에 하나 추가 |
| `extend(iterable)` | 여러 개를 이어서 추가 |
| `insert(i, x)` | 특정 위치에 추가 (`odd.insert(0, 10)`: 위치, 데이터 순) |

- `+`: 결합/연결, `*`: 반복 지원
- `pop()`: 꺼내오기 (기본값 `-1`, 맨 끝 요소)
- `remove(x)`: 삭제 (값으로 찾아서 앞에서부터 하나만 제거)
- `clear()`: 비워서 `[]`로 초기화 (변수는 남고 item만 없어짐)
- `del`: item과 변수까지 없앰 (메모리에서 없애는 것처럼 보이지만 연결고리를 끊어주는 것)

```python
odd = [1, 3, 5]
odd.append(7)             # [1, 3, 5, 7]
odd.extend([9, 11])       # [1, 3, 5, 7, 9, 11]
odd.insert(0, 10)         # [10, 1, 3, 5, 7, 9, 11]
print(odd.pop())          # 11 (맨 끝)
odd.remove(10)            # 값 10 제거
print(odd)                # [1, 3, 5, 7, 9]
print([1, 2] + [3], [0] * 3)   # [1, 2, 3] [0, 0, 0]
odd.clear()
print(odd)                # []
del odd                   # 변수 이름 자체가 사라짐
```
- 보충: `del`은 "객체를 지운다"기보다 이름(변수)을 지우는 것이고, 객체는 아무도 참조하지 않을 때 파이썬이 정리함

## 10. 얕은 복사와 깊은 복사 (note_37, 38)
- 얕은 복사(shallow copy, 기본 구조): 바깥 리스트만 새로 만들고, 안쪽 item은 같은 객체를 공유
- 깊은 복사(deep copy): item 안에 있는 item까지 모두 새 주소를 할당 (완전히 새로 만듦)
- 노트 예: `a = [1, 2, 3]`에 `b = a`는 같은 주소 공유, `b = a.copy()`는 복사해서 새로 저장

```python
import copy

a = [1, 2, 3]
b = a            # 같은 객체
c = a.copy()     # 새 리스트
a.append(4)
print(b, c)      # [1, 2, 3, 4] [1, 2, 3]

nested = [[1, 2], [3, 4]]
shallow = copy.copy(nested)
deep = copy.deepcopy(nested)
nested[0].append(99)
print(shallow)   # [[1, 2, 99], [3, 4]]  안쪽 리스트를 공유
print(deep)      # [[1, 2], [3, 4]]      완전히 독립
```
- 노트 메모: 계산기처럼 "버튼을 누르면 입력" 등의 초기화에 deep copy가 쓰임
- 사용 라이브러리: 표준 라이브러리 `copy`, `decimal`, `fractions`, `math`

## 11. 튜플 선언 (note_35)
- 괄호 없이도 선언 가능하지만, 쉼표가 없으면 tuple로 인식되지 않음

```python
t = 1, 2, 3
print(type(t))        # <class 'tuple'>
one = (1,)            # 요소가 하나면 쉼표 필요
not_tuple = (1)       # 그냥 int
print(type(one), type(not_tuple))
```

## 12. dict 추가 정리 (note_35)
- `dict()`: 형변환, 쌍으로 된 시퀀스에서 만들 수 있음
- 딕셔너리 컴프리헨션: `{x: x * x for x in range(6)}` (`key: value` 구분)
- `get()`: 키가 없으면 `None` 반환, `[]`로 접근하면 `KeyError`
- `pop(key)`: 해당 key의 value를 꺼내고 삭제 (index가 아니라 key값으로 찾음)
- `popitem()`: 마지막 `(key, value)` 쌍을 꺼내고 삭제
- `clear()`: 비우기, `del`: 변수까지 삭제
- 요약 메모: `pop`은 꺼내고 없앰, `get`은 꺼내고 확인만 함

```python
squares = {x: x * x for x in range(6)}
print(squares)                      # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(dict([(1, 0), (2, 0)]))       # {1: 0, 2: 0}
print(squares.get("add"))           # None  (오류 없이 예외처리용)
try:
    squares["add"]
except KeyError:
    print("KeyError")
print(squares.pop(4))               # 16  (꺼내고 삭제)
print(squares.popitem())            # (5, 25)
print(squares.get(3))               # 9   (확인만, 삭제 안 됨)
print(squares)                      # {0: 0, 1: 1, 2: 4, 3: 9}
```
- `[판독 불확실]`: `{'a': 1, 'b': 2, 'c': 3}`을 "문자"로 표시한 옆 메모(key 변경 가능 여부, value는?)는 의문 형태로만 적혀 있음. 보충: key는 변경 불가(hashable), value는 변경 가능

## 13. 내장 함수 (note_35)
- 내장 함수(built-in functions): 파이썬 자체가 가지고 있는 함수
- `len()`, `sorted()`, `all()`, `any()`

```python
squares = {x: x * x for x in range(6)}
print(len(squares))       # 6
print(sorted([3, 1, 2]))  # [1, 2, 3]
print(all(squares))       # False
print(any(squares))       # True
print(all([1, 2, 3]), any([0, 0]))   # True False
```
- 노트: `all(squares)`의 결과는 `False`로 적혀 있음 (이유 칸에 `0` 관련 메모)
- 보충: `all()`은 dict에서 key만 검사하는데 key `0`이 거짓으로 평가되어 `False`가 나옴
