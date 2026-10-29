# 12. 장바구니·매출 관리 시스템 설계와 DB(dict) 만들기

> 이미지: [note_33](assets/note_33_cart_sales_dict_design_0402.jpg) · [note_34](assets/note_34_cart_dict_get_none.jpg) · [note_39](assets/note_39_random_range_list_dict_0408.jpg) · [note_40](assets/note_40_sales_db_design.jpg) · [note_41](assets/note_41_computing_thinking_db_flow.jpg) · [note_54](assets/note_54_excel_pandas_class_method.jpg)

> 날짜 표기: note_33(4/2), note_39(4/8), note_40·41·54는 날짜 표기가 없는 같은 주제의 이어지는 페이지. 순서는 내용 흐름으로 정리함.

## 1. 문제 정의 (note_33, 4/2)
- 주제: 장바구니 가격, 매출 관리 / "System 설계"
- 필요한 정보: 물건, 단가, 재고, 할인 정보 등 -> DB로 따로 만들거나 자료구조로 저장한 뒤 활용
- 랜덤하게 장바구니에 담음
- 역할 구분
  - 고객: 물건을 담는다 -> 계산한다
  - 점원: 재고, 0으로 시작 + 계산 -> 0으로 초기화 (`.clear()`), 재고 파악
- 최종 산출물: PPT까지 (노트 상단 메모)

## 2. 자료 설계: list -> tuple/dict (note_33)
1. 물품명 `[ , , , , ]` 리스트
2. 항목: 품명, 단가, 재고, 구매개수, 총금액(= 단가 x 개수)
   - 단가: `random`(1000 ~ 30000원)으로 랜덤 추출
   - 재고: 50 ~ 70, 구매개수: 1 ~ 25 (`random.randint`)
   - 노트 메모: tuple로 index를 두고 list-up, `key: Value1, Value2, ...` 형태 -> dict로 `품명: 단가, 구매개수, 금액, 재고`
3. 총금액: `print(품명.pop(0))`처럼 하나씩 꺼내며 반복 (노트: "random -> 이중 for loop")
4. 필요한 것: 단가, 재고 -> `{품명: 정보}` 구조, 예 `{품명: {단가: ○원, 재고: ○}}`
5. 반복: `len(품명) > 0`인 동안 손님 pick -> `(품명: 단가) x (구매개수)`, `재고 = 재고 - 구매개수`, `len(품명) < 0`(<=0)이면 `break`

```python
import random

random.seed(0)                      # 결과를 재현하려고 고정 (노트에는 없음)
names = ["apple", "milk", "bread", "egg"]

# DB: {품명: {"단가": ..., "재고": ...}}
db = {}
for name in names:
    db[name] = {"단가": random.randint(1000, 30000),
                "재고": random.randint(50, 70)}

# 손님이 랜덤하게 장바구니에 담음 (장바구니: {품명: 구매개수})
cart = {}
for _ in range(6):
    name = random.choice(names)
    qty = random.randint(1, 25)
    if cart.get(name) != None:      # 이미 있으면 개수를 더함
        cart[name] = cart.get(name) + qty
    else:                           # 없으면 새로 만듦
        cart[name] = qty

total = 0
for name, qty in cart.items():
    total += db[name]["단가"] * qty   # 단가 x 구매개수
    db[name]["재고"] -= qty           # 재고 반영
print(len(cart) > 0, total > 0)      # True True
```
- 보충: 노트의 `(재고 = 단가 - 구매개수)`는 오기로 보이며 `재고 - 구매개수`가 맞음. 같은 품목을 두 번 담을 수 있으므로 장바구니는 dict로 개수를 합산하는 편이 간단함
- 사용 라이브러리: 표준 라이브러리 `random`

## 3. 장바구니를 list에서 dict로 바꾸기 (note_34)
- 장바구니에 이미 있으면 `+1`, 없으면 새로 만듦(`new`)
- 판단: `장바구니.get(key) != None`이면 존재 -> `장바구니.get(key) + 1`
- 새 항목 추가: `장바구니['key'] = 개수` (dict 항목 추가)
- 노트: "다음 시간에 이어서 해볼게요. 파일 공유 받은 다음에 한번 해오세요"

```python
cart = {}
for item in ["apple", "milk", "apple"]:
    if cart.get(item) != None:
        cart[item] = cart.get(item) + 1
    else:
        cart[item] = 1
print(cart)    # {'apple': 2, 'milk': 1}

# 같은 동작을 더 짧게
cart2 = {}
for item in ["apple", "milk", "apple"]:
    cart2[item] = cart2.get(item, 0) + 1
print(cart2 == cart)   # True
```
- 노트 후반(note_54): `[]`로 접근하면 key가 없을 때 오류 발생, `get()`은 오류가 발생하지 않음. 또는 `try` 수행 중 오류가 나면 `except`를 실행

## 4. 랜덤 학생 성적 데이터 (note_39, 4/8)
### 문제
- 1~6학년 초등학생. 학년마다 5~8반(random). 한 반은 20~30명(random). 과목: 국, 영, 수, 과
- 학생 모든 과목에 대한 성적을 하나의 변수에 저장
### 노트의 구조
- `학생 = {"국어": 국어, "영어": 영어, "수학": 수학, "과학": 과학, "학년": 학년, "반": 반}`
- `학년 = rand.randint(1, 6)`, `반 = rand.randint(5, 8)`, 각 반 학생 수 `rand.randint(20, 30)`(노트에서 지움 -> "알 필요 X")
- `for 학생 in range(len(학년(반(학생))))`: 전체 -> 학년 -> 반 -> 학생 순으로 접근, `print(학생[ ])`
- 소속: `학생[i]` = `학생[반][명]`, A 학생 -> [학년 반], [성적] "두 개 dict?"
- 오른쪽 메모: `물품명(단가)[재고]`를 `random`으로 뽑는 것과 같은 방식 (전체, 학생, 1반)

```python
import random as rand

rand.seed(1)
school = {}                              # {학년: {반: [학생, ...]}}
for grade in range(1, 7):
    classes = {}
    for cls in range(1, rand.randint(5, 8) + 1):   # 반 수 5~8
        students = []
        for _ in range(rand.randint(20, 30)):      # 학생 수 20~30
            students.append({
                "학년": grade, "반": cls,
                "국어": rand.randint(0, 100), "영어": rand.randint(0, 100),
                "수학": rand.randint(0, 100), "과학": rand.randint(0, 100),
            })
        classes[cls] = students
    school[grade] = classes

print(len(school))                              # 6
first = school[1][1][0]                         # 1학년 1반 첫 학생
print(sorted(first.keys()))
total_students = sum(len(s) for c in school.values() for s in c.values())
print(total_students > 6 * 5 * 20 - 1)          # True
```
- 보충: 노트의 "반 5~8" 표현은 "반이 5개~8개"로 읽어 `range(1, 반 수 + 1)`로 만들었음. 반 번호가 5~8번이라는 뜻이면 `rand.randint(5, 8)`을 반 번호로 쓰면 됨 (`[판독 불확실]`)

## 5. 컴퓨팅 사고력과 시나리오 (note_41)
- 컴퓨팅 사고력: "시나리오" 기반 -> 내가 만든 결과물을 사용자가 어떻게 활용할지 생각
  - 예: 무엇을 만들어, 누가 사용해, 어떻게 사용해? 내가 만들 때는 이런 걸 이렇게 <-> 사용자 입장에서 보기 -> 보완점 찾아 다시 수정, 반복
- WAY TO GO
  1. 상황: 계산 관련(계산원, 손님) / 물건, 물품 재고(관리자) / 매출(관리자)
  2. 상황에서 서로 연관이 있는지 파악 (공통, 특정 경우까지) -> 어떻게 할지 방식 맞춤
  3. 그 다음 코드 작성
- 풀이: 준비 -> 실제 수행 작업, 연습해보자
- [계산 concept]
  1. 장바구니 물건 총금액: 준비 = 물건, 물건 정보 (DB로 사용하겠다), 물건 정보를 어떻게 사용할 수 있는지
     - DB(물건): 물건 이름, 단가 필요 / DB에서 물건 가져오기: 물건 dict의 key 이용 / 작업: 단가를 누적해서 합한다
  2. 재고: 준비 = 현재 상황, 재고 변경 관련 인터페이스, 물건 추가/수정/삭제 기능 / 작업: 결제 후 재고 반영, 관리자의 물품 정보 변경
  3. DB에 물건명, 단가, 재고를 관리해야겠다로 확장해 나감
- DB 만들기: 품목명 `[ ]`로 두고 단가, 재고는 random으로 지정. `품목명.append(단가)`, `append(재고)`로 한 리스트에 섞어 넣는 방식은 X 표시 (구조가 섞임) -> `for i in range(len(품목명))`로 품목마다 dict 항목 만들기

## 6. 매출 기능 설계 (note_40)
### 매출 정리
- 준비: 판매 현황 기록 방법 결정 (품목별, 시간대, 하루 등등), 매출 기록 양식
- 매출 = 판매 - 원자재, 인건비 등 = 순수익 (-요인 파악)
- 작업: 매출 관련 양식, 재고 기입 (DB 확장 or 별도로 만들지 결정)
- 풀이: 필요한 기능을 list-up

| 영역 | 기능 |
|---|---|
| DB | 1-1 금액 계산, 1-2 재고 변경 관련, 1-3 매출 관련 |
| 물품 | 2-1 물품 관련 전반적인 관리, 2-2 현황 파악, 2-3 주문 진행할 것 |
| 매출 | 3-1 현황 파악, 3-2 수입/지출 관련 |

- "이런 기능을 이런 함수로 만들거다, 이런 경우에는 이렇게 적용시킬 거다": 문서 작업 중요 (엑셀, 파워포인트 등), DO NOT SKIP
- UI: 관리자용 / 계산 등 -> 하나로 묶여 있어야 한다. 공모전: 3~5개 이상 해보자(메모)
### 함수로 만들기 (오른쪽 메모)
- `def DB생성(매개변수)`: 내가 만들 함수 이름, 어떤 것을 받을지 정하는 매개변수
- `return`: 반환 방식, `global`: 전역 변수 만들어주는 방식 (DB 만들 때 필요)
- 2. 장바구니: 이중 for loop (랜덤하게 개수 뽑아) 또는 for -> 바구니 안에 있는지 check -> 있으면 count, 없으면 1로 초기화 (`?` 표시)

## 7. DB와 클래스로 확장 (note_54)
- 모듈: pandas, openpyxl (엑셀 관련). pandas = 엑셀 + 복합(데이터분석), openpyxl = 엑셀. 노트: "잠깐 잠깐 다뤄보자"
- DB, 단가, 재고, 매출기록: `def` 안에 -> DB 물품 class로 만들어 관리하도록 함
- `# 21. DB 품목 추가`: 링크 걸어서, 단가/재고가 문자로 되어 있으니 숫자로 형변환해서 사용
- `# 24. 빈 dict` -> DB로 사용, `# 32~36 header에 '주간 판매량' 추가`
- `# 42. [ ]`: key 값 없으면 오류 발생, `# 43. get()`: 오류 발생 X, `try` 안에서 수행하다 오류 발생 시 `except` 실행
- `class DB 계산기 (DB 생성/관리)`: `# super` -> 객체 생성
- 리스트 `remove`는 앞에서부터 찾아 제거 (뒤에는 남아 있음, `with key`), `pop`은 index로 찾아가기 때문에 dict에서는 못 쓴다 (dict의 `pop`은 key로 지움)
- `__`(밑줄 두 개): 클래스 내부에서만 사용할 거야 (내부용)
- class 내부에는 "기능"만 있어서 설계 시 "절차"를 가정해야 함. 훨씬 class가 많아짐 (일 단위/월 단위/품목별... 재고 관리)
- Flet -> (Database?) -> Java, HTML (노트 메모, `[판독 불확실]`)
- 계산기 / 전화번호 개념은 [14_classes_oop](14_classes_oop.md)에서 이어짐
