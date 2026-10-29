# 04. 형변환, print, str.format, input

> 이미지: [note_07](assets/note_07_dict_typecasting_print.jpg) · [note_08](assets/note_08_format_input_import_operators.jpg) · [note_27](assets/note_27_summary_datatypes_print_format.jpg) · [note_28](assets/note_28_summary_input_import_namespace.jpg)

## 1. 형변환 (Type Casting)
- **암시적 형변환**: 파이썬이 자동으로 더 넓은 자료형으로 맞춤
  - 정수 + 실수는 실수
- **명시적 형변환**: 사용자가 직접 변환
  - `int()`, `float()`, `str()`, `list()` 등

```python
print(1 + 2.5)          # 3.5 (실수)
num_str = "10"
num = int(num_str)      # 문자열을 정수로
a = {1, 2, 2, 3, 4}
a2 = list(a)            # set을 list로
print(a2)               # [1, 2, 3, 4]
```

> 보충: 노트의 `list{1,2,3,4}`는 문법 오류이며, 소괄호를 쓰는 `list(...)`가 맞음.

## 2. print()
- 원형: `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
- `sep`: item 사이 구분자 (기본 공백)
- `end`: 출력 끝에 붙는 문자 (기본 줄바꿈)
- `file`, `flush`는 지금은 필요 없음 (모듈 내용)

```python
print(1, 2, 3, 4)                    # 1 2 3 4
print(1, 2, 3, 4, sep='*')           # 1*2*3*4
print(1, 2, 3, 4, sep='*', end='&')  # 1*2*3*4&
```

## 3. str.format()
- 문자열에 포맷을 적용하는 방법
- `{}` 자리에 값을 순서대로 채움

```python
x = 3
y = 5
print('~{}~{}'.format(x, y))   # ~3~5
```

### % 서식 (이전 방식)
- `%d`: 정수
- `%3.2f`: 실수. 소수점 이하 2자리까지 표시
  - 예: `12.4798`을 `%3.2f`로 출력하면 `12.48`
  - 보충: `3`은 전체 최소 너비, `.2`는 소수점 이하 자릿수. 반올림되므로 12.47이 아니라 **12.48**

```python
print('%3.2f' % 12.4798)   # 12.48
print('%d' % 7)            # 7
```

### 문자열 메서드 (숙제로 예제 만들기)
- `lower`, `upper`, `join`, `split`, `find`, `replace`

```python
s = "Hello World"
print(s.lower(), s.upper())            # hello world HELLO WORLD
print(s.split(" "))                    # ['Hello', 'World']
print("-".join(['a', 'b', 'c']))       # a-b-c
print(s.find("World"))                 # 6
print(s.replace("World", "Python"))    # Hello Python
```

## 4. input()
- 기본 반환값이 문자열
- 숫자로 쓰려면 적절히 형변환해서 사용

```python
num = input("숫자 입력: ")      # '3' (문자열)
num = int(num)                   # 정수로 변환
num = int(input("숫자 입력: "))  # 한 줄로 쓰는 방식
```
