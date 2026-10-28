# 2026년 4월 코딩 테스트 풀이
 
파이썬 기초 문법을 문제 풀이로 적용한 기록.
 
- 기간: 2026-04-10 ~ 2026-04-28
- 문제 출처: 프로그래머스 (코딩 테스트 입문, 코딩 기초 트레이닝)
- 풀이 방식: 문제 분석(변수/작업 정리), 코드 셀 단위 시도, 결과 확인
## 구현 경험
 
| 항목 | 구현 내용 | 파일 |
|---|---|---|
| 조건문 | if/elif/else 분기, 범위 비교(`0 < angle < 90`), 중첩 if로 사분면 판별 | [04_15](2026_04_15_codingtest.ipynb), [04_16](2026_04_16_codingtest.ipynb), [04_28](2026_04_28_codingtest.ipynb) |
| 논리 연산 | `&`, `\|`로 홀짝 조합 조건 처리, boolean 인자 분기 | [04_10](2026_04_10_codingtest.ipynb), [04_28](2026_04_28_codingtest.ipynb) |
| 반복문, 누적 | for + range로 합계, 개수, 약수 개수 누적 (초기화 후 누적) | [04_10](2026_04_10_codingtest.ipynb), [04_15](2026_04_15_codingtest.ipynb), [04_16](2026_04_16_codingtest.ipynb), [04_26](2026_04_26_codingtest.ipynb) |
| 리스트 처리 | append, remove, reverse, index, max, 인덱스 슬라이싱, sorted | [04_14](2026_04_14_codingtest.ipynb), [04_16](2026_04_16_codingtest.ipynb), [04_18](2026_04_18_codingtest.ipynb), [04_24](2026_04_24_codingtest.ipynb), [04_26](2026_04_26_codingtest.ipynb) |
| 함수형 도구, 컴프리헨션 | filter + lambda로 조건 제거, 리스트 컴프리헨션으로 원소 변환 | [04_13](2026_04_13_codingtest.ipynb), [04_15](2026_04_15_codingtest.ipynb), [04_28](2026_04_28_codingtest.ipynb) |
| 문자열 처리 | str/int 형변환, join, 문자 반복, list 변환, upper, `not in`으로 문자 필터링 | [04_10](2026_04_10_codingtest.ipynb), [04_15](2026_04_15_codingtest.ipynb), [04_20](2026_04_20_codingtest.ipynb) |
| 집합 | set 교집합(`&`)으로 공통 원소 개수 계산 | [04_26](2026_04_26_codingtest.ipynb) |
| 입출력 | input()으로 정수 입력, f-string 출력 | [04_28](2026_04_28_codingtest.ipynb) |
| 문제 분석 | 변수와 작업을 마크다운으로 먼저 정리한 뒤 코드 작성 | [04_16](2026_04_16_codingtest.ipynb), [04_18](2026_04_18_codingtest.ipynb), [04_20](2026_04_20_codingtest.ipynb), [04_24](2026_04_24_codingtest.ipynb) |
 
## 문제 해결
 
| 문제 | 처음 시도 결과 | 풀리지 않은 이유 | 해결 방법 | 파일 |
|---|---|---|---|---|
| 키 큰 사람 수 | 누적 변수가 값 없이 증가 연산에 사용됨 | 변수 초기화 누락 (`count = count + 1`) | 누적 변수를 `0`으로 초기화한 뒤 조건 충족 시 증가 | [04_10](2026_04_10_codingtest.ipynb) |
| 인덱스 문자 조합 | `SyntaxError: invalid syntax` | 키워드 인자 지정에 `=` 대신 `:` 사용 (`end:""`) | `end = ""`로 수정, 04_13에서 완성 | [04_10](2026_04_10_codingtest.ipynb), [04_13](2026_04_13_codingtest.ipynb) |
| 가장 큰 두 수의 곱 | `IndexError: pop index out of range` | `list.pop()`은 인덱스를 받는데 최댓값(값)을 전달 | 값 기준 삭제인 `remove()` 사용, `max()` 두 번 호출 | [04_18](2026_04_18_codingtest.ipynb) |
| 모음 제거 | `ValueError: empty separator` | `str.split("")`은 빈 구분자를 허용하지 않음 | 문자열 for 순회, 모음이 아니면 리스트에 append, `"".join()`으로 결합 | [04_19](2026_04_19_codingtest.ipynb), [04_20](2026_04_20_codingtest.ipynb) |
| 특정 문자 제거 | 같은 문자가 여러 개인데 첫 번째만 삭제됨 | `list.remove()`는 첫 번째 일치 값만 삭제 | `filter()` + `lambda`로 조건에 맞는 원소만 유지 | [04_15](2026_04_15_codingtest.ipynb) |
 
### 변수 초기화와 누적
 
```python
total = 0                # 누적 변수 초기화
for i in range(1, 5):
    total = total + i    # 이전 값을 읽어서 새 값으로 갱신
print(total)             # 10
```
 
| 누적 종류 | 초기값 | 예시 |
|---|---|---|
| 합계, 개수 | `0` | `count = 0` |
| 곱 | `1` | `result = 1` |
| 리스트 | `[]` | `answer = []` |
| 문자열 | `""` | `output = ""` |
 
> 누적 연산은 이전 값을 읽은 뒤 새 값을 쓰는 구조.
> 읽기 전에 값이 없으면 오류 (셀에서는 `NameError`, 함수 안에서는 `UnboundLocalError`).
> 변수명은 내장 함수명(`sum`, `max` 등)과 겹치지 않게 지정.
 
### 키워드 인자 (print)
 
| 인자 | 설명 | 기본값 |
|---|---|---|
| `sep` | 값 사이에 넣는 구분 문자 | `' '` |
| `end` | 출력 마지막에 붙는 문자 | `'\n'` (줄바꿈) |
 
```python
print("a", "b", end="")   # 줄바꿈 없이 이어서 출력: ab 형태
```
 
> 키워드 인자는 `이름=값` 형태로 전달.
> `:`는 딕셔너리, 슬라이싱, 타입 힌트에 쓰는 기호이며 인자 지정에는 사용 불가.
 
### pop 과 remove
 
| 메서드 | 삭제 기준 | 반환값 | 예시 |
|---|---|---|---|
| `list.pop(i)` | 인덱스 `i`의 원소 | 삭제한 원소 | `[1, 2, 3].pop(0)` 반환 `1` |
| `list.remove(x)` | 값이 `x`인 첫 번째 원소 | `None` | `[1, 2, 3].remove(2)` |
 
```python
numbers = [1, 2, 3, 4, 5]
numbers.pop(max(numbers))   # pop(5): 유효 인덱스는 0 ~ 4라서 IndexError
```
 
> `pop`은 인덱스, `remove`는 값을 기준으로 삭제.
> 값을 알고 있을 때는 `remove`, 위치를 알고 있을 때는 `pop`.
 
### 문자열 분리와 결합
 
| 방법 | 설명 | 예시 |
|---|---|---|
| `str.split(sep)` | `sep` 기준으로 나눈 리스트 반환 | `"a b".split(" ")` 결과 `['a', 'b']` |
| `str.split("")` | 빈 구분자는 `ValueError` | 사용 불가 |
| `list(str)` | 문자 단위 리스트로 변환 | `list("abc")` 결과 `['a', 'b', 'c']` |
| `"".join(list)` | 리스트 원소를 하나의 문자열로 결합 | `"".join(['a', 'b'])` 결과 `'ab'` |
 
> 문자열은 불변(immutable) 자료형이라 `remove`, `append` 메서드가 없음.
> 문자열은 for로 문자 단위 순회 가능, 결과는 리스트에 모은 뒤 `join`으로 결합.
 
### 조건에 맞는 원소만 남기기
 
| 방법 | 설명 |
|---|---|
| `list.remove(x)` | 값이 같은 첫 번째 원소 1개만 삭제, 원본 변경 |
| `filter(함수, 반복가능객체)` | 함수 결과가 `True`인 원소만 남긴 이터레이터 반환 (원본 유지) |
| `list(filter(...))` | 이터레이터를 리스트로 변환 |
 
```python
letter = "B"
my_list = list("BCBdbe")
list(filter(lambda x: x != letter, my_list))   # ['C', 'd', 'b', 'e']
```
 
> `lambda`는 이름 없는 한 줄 함수.
> `filter`는 반환값이 이터레이터라서 리스트로 쓰려면 `list()`로 감싸야 함.
 
## 사용 라이브러리
 
- 외부 라이브러리: 없음
- 표준 라이브러리: 없음
  - 내장 함수, 메서드 중심 (len, range, sum, max, sorted, filter, set 등)
  - 04_10에 `from typing import Counter`가 있으나 사용하지 않음
## 파일 구성
 
| 날짜 | 풀이 내용 |
|---|---|
| [04_10](2026_04_10_codingtest.ipynb) | 키 큰 사람 수, 문자열 대문자 변환, boolean 인자 분기, 두 수 이어붙이기 비교, 문자 배열 합치기, 인덱스 문자 조합(시작) |
| [04_13](2026_04_13_codingtest.ipynb) | 인덱스 문자 조합(완료), 배열 원소 두 배 |
| [04_14](2026_04_14_codingtest.ipynb) | 피자 판 수, 평균, 잔 수와 거스름돈, 배열 뒤집기, 문자열 뒤집기(시작) |
| [04_15](2026_04_15_codingtest.ipynb) | 문자열 뒤집기(완료), 짝수 홀수 개수, 문자 반복, 특정 문자 제거, 각도 분류 |
| [04_16](2026_04_16_codingtest.ipynb) | 양꼬치 계산, 짝수 합, 배열 자르기, 순서쌍 개수, 사분면 판별 |
| [04_18](2026_04_18_codingtest.ipynb) | 최댓값 만들기, 모음 제거(시작) |
| [04_19](2026_04_19_codingtest.ipynb) | 모음 제거(이어서 시도) |
| [04_20](2026_04_20_codingtest.ipynb) | 모음 제거(완료) |
| [04_24](2026_04_24_codingtest.ipynb) | 배열 원소 길이, 삼각형 완성조건 |
| [04_26](2026_04_26_codingtest.ipynb) | 편지 가로 길이, 가장 큰 수와 인덱스, 배열 유사도, n의 배수 고르기, 자릿수 합 |
| [04_28](2026_04_28_codingtest.ipynb) | 홀짝 구분, 정수 부분, 주사위 게임, 정수 찾기, 배열 원소 삭제 |
 
## 범위
 
- 대부분 코드 셀 단위 풀이
- `def solution` 함수로 정리한 문제는 일부 (04_10 대문자 변환 등)
- 04_10 boolean 인자 문제는 문자열 비교에서 멈춤 (최종 정리 없음)
