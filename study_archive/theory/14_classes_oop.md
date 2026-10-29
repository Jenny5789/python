# 14. 클래스와 객체지향 프로그래밍 (OOP)

> 이미지: [note_49](assets/note_49_object_class_custom_exception.jpg) · [note_50](assets/note_50_class_method_inheritance_super.jpg) · [note_51](assets/note_51_overloading_overriding_multiple_inheritance.jpg) · [note_52](assets/note_52_polymorphism_complexnumber_polygon.jpg) · [note_47](assets/note_47_calculator_min_max_avg_class.jpg) · [note_38](assets/note_38_deep_copy_nested.jpg) · [note_54](assets/note_54_excel_pandas_class_method.jpg) · [note_55](assets/note_55_csv_module_dictreader.jpg)

> 순서 안내: 클래스 수업은 note_55(4/15 특강 표기)에서 시작해 note_49 -> 50 -> 51 -> 52로 이어지는 것으로 보이나 날짜가 없는 페이지가 많아 `[추정]`임.

## 1. 클래스란? (note_55, 4/15)
- 클래스 = 속성 + 메서드 (속성: 변수, 메서드: 함수)
- 절차는 개발자가 각성(각자 설계)해서 획일적이지 않다. 객체지향 방식 구현
- 방식 비교
  - 절차지향: 세부 작업을 순서대로 코드 작성
  - 함수지향: 세부 작업을 묶어서 유사한 기능을 함수로 정의, 함수 나열 방식으로 코드 작성
  - 객체지향: 클래스로 속성과 메서드를 묶어서 설계
- 노트 문구: "의도를 생각하자 (코드를 어떻게 작성해야 할지 등). 예) 왜 `{ }`를 사용하는지"

## 2. 객체지향 프로그래밍 개념 (note_49)
- OOP (Object-Oriented Programming) <-> 절차지향 (순차적으로 진행)
- 틀(class)을 만들어서 공유해서(반복해서) 사용 -> 일정함. 틀은 공유, 결과물(객체)은 각각 고유함
- class = 설계도(틀, 붕어빵 틀 같은 것) / 객체 = 결과물 (예: Red, Green 차량 옵션 -> 특성 적용)
- 객체지향 = 고유한 특성 + 각각의 특성을 묶어서 그 기반으로 `class`를 만듦
- 특징
  - 다중 패러다임 프로그래밍 (여러 가지 가능, 유사한 것끼리 묶음 -> 객체)
  - 재사용 (DRY: Don't Repeat Yourself) 가능한 코드 작성
  - class는 속성(변수)과 동작(함수)에 대한 정의. 예: 차량의 색상, 자동 주행 기능
  - object는 class의 인스턴스 (찍어놓은 data)
- 예: 사과 = Class, 사과1, 사과2, 사과3 = 인스턴스(object)
- 예: 게임 캐릭터

## 3. 클래스 정의, `__init__`, self, 속성 (note_49)
- `class Human:` 안의 변수
  - 클래스 속성(class attribute): 공통 특성이 있을 때 작성 (필수 아님). 예 `species = "Human"` -> 각각 같은 값
  - 인스턴스 속성(instance attribute): 각각의 특성 -> 각각 다른 값 (예 `name`, `age`)
- `def __init__(self, name, age)`: 필수! 객체를 만들 때 자동 호출되는 초기화 함수. `self`는 내가 만들 객체 자신(전지적 시점). 매개변수는 "내가 선언하고 있는 매개변수를 참조한다"
- `self`: 본인 class를 마음대로 사용 가능. 노트: `self`는 default라고 생각하면 됨

```python
class Human:
    species = "Human"              # class attribute: 모두 같은 값

    def __init__(self, name, age): # 객체를 만들 때 자동 호출
        self.name = name           # instance attribute: 각각 다른 값
        self.age = age

kim = Human("kim", 10)             # 노트의 KKKim
lee = Human("lee", 10)             # 노트의 LLLee
print(kim.species, kim.name, lee.name)   # Human kim lee
print(kim.species is lee.species)        # True (같은 class attribute)
```

## 4. 메서드 (note_50)
- method: class에 정의되어 있는 함수. `#instance method`
- 자기 자신을 참조하는 변수임을 알려야 하기 때문에 `self.name`을 사용
- `Human.dance(kim)`처럼 클래스 이름으로도 호출 가능 (노트: "Human.dance( )도 가능하다")

```python
class Human:
    species = "Human"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is dancing".format(self.name)

kim = Human("kim", 10)
print(kim.sing("HAPPY"))        # kim sings HAPPY
print(Human.dance(kim))         # kim is dancing  (클래스 이름으로 호출)
```

## 5. 상속 (Inheritance) (note_50)
- class는 "template": 많은 사람들이 가져다 이용 가능 + 필요에 따라 수정/변경 가능
- 상속: 공통적인 것을 뽑아 class로 만들고, 상속받는 것으로 많이 만들어 사용 -> 유지보수가 편해짐. 노트: "Class의 꽃 = 상속!!!"
- 부모 class의 속성, 메서드를 자식 class가 쓸 수 있음 (= 자식은 부모를 사용할 수 있다). 부모 class는 미리 선언되어 있어야 함
- 자식 class `class Penguin(Bird):`에서 `super().__init__()`: 부모 class 호출 -> 초기화 -> 객체를 동일하게 가짐
- `peggy = Penguin()`: 자기 자신 외에 필요한 값이 없으므로 `()` 안에 적지 않음 (`__init__`에 `self`만 있기 때문)
- 노트: 자식은 부모가 선언되어 있지 않아도 다른 template을 만들어 사용할 수 있음 (`[판독 불확실]`)

```python
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):                # child class
    def __init__(self):
        super().__init__()          # 부모 class 호출 + 초기화
        print("Penguin is ready")

    def whoisThis(self):            # 부모 메서드를 덮어씀
        print("Penguin")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()                        # 부모의 메서드를 그대로 사용
```
- 출력: `Bird is ready`, `Penguin is ready`, `Penguin`, `Swim faster`

## 6. 캡슐화 (Encapsulation) (note_50)
- method, 변수에 대한 접근 제한 / 직접적인 데이터 수정 방지 (class를 만든 쪽에서는 외부에서 변경/접근 못 하게)
- `self.__maxprice = 900`: 밑줄 두 개는 "클래스 내부에서만 사용할 거야"라는 뜻 (내부용, note_54)
- 노트 정리
  1. 위치가 클래스 내부이면 변경 가능
  2. 위치가 클래스 밖이면 항상 900 (밖에서 `__maxprice = 1000`을 써도 안 바뀜)
  3. 변경하려면 method가 존재해야 함 -> `def setMaxPrice(self, price)`

```python
class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()                  # Selling Price: 900
c.__maxprice = 1000       # 밖에서 값을 넣어도 내부 값은 그대로
c.sell()                  # Selling Price: 900
c.setMaxPrice(1000)       # method를 통해서만 변경
c.sell()                  # Selling Price: 1000
```
- 보충: `__maxprice`는 이름이 `_Computer__maxprice`로 바뀌는 방식이라 `c.__maxprice = 1000`은 에러가 아니라 새 속성이 하나 더 생기는 것

## 7. 다중상속 (note_51)
- 여러 부모를 한 번에 상속받는 구조 (그림 왼쪽: 부모 2개 -> 자식 1개)
- 그림 오른쪽: 단계 상속 (부모 -> 자식 -> 손자). 노트: "형식을 (자주) 사용한다 (현실적인 방법)", 예 GREEN -> GOLD -> VIP

```python
class Base1:
    def hello(self):
        return "Base1"

class Base2:
    def hello(self):
        return "Base2"
    def only2(self):
        return "only Base2"

class Derived(Base1, Base2):        # 다중상속
    pass

d = Derived()
print(d.hello())                    # Base1 (왼쪽 부모가 우선)
print(d.only2())                    # only Base2
print([c.__name__ for c in Derived.__mro__])   # ['Derived', 'Base1', 'Base2', 'object']

class Green: pass
class Gold(Green): pass
class VIP(Gold): pass
print(issubclass(VIP, Green))       # True
```

## 8. 특수 함수와 오버로딩 (Overloading) (note_51)
- 특수 함수: underscore 두 개(`__`)로 시작하는 함수. 의도하지 않아도 동작하는 함수, 필요할 때 알아서 호출됨
- `p1 + p2`에 있는 `+`는 class 함수에 저장되어 있는 특수 함수 `__add__` (노트: "특수 함수 사용 -> 너무 추천")
- 오버로딩(overloading): 같은 연산자가 상황에 따라 다르게 동작 (노트: "상황에 따라 합쳐?")
- `print(p1 + p2)` = `print(Point.__add__(p1, p2))`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):          # + 연산자 오버로딩
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):                 # print()가 호출하는 특수 함수
        return "({}, {})".format(self.x, self.y)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 + p2)                         # (3, 5)
print(Point.__add__(p1, p2))           # (3, 5)  위와 같은 호출
```
- 보충: 파이썬은 Java처럼 매개변수 개수만 다른 메서드를 여러 개 정의하는 오버로딩은 없고, 연산자 오버로딩(`__add__` 등)이 위의 의미

## 9. 오버라이딩 (Overriding) (note_51)
- 부모 class `A`의 메서드 `A1`을, 자식 class `B(A)`에서 같은 이름 `A1`로 다시 정의 -> 자식의 `A1`이 부모를 덮어쓰기 (= 부모 자원, 자식 새로 선언)
- "부모 선언 -> 자식에서 재세팅! (공통으로 사용 -> 자식들이 많이 다르게 사용함)"

```python
class A:
    def A1(self):
        return "부모의 A1"

class B(A):
    def A1(self):
        return "자식의 A1"             # 덮어쓰기

print(A().A1())   # 부모의 A1
print(B().A1())   # 자식의 A1
```

## 10. 다형성 (Polymorphism) (note_52)
- 공통 인터페이스를 사용해서 "조작"
- `Parrot`, `Penguin` 모두 `fly(self)`를 가지고 있고, `flying_test(bird)`는 `bird.fly()`를 호출한다고 가정하고 사용
- 객체 생성: `blu = Parrot()`, `peg = Penguin()` -> 객체를 넘기면 바로 `blu.fly`가 사용됨

```python
class Parrot:
    def fly(self):
        return "Parrot can fly"
    def swim(self):
        return "Parrot can't swim"

class Penguin:
    def fly(self):
        return "Penguin can't fly"
    def swim(self):
        return "Penguin can swim"

def flying_test(bird):                 # common interface
    return bird.fly()

blu = Parrot()                         # instantiate objects
peg = Penguin()
print(flying_test(blu))                # Parrot can fly
print(flying_test(peg))                # Penguin can't fly
```

## 11. 기본값 매개변수, 속성 추가, isinstance / issubclass (note_52)
- `ComplexNumber`: `def __init__(self, r=0, i=0)`: default 값이 존재 (값 지정 X -> 사용)
- `num2 = ComplexNumber(5)`, `num2.attr = 10`: template에 필요에 따라 속성을 추가해 넣을 수 있음 (객체 한정해서 넣어줌)
- 노트 메모: `del`을 사용하는 것보다 불필요한 class는 적게 만들자
- `isinstance()`: 상속받은 거니? / `issubclass()`: sub 클래스가 있니? -> 확인용 (상속 여부)

```python
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        return "{}+{}j".format(self.real, self.imag)

num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(5)                # i는 기본값 0
num2.attr = 10                         # 이 객체에만 속성 추가
print(num1.get_data(), num2.get_data(), num2.attr)   # 2+3j 5+0j 10
print(hasattr(num1, "attr"))           # False (다른 객체에는 없음)

class Animal: pass
class Dog(Animal): pass
d = Dog()
print(isinstance(d, Animal), isinstance(d, Dog))    # True True
print(issubclass(Dog, Animal), issubclass(Animal, Dog))   # True False
```
- `[판독 불확실]`: 노트의 `issubclass()` 설명은 "sub 클래스가 있니?"로 읽혔으나, 정확히는 "첫 번째 클래스가 두 번째 클래스의 자식인가?"를 확인

## 12. Polygon / Triangle 예제 (note_52)
- `class Polygon`: `__init__(self, no_of_sides)`에서 `self.n = no_of_sides`, `self.sides = [0 for i in range(no_of_sides)]` (노트: `for i in range(no ~): self.sides.append(0)`)
- `class Triangle(Polygon)`: 변이 3개인 도형으로 상속

```python
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = []
        for i in range(no_of_sides):
            self.sides.append(0)

    def input_sides(self, sides):
        self.sides = list(sides)

    def disp_sides(self):
        for i in range(self.n):
            print("Side", i + 1, "is", self.sides[i])

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)

    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

t = Triangle()
t.input_sides([3, 4, 5])
t.disp_sides()
print(t.find_area())                   # 6.0
```
- 보충: 노트에는 `Triangle`의 본문이 없어서 `find_area`는 일반적인 예제(헤론의 공식)로 채움

## 13. 계산기 클래스 (note_47)
- 목표: ① 계산기 - 리스트 입력받아서 `+`, `-`, `x`, `÷`, `avg`, `max`, `min`
- 숫자, 문자(연산자)를 구분해 예외처리 / 함수 단위로 만들기 / class 계산기
- 공통: 입력 후 연산. 입력 리스트 예: `cal = [a, +, b, +, c, +, d]` (숫자, 연산기호)
- 흐름: 입력 -> 숫자인가? T: 숫자 저장(`print`) / F: 연산자 -> `+`이면 점프 후 다음 연산자 / `else` 예외처리
  1. 숫자, 숫자 확인 (아니면 오류 알림) 2. 초기화 설정 3. 연산해 평균, 최대, 최소 구해
  - 숫자는 숫자대로, 연산자는 연산자대로 입력. 예: `1 + 2 + 3`, `1 - 2 - 3`, `1 x 2 x 3`, `1 ÷ 2 ÷ 3` 결과 확인
- 노트 메모: 계산기 - 버튼 누르면 입력 등등, 초기화 (deep copy 이용)

```python
class Calculator:
    OPS = ("+", "-", "*", "/")

    def __init__(self):
        self.reset()

    def reset(self):                       # 초기화
        self.numbers = []
        self.op = None

    def load(self, tokens):
        """tokens 예: [1, '+', 2, '+', 3]  숫자는 숫자대로, 연산자는 연산자대로"""
        self.reset()
        for t in tokens:
            if isinstance(t, (int, float)):
                self.numbers.append(t)
            elif t in self.OPS:
                if self.op is None:
                    self.op = t
                elif self.op != t:
                    raise ValueError("연산자는 한 종류만 사용합니다")
            else:
                raise ValueError("숫자 또는 연산자가 아닙니다: {!r}".format(t))
        if not self.numbers:
            raise ValueError("숫자가 없습니다")

    def calc(self):
        result = self.numbers[0]
        for n in self.numbers[1:]:
            if self.op == "+":
                result += n
            elif self.op == "-":
                result -= n
            elif self.op == "*":
                result *= n
            elif self.op == "/":
                result /= n
        return result

    def avg(self):
        return sum(self.numbers) / len(self.numbers)

    def max(self):
        return max(self.numbers)

    def min(self):
        return min(self.numbers)

c = Calculator()
for tokens in ([1, "+", 2, "+", 3], [1, "-", 2, "-", 3], [1, "*", 2, "*", 3], [1, "/", 2, "/", 3]):
    c.load(tokens)
    print(tokens[1], c.calc())             # 6, -4, 6, 0.1666...
c.load([4, "+", 8, "+", 6])
print(c.avg(), c.max(), c.min())           # 6.0 8 4
try:
    c.load([1, "+", "a"])
except ValueError as e:
    print("오류:", e)
```
- 보충: 노트의 "초기화"를 `reset()` 메서드로 구현. `max`/`min`/`avg`는 같은 입력 리스트로 계산

## 14. 전화번호부 클래스 (note_47, 38)
- 주제: 개인이름, 이메일 주소, 전화번호, 직장명 / 사용자 -> 개인정보 알려주면 저장 후 불러와 공유 / 검색을 통해 특정 정보를 알 수 있게
- 노트 메모
  - `(self, 개인정보: dict)`: "나는 dict로 사용할 거야"라고 알려주는 용도(타입 힌트)
  - `->`: 반환값은 ○○야라고 전달해주는 것
  - 전화번호부 `.items()`로 `for 사람정보 in self.전화번호부.items()` 반복, 일부만 가지고 검색
  - deep copy: 저장한 개인정보가 바깥에서 바뀌지 않도록 복사해서 보관 (계산기 초기화 등)

```python
import copy

class PhoneBook:
    def __init__(self):
        self.book = {}                       # {이름: 개인정보 dict}

    def add(self, info: dict) -> None:
        self.book[info["이름"]] = copy.deepcopy(info)   # 원본과 분리해서 저장

    def get(self, name: str) -> dict:
        return self.book.get(name)           # 없으면 None

    def search(self, keyword: str) -> list:
        """일부만 가지고 검색: 값 중 하나라도 keyword를 포함하면 결과에 포함"""
        found = []
        for name, info in self.book.items():
            if any(keyword in str(v) for v in info.values()):
                found.append(info)
        return found

pb = PhoneBook()
me = {"이름": "kim", "이메일": "kim@example.com", "전화번호": "010-1234-5678", "직장명": "ABC"}
pb.add(me)
pb.add({"이름": "lee", "이메일": "lee@example.com", "전화번호": "010-9999-0000", "직장명": "XYZ"})
me["전화번호"] = "changed"                  # 원본을 바꿔도 저장된 값은 그대로
print(pb.get("kim")["전화번호"])             # 010-1234-5678
print([x["이름"] for x in pb.search("010-12")])   # ['kim']
print([x["이름"] for x in pb.search("example")])  # ['kim', 'lee']
print(pb.get("park"))                        # None
```
- 사용 라이브러리: 표준 라이브러리 `copy`
- 보충: 예시 이메일 주소는 가상의 값(`example.com`)이며 노트의 실제 개인정보는 옮기지 않음

## 15. 클래스 설계 메모 (note_54)
- class 내부에는 "기능"만 있어서 설계할 때 "절차"를 가정해야 함. 훨씬 class가 많아진다 (일 단위/월 단위/품목별... 재고 관리 등)
- 예: `class DB 계산기 (DB 생성/관리)`, `# super -> 객체 생성`
- 관련: [12_shopping_cart_sales_system](12_shopping_cart_sales_system.md)의 7번 항목
