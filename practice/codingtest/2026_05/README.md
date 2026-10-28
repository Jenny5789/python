# 2026년 5월 코딩 테스트 풀이

4월 기초 문법 풀이를 이어, 함수 단위(`def solution`) 풀이와 문제 분석 습관으로 확장한 기록.

- 기간: 2026-05-02 ~ 2026-05-31
- 문제 출처: 프로그래머스
- 풀이 방식: 문제 분석(설계 주석), 코드 셀 단위 시도, `def solution` 정리
- 개념 정리: 아래 [개념 정리](#개념-정리) 항목 참고 (컴프리헨션, 문자열 메서드, 정렬, map, zip 등)

## 구현 경험

| 항목 | 구현 내용 | 파일 |
|---|---|---|
| 반복문, 누적 | 중첩 for로 약수 구하기, 약수 개수 홀짝에 따라 가감, 요금 누적, while 반복 횟수 제한(콜라츠) | [05_19](2026_05_19_codingtest.ipynb), [05_24](2026_05_24_codingtest.ipynb) |
| 스택 | 리스트 append/pop으로 올바른 괄호 판별, 비어 있을 때 닫는 괄호 처리 | [05_28](2026_05_28_codingtest.ipynb) |
| 정렬 활용 | sort/sorted(reverse), 한쪽 오름차순 + 한쪽 내림차순으로 곱의 합 최소화 | [05_24](2026_05_24_codingtest.ipynb), [05_31](2026_05_31_codingtest.ipynb) |
| 문자열 가공 | split/join, 공백 처리, upper/lower/capitalize, JadenCase 변환, 문자 위치별 대소문자 교체 | [05_26](2026_05_26_codingtest.ipynb), [05_27](2026_05_27_codingtest.ipynb), [05_29](2026_05_29_codingtest.ipynb), [05_25](2026_05_25_codingtest.ipynb) |
| 슬라이싱, range | 앞 n글자, 뒤 4자리 제외 마스킹, range step으로 홀짝 번째 합, 음수 step | [05_02](2026_05_02_codingtest.ipynb), [05_10](2026_05_10_codingtest.ipynb), [05_11](2026_05_11_codingtest.ipynb), [05_19](2026_05_19_codingtest.ipynb) |
| 리스트 컴프리헨션 | 간격 수열, 곱 리스트 생성 | [05_30](2026_05_30_codingtest.ipynb), [05_31](2026_05_31_codingtest.ipynb) |
| zip | 두 배열 동시 순회(내적, 문자열 섞기), 중첩 zip으로 행렬 덧셈 | [05_11](2026_05_11_codingtest.ipynb), [05_20](2026_05_20_codingtest.ipynb), [05_22](2026_05_22_codingtest.ipynb) |
| 조건 분기 | 중첩 if 4가지 경우 분기, break로 반복 중단, 연산자 분기 계산 | [05_09](2026_05_09_codingtest.ipynb), [05_14](2026_05_14_codingtest.ipynb), [05_17](2026_05_17_codingtest.ipynb) |
| 수학 계산 | 약수의 합, 자릿수 합, 하샤드 수, 제곱근 판별, 분수 덧셈, 평균, 중앙값 | [05_13](2026_05_13_codingtest.ipynb), [05_15](2026_05_15_codingtest.ipynb), [05_16](2026_05_16_codingtest.ipynb), [05_21](2026_05_21_codingtest.ipynb) |
| 입출력 | input().strip().split(), map(int, ...)으로 입력 파싱 | [05_02](2026_05_02_codingtest.ipynb), [05_03](2026_05_03_codingtest.ipynb), [05_22](2026_05_22_codingtest.ipynb) |
| 함수 설계 | 의사코드 주석으로 설계 후 코드 작성, 셀 풀이를 `def solution`으로 정리 | [05_14](2026_05_14_codingtest.ipynb), [05_16](2026_05_16_codingtest.ipynb), [05_18](2026_05_18_codingtest.ipynb), [05_21](2026_05_21_codingtest.ipynb), [05_23](2026_05_23_codingtest.ipynb) |

## 문제 해결

| 문제 | 처음 시도 결과 | 풀리지 않은 이유 | 해결 방법 | 파일 |
|---|---|---|---|---|
| 특정 부분 문자열 제거 | `ValueError: list.remove(x): x not in list`, 반복 시도 | `remove`는 값이 완전히 일치하는 원소만 삭제, 순회 중 같은 리스트를 변경 | 새 리스트를 만들고 조건에 맞는 원소만 append | [05_06](2026_05_06_codingtest.ipynb), [05_07](2026_05_07_codingtest.ipynb), [05_08](2026_05_08_codingtest.ipynb), [05_09](2026_05_09_codingtest.ipynb) |
| 연속 중복 제거 | 기대값과 다른 결과 (`[1,1,3,3,0,1,1]`이 `[1,3,0]`) | `not in answer`는 이미 담긴 모든 값과 비교해, 연속이 아닌 중복도 제거 | 마지막으로 담은 원소 `answer[-1]`과 비교 | [05_20](2026_05_20_codingtest.ipynb), [05_23](2026_05_23_codingtest.ipynb) |
| 가장 작은 수 제거 | 원소 순서가 달라짐 | `sort()`가 원본 리스트를 정렬 순서로 변경(in-place) | `min()`으로 최솟값을 찾고 `remove()`로 삭제 | [05_20](2026_05_20_codingtest.ipynb) |
| 연속 공백 문자열 | 빈 문자열 원소 발생, 또는 공백 정보 손실 | `split(" ")`와 `split()`의 분리 규칙 차이 | 용도에 맞게 선택: 공백 유지는 `split(" ")` + 빈 문자열 보존, 공백 정리는 `" ".join(s.split())` | [05_06](2026_05_06_codingtest.ipynb), [05_27](2026_05_27_codingtest.ipynb), [05_29](2026_05_29_codingtest.ipynb) |
| 단어별 대소문자 교체 | 단어가 바뀌어도 앞 단어의 홀짝 규칙이 이어짐 | 전체 문자열 인덱스 `i`를 기준으로 판단 | 단어 내 위치 카운터를 두고 공백에서 `0`으로 초기화 | [05_25](2026_05_25_codingtest.ipynb) |

### 순회 중 리스트 변경과 부분 문자열 검사

| 표현 | 설명 | 예시 |
|---|---|---|
| `x in list` | 리스트 원소 중 `x`와 같은 값이 있는지 확인 | `"ad" in ["abcd", "ad"]` 결과 `True` |
| `sub in str` | 문자열 안에 연속된 부분 문자열이 있는지 확인 | `"ad" in "abcd"` 결과 `False` |
| `list.remove(x)` | 값이 `x`인 첫 번째 원소 삭제 | 부분 문자열 검색 불가 |
| `[x for x in list if 조건]` | 조건에 맞는 원소만 새 리스트로 생성 | `[x for x in arr if "ad" not in x]` |

```python
nums = [1, 1, 2]
for x in nums:
    if x == 1:
        nums.remove(x)
print(nums)   # [1, 2]  (삭제 후 인덱스가 당겨져 두 번째 1을 건너뜀)
```

> 순회 중인 리스트의 원소를 삭제하면 인덱스가 당겨져 다음 원소를 건너뜀.
> 새 리스트(`answer`)를 만들어 조건에 맞는 원소만 담는 방식으로 해결.

### 중복 제거 방식 비교

| 방식 | 동작 | `[1,1,3,3,0,1,1]` 결과 |
|---|---|---|
| `if i not in answer` | 이미 담은 값은 다시 담지 않음 (전체 중복 제거) | `[1, 3, 0]` |
| `if answer[-1] != i` | 직전에 담은 값과 같을 때만 건너뜀 (연속 중복 제거) | `[1, 3, 0, 1]` |

> `answer[-1]`은 리스트의 마지막 원소.
> 빈 리스트에서는 `IndexError`가 나므로 `len(answer) == 0`을 먼저 검사해 첫 원소를 담음.

### 정렬과 최솟값 삭제

| 방법 | 설명 | 반환값 |
|---|---|---|
| `list.sort()` | 원본 리스트를 직접 정렬 (in-place) | `None` |
| `sorted(iterable)` | 원본 유지, 정렬된 새 리스트 생성 | 새 `list` |
| `min(list)` | 최솟값 반환 | 값 |
| `list.remove(min(list))` | 최솟값 1개 삭제, 나머지 순서 유지 | `None` |

> 정렬은 원소 순서를 바꿈. 원래 순서를 유지해야 하는 문제에는 정렬 대신 `min` + `remove` 사용.

### split 인자 차이

| 표현 | 동작 | 예시 (`s = "a  b"`) |
|---|---|---|
| `s.split()` | 연속 공백을 하나로 보고 분리, 앞뒤 공백 제거 | `['a', 'b']` |
| `s.split(" ")` | 공백 1개 기준으로 분리, 연속 공백은 빈 문자열 원소가 됨 | `['a', '', 'b']` |
| `" ".join(s.split())` | 연속 공백을 하나로 정리한 문자열 | `'a b'` |

> 공백 개수를 유지해야 하는 문제는 `split(" ")`로 나눈 뒤 빈 문자열 원소를 그대로 보존.
> 공백 개수가 의미 없는 문제는 `split()` 사용.

### 위치 카운터 초기화

```python
text = 0                  # 단어 안에서의 위치
for ch in s:
    if ch == ' ':
        text = 0          # 단어가 바뀌면 위치 초기화
        continue          # 현재 반복을 건너뜀
    # text가 짝수면 대문자, 홀수면 소문자 처리
    text += 1
```

> 전체 인덱스 `i`는 문자열 전체 기준 위치.
> 단어별 규칙은 단어 안의 위치를 따로 세는 카운터 변수가 필요.

## 개념 정리

5월 풀이 중 직접 정리한 개념 메모.

### 리스트 컴프리헨션 (List Comprehension)

```python
# for 루프
for i in range(5):
    result.append(i*2)

# 리스트 컴프리헨션
[i*2 for i in range(5)]
```

| 형태 | 설명 |
|------|------|
| 기본형 | `[반환값 for 변수 in 반복가능객체]` |
| 조건 필터링 | `[반환값 for 변수 in 반복가능객체 if 조건]` |
| 조건 표현식 | `[True일때 if 조건 else False일때 for 변수 in 반복가능객체]` |

| 형태 | 예시 | 결과 |
|------|------|------|
| 기본형 | `[i*2 for i in range(5)]` | `[0, 2, 4, 6, 8]` |
| 조건 필터링 | `[i for i in range(5) if i % 2 == 0]` | `[0, 2, 4]` |
| 조건 표현식 | `['짝' if i%2==0 else '홀' for i in range(4)]` | `['짝', '홀', '짝', '홀']` |

### 문자열 대소문자 변환

| 함수 | 설명 | 예시 |
|------|------|------|
| `upper()` | 모든 문자를 대문자로 변경 | `"hello".upper()` 결과 `"HELLO"` |
| `lower()` | 모든 문자를 소문자로 변경 | `"HELLO".lower()` 결과 `"hello"` |
| `swapcase()` | 대문자와 소문자를 서로 변환 | `"Hello".swapcase()` 결과 `"hELLO"` |
| `title()` | 각 단어의 첫 글자만 대문자, 나머지 소문자 | `"hello world".title()` 결과 `"Hello World"` |
| `capitalize()` | 문자열 전체에서 첫 글자만 대문자, 나머지는 모두 소문자로 변경 | `"hello world".capitalize()` 결과 `"Hello world"` |

> `title()`은 각 단어의 첫 글자를 대문자로, `capitalize()`는 문자열 전체에서 딱 한 번만 적용.
> `capitalize()`는 첫 글자 이후를 소문자로 강제 변환 (`"hELLO".capitalize()` 결과 `"Hello"`).

### 문자열 공백, 문자 제거

| 함수 | 설명 | 예시 |
|------|------|------|
| `strip("0")` | 문자열 양쪽의 "0" 제거 | `"007".strip("0")` 결과 `"7"` |
| `lstrip("0")` | 왼쪽의 "0"만 제거 | `"007".lstrip("0")` 결과 `"7"` |
| `rstrip("0")` | 오른쪽의 "0"만 제거 | `"700".rstrip("0")` 결과 `"7"` |

### 이스케이프 문자 (특수 문자 출력)

| 이스케이프 | 나타내는 문자 | 예시 |
|------|------|------|
| `\\` | 백슬래시 `\` | `print("\\")` 출력 `\` |
| `\"` | 큰따옴표 `"` | `print("\"hello\"")` 출력 `"hello"` |
| `\'` | 작은따옴표 `'` | `print('it\'s')` 출력 `it's` |

> `\` (백슬래시)는 뒤에 오는 문자를 특수하게 해석하는 이스케이프 문자.

```python
print('!@#$%^&*(\\\'\"<>?:;')  # 출력: !@#$%^&*(\'"<>?:;
```

### 문자열 교체

| 함수 | 설명 | 예시 |
|------|------|------|
| `replace(old, new)` | `old`를 찾아 `new`로 교체 | `"hello".replace("l", "r")` 결과 `"herro"` |
| `replace(old, new).replace(...)` | 메서드 체이닝으로 여러 교체 연속 적용 | `"aabbcc".replace("a","x").replace("b","y")` 결과 `"xxyycc"` |

> `replace()`는 원본 문자열을 변경하지 않고 새 문자열을 반환.
> `replace(str.upper(), str.lower())`처럼 전체 문자열을 인자로 넘기면 동작하지 않음. 교체할 개별 문자를 인자로 전달.

### 정렬

| 함수 | 설명 | 반환값 |
|------|------|--------|
| `sorted(iterable, key=None, reverse=False)` | 원본은 그대로, 새로운 정렬된 리스트 반환 | 새 `list` |
| `list.sort(key=None, reverse=False)` | 원본 리스트를 직접 수정하여 정렬 | `None` (in-place) |
| `"".join(sorted(s))` | 문자열의 각 문자를 오름차순 정렬 후 문자열로 결합 | 새 `str` |
| `"".join(sorted(s, reverse=True))` | 문자열의 각 문자를 내림차순 정렬 후 문자열로 결합 | 새 `str` |

> `sorted()`는 리스트 외 모든 반복 가능한 객체에 사용 가능, `sort()`는 리스트 전용 메서드.
> 문자열에 `sorted()`를 사용하면 리스트를 반환하므로, 문자열로 되돌리려면 `"".join()`으로 결합.

| 매개변수 | 설명 |
|----------|------|
| `iterable` | 정렬할 데이터 (`sorted()`만 해당) |
| `key` | 정렬 기준을 지정하는 함수 |
| `reverse` | `False`는 오름차순, `True`는 내림차순 |

```python
s = "hello"
sorted_s = "".join(sorted(s, reverse=True))
print(sorted_s)  # 출력: ollhe
```

> 문자열 정렬 기준은 유니코드 코드포인트 순서. 대문자(`A~Z`)가 소문자(`a~z`)보다 앞에 위치.

### map 함수

| 함수 | 설명 | 예시 |
|------|------|------|
| `map(function, iterable)` | 이터러블의 각 요소에 함수를 적용한 map 객체 반환 | `map(int, ["1","2","3"])` 결과 `<map object>` |
| `list(map(function, iterable))` | map 객체를 리스트로 변환 | `list(map(int, ["1","2","3"]))` 결과 `[1, 2, 3]` |

```python
num = "1 2 3 4 5".split()       # ["1", "2", "3", "4", "5"]
int_num = list(map(int, num))   # [1, 2, 3, 4, 5]
```

### 리스트 필터링

| 방법 | 설명 | 예시 |
|------|------|------|
| `"ad" in s` | 문자열에 부분 문자열 포함 여부 확인 | `"ad" in "abcd"` 결과 `False` |
| `[x for x in list if 조건]` | 조건에 맞는 원소만 새 리스트로 반환 | `[x for x in arr if "ad" not in x]` |
| `list.remove(x)` | 값이 정확히 일치하는 첫 번째 원소 삭제 | 부분 문자열 검색 불가 |

### 문자열 시작, 끝 확인

| 함수 | 설명 | 예시 |
|------|------|------|
| `startswith(prefix)` | 문자열이 지정한 문자(열)로 시작하면 `True` | `"hello".startswith("he")` 결과 `True` |
| `endswith(suffix)` | 문자열이 지정한 문자(열)로 끝나면 `True` | `"hello".endswith("lo")` 결과 `True` |

> 두 함수 모두 대소문자를 구분하며, `True` 또는 `False`를 반환.

### 산술 연산

| 함수 | 설명 | 예시 |
|------|------|------|
| `math.prod(iterable)` | 반복 가능한 객체 내 모든 요소의 곱을 반환 | `math.prod([2, 3, 4])` 결과 `24` |
| `sum(iterable)` | 반복 가능한 객체 내 모든 요소의 합을 반환 | `sum([2, 3, 4])` 결과 `9` |
| `math.fsum(iterable)` | 부동소수점 오차를 줄인 정밀한 합을 반환 | `math.fsum([0.1] * 10)` 결과 `1.0` (`sum([0.1] * 10)`은 `0.9999999999999999`) |
| `math.sqrt(x)` | x의 제곱근을 반환 | `math.sqrt(9)` 결과 `3.0` |
| `math.pow(x, y)` | x의 y 거듭제곱을 반환 | `math.pow(2, 3)` 결과 `8.0` |

> `sum()`은 built-in 함수로 `import` 없이 사용 가능, 나머지는 `import math` 필요.
> `math.sqrt()`와 `math.pow()`는 항상 float 타입을 반환.
> `math.pow(x, y)`는 `x ** y`와 결과가 같지만, `**`는 `int`도 반환 가능.

### 불리언 (Boolean)

| 값 | 설명 | 예시 |
|------|------|------|
| `True` | 참을 나타내는 불리언 값 | `1 == 1` 결과 `True` |
| `False` | 거짓을 나타내는 불리언 값 | `1 == 2` 결과 `False` |

> 파이썬의 불리언은 첫 글자가 대문자. `true`, `false`로 쓰면 오류 발생.

### 반복 가능한 객체 묶기 (zip)

| 함수 | 설명 | 예시 |
|------|------|------|
| `zip(*iterables)` | 여러 이터러블의 요소를 순서대로 쌍으로 묶어 반환 | `zip([1,2], ["a","b"])` 결과 `(1,"a"), (2,"b")` |
| `zip(*iterables, strict=False)` | `strict=True` 설정 시 길이가 다르면 오류 발생 | `zip([1,2,3], ["a","b"], strict=True)` 결과 `ValueError` |

> `zip()`은 가장 짧은 이터러블 기준으로 묶으며, `strict=True`를 사용하면 길이가 다를 때 `ValueError`를 발생시켜 실수를 방지.

```python
names  = ["Alice", "Bob", "David"]  # 3개
scores = [90, 85]                   # 2개

for name, score in zip(names, scores):
    print(name, score)  # 출력: Alice 90, Bob 85 (David는 짝이 없어서 제외)
```

> 기본값 `strict=False`일 때, 짧은 쪽에 맞춰 자동으로 멈춤.
> `"David"`가 조용히 무시되기 때문에 실수를 알아채기 어려움.

`strict=True`로 실수 방지

```python
for name, score in zip(names, scores, strict=True):
    print(name, score)  # ValueError: zip() has arguments with different lengths
```

> 길이가 다르면 오류를 발생시켜 데이터가 빠진 것을 바로 확인 가능.
> 두 리스트가 반드시 같은 길이여야 한다고 확신할 때 사용하면 좋음.

### 문자열 숫자 확인

| 함수 | 설명 | 예시 |
|------|------|------|
| `isdigit()` | 문자열이 0~9 범위의 숫자 문자(위첨자 등 포함)로만 이루어졌으면 `True` | `"123".isdigit()` 결과 `True` |
| `isnumeric()` | 문자열이 숫자로 표현 가능한 문자(분수, 거듭제곱 등 포함)로만 이루어졌으면 `True` | `"½".isnumeric()` 결과 `True` |

> 두 함수 모두 빈 문자열이면 `False`를 반환.

| 문자열 | `isdigit()` | `isnumeric()` |
|--------|-------------|---------------|
| `"123"` | `True` | `True` |
| `"²"` (위첨자) | `True` | `True` |
| `"½"` (분수) | `False` | `True` |
| `"a234"` | `False` | `False` |
| `"abc"` | `False` | `False` |

> 일반적인 정수 입력 검증에는 `isdigit()`으로 충분.
> 유니코드 숫자 문자까지 포함해야 한다면 `isnumeric()` 사용.

## 사용 라이브러리

- 외부 라이브러리: 없음
- 표준 라이브러리
  - `math`: `prod`(05_09), `sqrt`(05_16, 05_21), `ceil`(05_20)
  - `fractions`: `Fraction` 분수 덧셈(05_13)
  - `statistics`: `mean` 평균(05_16)

## 파일 구성

| 날짜 | 풀이 내용 |
|---|---|
| [05_02](2026_05_02_codingtest.ipynb) | 앞 n글자 슬라이싱, 입력 파싱, 조건에 따른 수열 변환 |
| [05_03](2026_05_03_codingtest.ipynb) | 대소문자 변환, f-string, 문자열 곱하기, 배열 원소 삭제, 자릿수 합, 정렬 후 슬라이싱 |
| [05_04](2026_05_04_codingtest.ipynb) | n의 배수, 뒤에서 5등까지, lstrip, 배열 비교, 길이별 인덱스 연산(시작) |
| [05_05](2026_05_05_codingtest.ipynb) | 길이별 인덱스 연산(완료), 문자열 겹쳐쓰기, 특수문자 출력, replace |
| [05_06](2026_05_06_codingtest.ipynb) | split 공백 처리 비교, 특정 부분 문자열 제거(시작) |
| [05_07](2026_05_07_codingtest.ipynb), [05_08](2026_05_08_codingtest.ipynb), [05_09](2026_05_09_codingtest.ipynb) | 특정 부분 문자열 제거(반복 시도 후 해결), 문자열 변환, 구간 계산, 홀짝 합, endswith, 식 계산 |
| [05_10](2026_05_10_codingtest.ipynb) | 병행 인덱스, 5명씩 묶기, 홀짝 번째 합, 앞뒤 합치기 |
| [05_11](2026_05_11_codingtest.ipynb) | zip 문자열 섞기, 카운트다운, 배수 배열, 9로 나눈 나머지 |
| [05_12](2026_05_12_codingtest.ipynb) | 간격 range, 카운트 업, split 후 정렬 |
| [05_13](2026_05_13_codingtest.ipynb) | 분수 덧셈, 중앙값, 홀수 배열 |
| [05_14](2026_05_14_codingtest.ipynb) | 부분 문자열 포함 확인, 문자열 4가지 경우 분기 |
| [05_15](2026_05_15_codingtest.ipynb) | 약수의 합, 자릿수 합, 뒤집은 리스트, 내림차순 정렬 |
| [05_16](2026_05_16_codingtest.ipynb) | `def solution` 정리(짝홀, 평균, 하샤드 수, 간격 수열), 정수 제곱근 판별(시작) |
| [05_17](2026_05_17_codingtest.ipynb) | break로 나머지 1 찾기, 두 정수 사이의 합 |
| [05_18](2026_05_18_codingtest.ipynb) | 대소문자 무시 개수 비교, 음양 더하기, 없는 숫자 더하기, 나누어 떨어지는 배열, 김서방 찾기 |
| [05_19](2026_05_19_codingtest.ipynb) | 콜라츠 추측, 핸드폰 번호 가리기 |
| [05_20](2026_05_20_codingtest.ipynb) | 제일 작은 수 제거, 내적, 가운데 글자, 같은 숫자는 싫어(1차) |
| [05_21](2026_05_21_codingtest.ipynb) | 수박수박수, 정수 제곱근 판별(완료), 문자열 다루기 기본 |
| [05_22](2026_05_22_codingtest.ipynb) | 직사각형 별 찍기, 행렬의 덧셈 |
| [05_23](2026_05_23_codingtest.ipynb) | 같은 숫자는 싫어(완료), 시저 암호(시작) |
| [05_24](2026_05_24_codingtest.ipynb) | 약수의 개수와 덧셈, 문자열 내림차순 배치, 부족한 금액 |
| [05_25](2026_05_25_codingtest.ipynb) | 최대공약수와 최소공배수(시작), 이상한 문자 만들기 |
| [05_26](2026_05_26_codingtest.ipynb) | 최댓값과 최솟값, JadenCase(시작) |
| [05_27](2026_05_27_codingtest.ipynb) | JadenCase 연속 공백 처리 |
| [05_28](2026_05_28_codingtest.ipynb) | JadenCase 정리, 올바른 괄호 |
| [05_29](2026_05_29_codingtest.ipynb) | JadenCase 공백 유지 방식으로 수정 |
| [05_30](2026_05_30_codingtest.ipynb) | x만큼 간격이 있는 n개의 숫자 |
| [05_31](2026_05_31_codingtest.ipynb) | 최솟값 만들기 |

