# 05. 연산자

> 이미지: [note_08](assets/note_08_format_input_import_operators.jpg) · [note_09](assets/note_09_assignment_operator.jpg) · [note_10](assets/note_10_identity_operator_namespace.jpg) · [note_28](assets/note_28_summary_input_import_namespace.jpg)

## 1. 산술 연산자
| 연산자 | 의미 | 예 | 결과 |
|---|---|---|---|
| `+` `-` `*` | 더하기, 빼기, 곱하기 | `3 * 2` | 6 |
| `/` | 나누기 (결과는 실수) | `7 / 2` | 3.5 |
| `%` | 나머지 | `7 % 2` | 1 |
| `//` | 몫 | `7 // 2` | 3 |
| `**` | 거듭제곱 (x의 y제곱) | `2 ** 3` | 8 |

## 2. 비교 연산자
- `>`, `<`, `==`, `!=`, `>=`, `<=`
- 결과는 True 또는 False
- 반복문에서는 `>=`, `<=`보다 `>`, `<`를 쓰는 편이 낫다고 정리 [판독 불확실]

## 3. 논리 연산자
- `and`, `or`, `not`
- 비교 결과(논리값)끼리 연결

```python
a, b = 0, 3
print((a == 0) and (b == 3))   # True
```

| A | B | A and B | A or B |
|---|---|---|---|
| T | T | T | T |
| T | F | F | T |
| F | T | F | T |
| F | F | F | F |

## 4. 비트 연산자
- `&` (AND), `|` (OR), `~` (NOT), `^` (XOR), `<<`, `>>` (시프트)
- 왼쪽 시프트 `<<`는 값을 2배, 오른쪽 시프트 `>>`는 값을 절반으로 만드는 효과

```python
print(5 << 1)   # 10 (5 * 2)
print(5 >> 1)   # 2  (5 // 2)
print(6 & 3, 6 | 3, 6 ^ 3)   # 2 7 5
```

## 5. 대입 연산자
- `a += 5`는 `a = a + 5`와 같음
- 학습 요령: 먼저 풀어 쓴 형태를 적어 보고, 그 다음 줄여 쓴 형태로 바꿈
- `-=`, `*=`, `/=`, `//=`, `%=`, `**=`도 같은 방식

```python
a = 10
a += 5      # a = a + 5
print(a)    # 15
```

## 6. 항등 연산자 (Identity)
- `is`, `is not`: 두 값이 같은 메모리 주소를 가리키는지 비교
- `id()`로 주소 확인
- `==`는 값이 같은지, `is`는 주소가 같은지 비교

```python
x1 = 5
y1 = 5
print(x1 is y1)               # True  (같은 주소)

l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 is l2)               # False (변경 가능한 객체는 따로 생성)
print(l1 == l2)               # True  (값은 같음)

a = 10
b = [10, 11]
print(id(a) == id(b[0]))      # True  (b 안의 10과 a는 같은 주소)
```
