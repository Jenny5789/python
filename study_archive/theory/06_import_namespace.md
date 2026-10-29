# 06. import, 모듈, 패키지, 네임스페이스

> 이미지: [note_10](assets/note_10_identity_operator_namespace.jpg) · [note_11](assets/note_11_namespace_scope_global_nonlocal.jpg) · [note_20](assets/note_20_module_package_import.jpg) · [note_28](assets/note_28_summary_input_import_namespace.jpg)

## 1. import
- 파이썬은 꼭 필요한 기능 외에는 기본으로 불러오지 않음
- 필요한 모듈을 가져오고, 파일 이름을 지정하면 코드에서 사용 가능해짐

### 전체 가져오기
```python
import math
print(math.pi)    # 모듈 이름을 붙여 사용
```

### 일부만 가져오기
```python
from math import pi
print(pi)         # 모듈 이름 없이 사용
```
- math에서 `pi`만 가져옴
- 코드 안에 `pi`라는 이름의 변수가 따로 있으면 충돌하므로 주의

### 별칭 (as)
```python
import math as m
print(m.pi)       # 모듈명은 math이고 별칭을 m으로 사용 (자주 쓰는 방식)
```

### 한 번 불러온 모듈은 다시 불러오지 않음
- 모듈을 수정한 뒤 다시 불러오려면 `importlib.reload()`로 강제 재로드
- 노트에는 `imp.reload()`로 적혀 있음. 보충: `imp` 모듈은 Python 3.12에서 제거되어 `importlib.reload()`를 사용

```python
import importlib
import math
importlib.reload(math)
```

## 2. dir()
- 모듈 안에 있는 구성 요소를 보고 싶을 때 사용
- `dir(math)`: math의 구성 요소를 모두 확인
- 인자 없이 `dir()`: 현재 작업 공간에 어떤 이름이 있는지 확인
- 버전에 따라 결과가 달라질 수 있으므로 비교 용도로 사용

```python
import math
print(dir(math)[:5])
```

## 3. 모듈과 패키지
- 모듈 (Modules): `import`로 불러다 쓰는 파이썬 파일 단위
- 패키지 (Package): 모듈을 계층 구조로 묶은 것 (클래스 개념처럼 가지가 갈라지는 구조)
- 보충 확인 항목
  - 파이썬 파일 위치 확인: `import sys; sys.path` (모듈을 찾는 경로 목록)
  - 로컬에서 만든 파일을 Colab이나 VS Code에서 쓸 때 호환 여부 확인 필요

## 4. 네임스페이스 (Namespace)
- 이름(Name)은 ID를 통해 주소를 알 수 있음
- 네임스페이스: 변수가 어디까지 사용 가능한지를 정하는 범위
- 들여쓰기가 코드 블록을 구분하는 규칙이라면, 네임스페이스는 이름을 찾는 규칙

### 탐색 순서
- 함수 안(local), 모듈(global), 내장(built-in) 순으로 가장 안쪽부터 바깥쪽으로 검색
- 이름은 dict처럼 관리됨
- 값을 함수 밖에서 쓰려면 `return`으로 내보내야 함

### 전역 변수와 지역 변수
- 전역 변수: 코드의 어느 위치에서나 접근 가능
- 지역 변수: 특정 코드 블록에서만 접근 가능 (함수, 클래스 안)

### 들여쓰기 수준별 예시
| 수준 | 의미 |
|---|---|
| LV1 | 가장 바깥, 전역 |
| LV2 | 함수 안, 지역 |
| LV3 | 중첩 함수 안 |

- 가장 안쪽 수준에서 이름을 찾고, 없으면 바깥 수준으로 올라가 찾음
- 안쪽(LV2)에서 만든 값은 바깥(LV1)에서 사용 불가

### global
```python
a = 10

def f():
    global a      # a는 전역 변수라고 선언
    a = 20        # 전역 변수 a가 바뀜

f()
print(a)          # 20
```
- `global` 없이 함수 안에서 `a = 20`을 하면 새로운 지역 변수가 만들어짐

### nonlocal
- 바로 바깥 함수의 변수에 접근할 때 사용

```python
def outer():
    a = 1
    def inner():
        nonlocal a
        a = 2
    inner()
    return a

print(outer())   # 2
```
- 값이 필요하면 매개변수로 넘기고 `return`으로 돌려받는 방식이 일반적이라 `nonlocal`은 거의 쓰지 않음
