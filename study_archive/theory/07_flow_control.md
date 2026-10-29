# 07. 흐름 제어: 조건문, 반복문

> 이미지: [note_12](assets/note_12_flow_control_if_elif_else.jpg) · [note_13](assets/note_13_for_loop_range.jpg) · [note_14](assets/note_14_while_break_continue.jpg) · [note_15](assets/note_15_pass_function_flowchart_overview.jpg) · [note_36](assets/note_36_list_comprehension_transpose.jpg) · [note_29](assets/note_29_summary_flow_control_loops.jpg)

## 1. 조건문
### if
- 조건이 참일 때 들여쓴 코드 블록 실행
- 특별한 상황에서 예외 처리할 때 사용

### if ~ else
- 둘 중 하나는 반드시 실행
- 하나를 만족하면 그 코드, 그 외의 경우는 else

### if ~ elif ~ else
- 여러 경우 중에서 하나만 처리
- `elif`는 앞 조건을 만족하지 않을 때 검사
- `else`는 모든 조건을 만족하지 않을 때 (생략 가능)
- 조건을 `and`, `or`, `not`으로 결합 가능

```python
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
else:
    grade = 'C'
print(grade)   # B
```

### 중첩 if (nested)
- 조건 안에 또 다른 조건
- 조건 우선순위와 조합을 따져 보아야 함
- `if A and B`처럼 한 줄로 합칠 수 있는지 먼저 확인

```python
num = 3
if num > 0:
    if num % 2 == 1:
        print("양수 홀수")
    else:
        print("양수 짝수")
else:
    print("0 이하")
```

## 2. for 반복문
- `for 변수 in 반복 가능한 객체:` 형태 (예: list)
- 항목을 하나씩 꺼내 더 이상 없을 때까지 반복
- seq는 반복 횟수일 수도, 반복 접근이 가능한 객체일 수도 있음
- for 문을 쓰지 않으면 `sum = sum + N[0]`, `sum = sum + N[1]`...처럼 반복해서 적어야 함

```python
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]   # 노트에는 중간 생략, 합계 48 [추정]
total = 0
for val in numbers:
    total = total + val
print(total)   # 48
```

### range()
- 메모리에 값을 모두 저장하지 않음
- `range(start, stop, step)`: start 이상 stop **미만**, 기본값은 `(0, 10, 1)`
- `range(3)`은 `range(0, 3, 1)`, `range(2, 3)`은 `range(2, 3, 1)`
- 인덱스로 접근할 때 많이 사용

```python
print(list(range(0, 10, 3)))   # [0, 3, 6, 9]
print(list(range(3, 0, -1)))   # [3, 2, 1]
```

### 합계를 구하는 세 가지 방법
```python
a = [1, 2, 3, 4]
s1 = a[0] + a[1] + a[2] + a[3]

s2 = 0
for index in range(len(a)):
    s2 += a[index]

s3 = 0
for v in a:
    s3 += v
print(s1, s2, s3)   # 10 10 10
```

### 중첩 for (2차원 리스트)
- 위치(index) 개념이 필요할 때 사용

```python
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
print()   # 1 2 3 4 5 6 7 8 9
```

## 3. while 반복문
- 조건이 참인 동안 반복
- 무한 루프에 빠지지 않도록 **종료 조건**(예: counter 증가)이 반드시 필요
- 종료 조건과 변수 초기화가 되어 있는지 확인
- 반복 횟수를 알 수 있으면 `for`를 우선 사용

```python
n = 5
i = 1
total = 0
while i <= n:
    total += i
    i = i + 1      # 빠뜨리면 무한 루프
print(total)       # 15
```

### while ~ else
- 반복이 `break` 없이 정상 종료되면 `else` 실행

```python
i = 0
while i < 3:
    i += 1
else:
    print("정상 종료")
```

## 4. break, continue, pass
- `break`: 반복문 전체를 빠져나감. if가 아니라 for(while)를 벗어남
- `continue`: 그 회차의 남은 코드를 건너뛰고 다음 반복으로 이동 (레벨 skip 아님)
- `pass`: 아무 일도 하지 않는 자리 표시. 코드 구조를 잡아 나갈 때 사용
  - `None`은 가리키는 것이 없는 값, `pass`는 아직 작성하지 않은 코드 자리

```python
# 짝수의 합
a = [1, 2, 3, 4]
s = 0
for v in a:
    if v % 2 != 0:
        continue
    s += v
print(s)   # 6

# 문자가 섞인 리스트에서 숫자만 더하기
b = [1, 2, 'a', 'b', 3]
t = 0
for v in b:
    if isinstance(v, int):
        t += v
print(t)   # 6
```
- 코딩 테스트에서 자주 나오는 패턴이라고 정리

---

# 추가 정리: 리스트 컴프리헨션 (note_36)

- 여러 명령문으로 작성된 코드를 한 줄로 작성 가능 (lambda와 비슷한 개념)
- 구조: `[ 실제 수행 명령 + 제어구문 ]` (이중 반복 + 조건도 가능)
- 노트 강조: 기본 틀(for문, 이중 for문 등)을 바꿔보는 연습을 해야 함 (기본기가 없으면 모호해짐)

## 1. 반복만 있는 경우
```python
pow2 = [2 ** x for x in range(10)]

pow2_1 = []
for x in range(10):
    pow2_1.append(2 ** x)
print(pow2 == pow2_1)   # True
print(pow2)             # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```
- `2 ** x`: 처리해야 할 명령문, `for x in range(10)`: 제어문

## 2. 반복 + 조건
```python
odd = [x for x in range(20) if x % 2 == 1]

odd2 = []
for x in range(20):
    if x % 2 == 1:
        odd2.append(x)
print(odd == odd2)   # True
print(odd)           # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

## 3. 조건이 2개일 때
- 노트의 `num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]` 형태
- 아래 for문 풀이에서 `if`를 이중으로 쓰면 `and`와 같은 동작 (노트에는 물음표 표시)

```python
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]

num_list2 = []
for y in range(100):
    if y % 2 == 0:
        if y % 5 == 0:
            num_list2.append(y)
print(num_list == num_list2)   # True
print(num_list)                # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```
- 보충: 노트의 for문 풀이는 `append(y)`가 첫 `if` 안에 있고 두 번째 `if`가 그 안쪽에 같이 있어 읽기 어렵게 적혀 있음. 위 코드는 같은 결과가 나오도록 정리한 것

## 4. if-else (조건 표현식)
- `if-else`는 컴프리헨션의 앞쪽(값 부분)에 씀

```python
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]

obj2 = []
for i in range(10):
    if i % 2 == 0:
        obj2.append("Even")
    else:
        obj2.append("Odd")
print(obj == obj2)   # True
print(obj[:4])       # ['Even', 'Odd', 'Even', 'Odd']
```
- 보충: 조건만 거를 때는 뒤쪽 `if`, 값을 둘 중 하나로 고를 때는 앞쪽 `if-else`

## 5. 중첩 반복: 행렬 전치 (transpose)
- 행렬의 행과 열을 바꾸기: `[[1,2,3,4],[5,6,7,8]]`(2x4) -> 4x2
- 노트에서는 새로 만들 변수 `transposed`, `transposed_row`를 두고, 바깥은 열 번호, 안쪽은 `matrix`의 각 행을 돈다

```python
matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)   # [[1, 5], [2, 6], [3, 7], [4, 8]]

# 컴프리헨션으로 같은 결과
t2 = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(t2 == transposed)   # True
```
- 노트 첫 줄의 `[[ ___ for ] for ]`는 안쪽 컴프리헨션이 바깥 `for`의 변수를 쓰는 형태를 뜻함
- `[판독 불확실]`: 노트 예시의 행렬 숫자는 `1~4`, `4~8` 비슷하게 보이나 위 코드는 `1~8`로 정리
