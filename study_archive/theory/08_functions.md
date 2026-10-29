# 08. 함수

> 이미지: [note_15](assets/note_15_pass_function_flowchart_overview.jpg) · [note_17](assets/note_17_updown_flowchart_function_def.jpg) · [note_18](assets/note_18_function_arguments_recursion.jpg) · [note_19](assets/note_19_lambda_filter_map.jpg) · [note_30](assets/note_30_summary_function_return_rps_flet_hw.jpg)

## 1. 함수란
- 작성해야 할 코드를 모듈로 만든 것 (큰 덩어리로 작성)
- 하나의 코드 블록을 특정 이름으로 지정해 둔 것
- 효과: 중복 감소, 재사용성 증가
- 파이썬은 인터프리터 언어이므로 **호출보다 먼저 정의**되어야 함
- 사용자 정의 함수와 내장 함수로 구분
- 함수 안과 밖의 변수 범위는 분리됨. 함수 안 변수는 지역 변수이고, 매개변수만 영향을 줌

```python
def 함수이름(매개변수):
    """설명(독스트링)"""
    실행할 코드
    return 반환값
```
- 호출할 때 `함수명()`의 괄호는 필수

## 2. return
- 값을 전달(반환)하고 함수의 동작을 중단함
- 함수 중간의 return은 비추천. 마지막에 두는 것을 권장
- 여러 값을 반환하면 tuple로 묶여 나옴 (의도적으로 변경하지 못하게)
- 일부 값만 쓰고 싶으면 `_`(underscore)로 받음

```python
def 예제_리턴():
    return 3, 6, 9

print(예제_리턴())    # (3, 6, 9)
a, _, _ = 예제_리턴()
print(a)             # 3
```

> 보충: 스크립트에서 `예제_리턴()`만 단독 호출하면 화면에 출력되지 않음. Colab 셀은 마지막 식의 값을 자동으로 보여 주기 때문에 노트에 출력으로 적힌 것.

### 절댓값 함수 예제
```python
def absolute_value(num):
    """절댓값을 반환한다."""
    if num >= 0:
        return num
    else:
        return -num

num = absolute_value(2)
print(num)                  # 2
print(absolute_value(-4))   # 4
```

## 3. 인자 (매개변수)
### 기본값 인자
- default 값이 있는 매개변수 **뒤에는 모두 default 값이 있어야** 함 (순서 혼동 방지)

```python
def greet(name, msg="GM!"):
    print(name, msg)

greet("Bruce")              # Bruce GM!
greet("Bruce", "HDYD?")     # Bruce HDYD?

# def greet(msg="GM!", name):   # SyntaxError
```

### 키워드 인자
- 키워드 인자 뒤에는 모두 키워드 인자만 올 수 있음

```python
greet(name="Bruce", msg="HDYD?")
# greet(name="Bruce", "HDYD?")  # SyntaxError
```

### 가변 인자 `*names`
- 인자 개수가 정해지지 않았을 때 사용. tuple로 전달됨

```python
def hello(*names):
    for n in names:
        print("Hello", n)

hello("A", "B", "C")
```
- 팁: 어떤 값을 매개변수로 이용할지 명확히 적어 둠

## 4. 재귀 (Recursion)
- 함수가 자기 자신을 호출
- 꼭 필요하지 않으면 사용하지 않음 (무한 루프 위험)
- 기본 재귀 한도는 1000

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```

### 반복문으로 계승 구하기
```python
result = 1
for i in range(3, 0, -1):   # 3, 2, 1
    result *= i
print(result)               # 6  (result가 0이면 곱이 항상 0)
```

## 5. lambda, filter, map
### lambda
- 이름 없는 일회용 함수. `lambda 인자: 식` (식 하나만 가능)
- `def`는 선언 후 호출해서 계산, lambda는 바로 계산

```python
def double(x):
    return x * 2

double2 = lambda x: x * 2
print(double(3), double2(3))   # 6 6
```

### filter와 map
- `filter(함수, 반복가능객체)`: 조건에 맞는 값만 걸러냄
- `map(함수, 반복가능객체)`: 각 값에 동일한 연산을 수행
- 둘 다 객체를 반환하므로 `list()`로 감싸서 확인 (list(객체)처럼 넣어야 함)

```python
my_list = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, my_list))
doubled = list(map(lambda x: x * 2, my_list))
print(evens)     # [2, 4, 6]
print(doubled)   # [2, 4, 6, 8, 10, 12]

# 같은 결과를 for 문으로
new_list = []
for x in my_list:
    new_list.append(x * 2)
print(new_list)  # [2, 4, 6, 8, 10, 12]
```

> 보충: 노트의 map 예제가 `x*2`인지 `x**2`인지 [판독 불확실]. 위 예제는 `x * 2` 기준.
> 보충: 노트에 적힌 filter/map의 인자 순서 설명은 부정확했고, 실제 시그니처는 `filter(function, iterable)`, `map(function, iterable)`.

---

# 추가 정리: 타입 힌트 (note_38)

- 함수의 매개변수에 `개인정보: dict`처럼 쓰면 "나는 dict로 사용할 거야"라고 알려주는 용도
- `->`: 반환값은 ○○야 라고 전달해주는 것 (반환 타입 표시)
- 힌트일 뿐이라 실행 시 타입을 강제하지 않음

```python
def add_person(book: dict, name: str, phone: str) -> dict:
    book[name] = phone
    return book

print(add_person({}, "kim", "010-1111-2222"))
# {'kim': '010-1111-2222'}
print(add_person({}, "lee", 123))   # 힌트와 달라도 실행됨 (오류 아님)
```
- 관련 실습은 [14_classes_oop](14_classes_oop.md)의 전화번호부 예제
