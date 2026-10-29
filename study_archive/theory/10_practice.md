# 10. 연습 문제: 약수 구하기, 업다운 게임

> 이미지: [note_16](assets/note_16_divisors_problem_flowchart.jpg) · [note_17](assets/note_17_updown_flowchart_function_def.jpg) · [note_18](assets/note_18_function_arguments_recursion.jpg) · [note_21](assets/note_21_updown_game_flowchart_hw.jpg)

## 문제 해결 순서 (노트 기준)
- 큰 그림 잡기
- 순서도(Flowchart) 그리기, 수정 및 보완
- 코드 작성
- 의도적으로 밑그림을 그리고 완성해야 함 (하다 보니 완성되는 방식은 지양)

## 1. 약수 구하기
- 문제: 정수를 입력받아 약수를 모두 출력 (예: 12의 약수는 1, 2, 3, 4, 6, 12)
- 순서도
  - 시작, 정수 A 입력, n = 1
  - n이 A보다 커지면 종료
  - `A % n == 0`이면 n 출력
  - n = n + 1 후 반복
- 피드백: `input()` 사용, `for i in range(1, n+1)`, 출력은 `sep`, `end` 활용

```python
A = int(input("정수 입력: "))
divisors = []
for n in range(1, A + 1):
    if A % n == 0:
        divisors.append(n)
print(f"{A}의 약수:", *divisors, sep=" ")
```

### 보완: 마지막 약수 뒤에 쉼표 없이 출력
- 슬라이싱 `divisors[0:len(divisors)-1]`과 `divisors[-1]` 활용

```python
A = 12
divisors = [n for n in range(1, A + 1) if A % n == 0]
print(f"{A}의 약수:", ", ".join(map(str, divisors)))
```

### 보완: 다시 실행할지 묻기
```python
while True:
    A = int(input("정수 입력: "))
    divisors = [n for n in range(1, A + 1) if A % n == 0]
    print(f"{A}의 약수:", ", ".join(map(str, divisors)))
    if input("다시 할까요? (y/n): ") != "y":
        break
```

## 2. 업다운 게임
- 문제: 1~100 사이의 정수를 입력해 컴퓨터가 정한 값을 맞추기
- 컴퓨터가 `random`으로 숫자를 정하고, 사용자가 입력한 숫자와 비교
  - 같으면 정답 출력 후 종료
  - 작으면 "업", 크면 "다운"
- 맞출 때까지 반복해야 하므로 `while True`와 `break` 사용 (조건 만족 시 반복 종료)

### 순서도
- 시작
- random 값 설정 (`num_t`)
- 내 숫자 입력 (`int(input())`로 숫자형으로 변환)
- 같은가? 같으면 출력 후 break
- 아니면 `elif`로 작은지 비교: 업 또는 다운 출력
- 입력 단계로 돌아가 반복

### 코드
- 사용 라이브러리: 표준 라이브러리 `random`

```python
import random

num_t = random.randint(1, 100)
while True:
    num = int(input("숫자 입력: "))
    if num == num_t:
        print(num)
        break
    elif num < num_t:
        print("업")
    else:
        print("다운")
```
- 노트의 조건 `num = num_t`는 대입이 아니라 비교 `==`로 써야 함

### 다음 단계
- Tkinter 또는 Flet으로 GUI 업다운 게임 만들기 (Flet은 앱, 웹을 지원하는 GUI)
