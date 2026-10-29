# 02. 변수와 리터럴

> 이미지: [note_02](assets/note_02_indentation_comments_variables.jpg) · [note_03](assets/note_03_constants_literals_string.jpg) · [note_04](assets/note_04_none_datatypes_number_list.jpg) · [note_26](assets/note_26_summary_features_literals.jpg)

## 1. 변수 (Variable)
- 데이터를 저장하기 위해 메모리에 지정된 위치에 붙인 이름
- 구성: 식별자 + 대입 연산자(`=`) + 리터럴
- 자료형은 대입된 값으로 추론됨
- 변수는 리터럴의 주소를 참조함 ("변수의 주소는 리터럴의 주소")

### 대입 과정 (`a = 10`)
- 대입 연산자를 찾음
- 리터럴 10을 기록하고 그 주소를 확인
- 변수 a를 위한 메모리를 확보
- a가 10의 주소를 가리키도록 저장

```python
a = 10
print(id(a))   # 리터럴 10의 주소
```

## 2. 상수 (Constant)
- 파이썬에는 값을 바꾸지 못하게 하는 상수가 없음
- C 언어는 `const int a = 10;`, `#define a 10`으로 상수 선언
- 파이썬에서는 다른 파일에 값을 두고 참조하는 방식으로 상수처럼 사용
  - 관례적으로 대문자 이름 사용 (예: `MAX_COUNT = 10`)

## 3. 리터럴 (Literal)
- 변수에 대입되는 가공되지 않은 원시 데이터
- 기본 리터럴: 숫자(Numeric), 문자열(String), 불리언(Boolean)

### 숫자 리터럴
| 종류 | 예시 | 비고 |
|---|---|---|
| 2진수 | `a = 0b1010` | 접두어 `0b` |
| 10진수 | `b = 100` | |
| 8진수 | `c = 0o310` | 접두어 `0o` |
| 16진수 | `d = 0x12C` | 접두어 `0x` |
| 실수 | `10.5`, `1.5e2` | `1.5e2`는 150.0 |
| 복소수 | `3.14j` | 허수부 `j` |

```python
print(0b1010, 100, 0o310, 0x12C)   # 10 100 200 300
print(1.5e2)                        # 150.0
```

### 불리언 리터럴
- `True`, `False`
- `1 == True`는 `True`

### 문자열 리터럴
- 파이썬에는 문자(char) 자료형이 없고 문자열만 존재 (C, C++은 char 사용)
- 작은따옴표, 큰따옴표, 여러 줄 따옴표 모두 가능
- 육안으로 12글자처럼 보여도 공백을 포함해 실제 글자 수를 센다
  - `"This is Python"`은 공백 포함 14자

```python
s = "This is Python"
print(len(s))   # 14
```

### 유니코드와 raw 문자열
- 유니코드: 키보드 입력이 유니코드에 약속된 코드로 전달되어 출력됨
- 컴퓨터 전원 켤 때 "삑" 소리처럼 유니코드 설정 덕분에 동작하는 사례도 있음
- raw 문자열: 이스케이프를 해석하지 않고 그대로 출력

```python
print(u"Ünicöde")   # Ünicöde
print(r"raw \n string")        # raw \n string
```

## 4. 특수 리터럴 (Special Literal)
- `None`: 참조값이 정해지지 않았을 때 (아직 기록할 수 없는 상태)
- 리터럴 모음: `list`, `tuple`, `set`, `dict`
  - 한 개의 변수에 여러 개의 item을 담음
  - 예: 회원 정보 이름, 나이, 주소를 하나로 묶음

## 5. 모든 것은 객체
- 클래스: 틀(설계도), 인스턴스(객체): 틀로 찍어낸 결과물
  - 자동차 설계도와 실제 자동차의 관계
- `type()`으로 자료형 확인, `isinstance(값, 자료형)`으로 검증 (True/False)

```python
print(type(10))                    # <class 'int'>
print(isinstance(1 + 2j, complex)) # True
```
