## 📝 문자열 대소문자 변환
| 함수 | 설명 | 예시 |
|------|------|------|
| `upper()` | 모든 문자를 대문자로 변경 | `"hello".upper()` → `"HELLO"` |
| `lower()` | 모든 문자를 소문자로 변경 | `"HELLO".lower()` → `"hello"` |
| `swapcase()` | 대문자 ↔ 소문자 일괄 변환 | `"Hello".swapcase()` → `"hELLO"` |
| `title()` | 각 단어의 첫 글자만 대문자, 나머지 소문자 | `"hello world".title()` → `"Hello World"` |

## ✂️ 문자열 공백·문자 제거
| 함수 | 설명 | 예시 |
|------|------|------|
| `strip("0")` | 문자열 양쪽의 "0" 제거 | `"007".strip("0")` → `"7"` |
| `lstrip("0")` | 왼쪽의 "0"만 제거 | `"007".lstrip("0")` → `"7"` |
| `rstrip("0")` | 오른쪽의 "0"만 제거 | `"700".rstrip("0")` → `"7"` |

## 🔤 이스케이프 문자 (특수 문자 출력)
| 이스케이프 | 나타내는 문자 | 예시 |
|------|------|------|
| `\\` | 백슬래시 `\` | `print("\\")` → `\` |
| `\"` | 큰따옴표 `"` | `print("\"hello\"")` → `"hello"` |
| `\'` | 작은따옴표 `'` | `print('it\'s')` → `it's` |

> 💡 `\` (백슬래시)는 뒤에 오는 문자를 특수하게 해석하는 **이스케이프 문자**입니다.
> ```python
> print('!@#$%^&*(\\\'\"<>?:;')  # → !@#$%^&*(\'"<>?:;
> ```

## 🔁 문자열 교체
| 함수 | 설명 | 예시 |
|------|------|------|
| `replace(old, new)` | `old`를 찾아 `new`로 교체 | `"hello".replace("l", "r")` → `"herro"` |
| `replace(old, new).replace(...)` | 메서드 체이닝으로 여러 교체 연속 적용 | `"aabbcc".replace("a","x").replace("b","y")` → `"xxyycc"` |

> 💡 `replace()`는 원본 문자열을 변경하지 않고 **새 문자열을 반환**합니다.  
> 💡 `replace(str.upper(), str.lower())` 처럼 전체 문자열을 인자로 넘기면 동작하지 않습니다. 교체할 **개별 문자**를 인자로 넘겨야 합니다.

## 📋 정렬
| 함수 | 설명 | 반환값 |
|------|------|--------|
| `sorted(iterable, key=None, reverse=False)` | 원본은 그대로, 새로운 정렬된 리스트 반환 | 새 `list` |
| `list.sort(key=None, reverse=False)` | 원본 리스트를 직접 수정하여 정렬 | `None` (in-place) |
| `"".join(sorted(s))` | 문자열의 각 문자를 오름차순 정렬 후 문자열로 결합 | 새 `str` |
| `"".join(sorted(s, reverse=True))` | 문자열의 각 문자를 내림차순 정렬 후 문자열로 결합 | 새 `str` |

> 💡 `sorted()`는 **리스트 외 모든 반복 가능한 객체**에 사용 가능하고, `sort()`는 **리스트 전용** 메서드입니다.  
> 💡 문자열에 `sorted()`를 사용하면 **리스트를 반환**하므로, 문자열로 되돌리려면 `"".join()`으로 합쳐야 합니다.
>
> | 매개변수 | 설명 |
> |----------|------|
> | `iterable` | 정렬할 데이터 (`sorted()`만 해당) |
> | `key` | 정렬 기준을 지정하는 함수 |
> | `reverse` | `False` → 오름차순 / `True` → 내림차순 |
>
> ```python
> s = "hello"
> sorted_s = "".join(sorted(s, reverse=True))
> print(sorted_s)  # → "ollhe"
> ```
>
> 💡 문자열 정렬 기준은 **유니코드 코드포인트** 순서로, 대문자(`A~Z`)가 소문자(`a~z`)보다 앞에 옵니다.
>
## 🔍 리스트 필터링
| 방법 | 설명 | 예시 |
|------|------|------|
| `"ad" in s` | 문자열에 부분 문자열 포함 여부 확인 | `"ad" in "abcd"` → `False` |
| `[x for x in list if 조건]` | 조건에 맞는 원소만 새 리스트로 반환 | `[x for x in arr if "ad" not in x]` |
| `list.remove(x)` | 값이 정확히 일치하는 첫 번째 원소 삭제 | 부분 문자열 검색 불가 ❌ |

## 🔍 문자열 시작·끝 확인
| 함수 | 설명 | 예시 |
|------|------|------|
| `startswith(prefix)` | 문자열이 지정한 문자(열)로 시작하면 `True` | `"hello".startswith("he")` → `True` |
| `endswith(suffix)` | 문자열이 지정한 문자(열)로 끝나면 `True` | `"hello".endswith("lo")` → `True` |

> 💡 두 함수 모두 **대소문자를 구분**하며, `True` / `False`를 반환합니다.

## 🔢 산술 연산
| 함수 | 설명 | 예시 |
|------|------|------|
| `math.prod(iterable)` | 반복 가능한 객체 내 모든 요소의 **곱**을 반환 | `math.prod([2, 3, 4])` → `24` |
| `sum(iterable)` | 반복 가능한 객체 내 모든 요소의 **합**을 반환 | `sum([2, 3, 4])` → `9` |
| `math.fsum(iterable)` | 부동소수점 오차를 줄인 정밀한 **합**을 반환 | `math.fsum([0.1, 0.2])` → `0.3` |
| `math.sqrt(x)` | x의 **제곱근**을 반환 | `math.sqrt(9)` → `3.0` |
| `math.pow(x, y)` | x의 y **거듭제곱**을 반환 | `math.pow(2, 3)` → `8.0` |

> 💡 `sum()`은 built-in 함수로 `import` 없이 사용 가능하며, 나머지는 `import math`가 필요합니다.  
> 💡 `math.sqrt()`와 `math.pow()`는 항상 **float** 타입을 반환합니다.  
> 💡 `math.pow(x, y)`는 `x ** y`와 결과가 같지만, `**`는 `int`도 반환할 수 있습니다.

## ✅ 불리언 (Boolean)
| 값 | 설명 | 예시 |
|------|------|------|
| `True` | 참을 나타내는 불리언 값 | `1 == 1` → `True` |
| `False` | 거짓을 나타내는 불리언 값 | `1 == 2` → `False` |

> 💡 파이썬의 불리언은 **첫 글자가 대문자**입니다. `true` / `false`로 쓰면 오류가 발생합니다.

## 🔗 반복 가능한 객체 묶기
| 함수 | 설명 | 예시 |
|------|------|------|
| `zip(*iterables)` | 여러 이터러블의 요소를 **순서대로 쌍으로 묶어** 반환 | `zip([1,2], ["a","b"])` → `(1,"a"), (2,"b")` |
| `zip(*iterables, strict=False)` | `strict=True` 설정 시 길이가 다르면 **오류 발생** | `zip([1,2,3], ["a","b"], strict=True)` → ❌ |

> 💡 `zip()`은 가장 **짧은 이터러블 기준**으로 묶으며, `strict=True`를 사용하면 길이가 다를 때 `ValueError`를 발생시켜 실수를 방지할 수 있습니다.
>
> ```python
> names  = ["Alice", "Bob", "David"]  # 3개
> scores = [90, 85]                   # 2개
>
> for name, score in zip(names, scores):
>     print(name, score)  # Alice 90 / Bob 85 / David는 짝이 없어서 그냥 버려짐 ❌
> ```
>
> ⚠️ 기본값 `strict=False`일 때, **짧은 쪽에 맞춰** 자동으로 멈춥니다.  
> `"David"`가 조용히 무시되기 때문에 실수를 알아채기 어렵습니다.
>
> 🛡️ `strict=True`로 실수 방지
> ```python
> for name, score in zip(names, scores, strict=True):
>     print(name, score)  # ValueError: zip() has arguments with different lengths 🚨
> ```
> 💡 길이가 다르면 오류를 터뜨려서 데이터가 빠진 걸 바로 알 수 있습니다. 두 리스트가 반드시 같은 길이여야 한다고 확신할 때 사용하면 좋습니다.
> ```
>
## 🔢 문자열 숫자 확인
| 함수 | 설명 | 예시 |
|------|------|------|
| `isdigit()` | 문자열이 0~9 범위의 숫자 문자(위첨자 등 포함)로만 이루어졌으면 `True` | `"123".isdigit()` → `True` |
| `isnumeric()` | 문자열이 숫자로 표현 가능한 문자(분수, 거듭제곱 등 포함)로만 이루어졌으면 `True` | `"½".isnumeric()` → `True` |

> 💡 두 함수 모두 빈 문자열이면 `False`를 반환합니다.
>
> | 문자열 | `isdigit()` | `isnumeric()` |
> |--------|-------------|---------------|
> | `"123"` | `True` | `True` |
> | `"²"` (위첨자) | `True` | `True` |
> | `"½"` (분수) | `False` | `True` |
> | `"a234"` | `False` | `False` |
> | `"abc"` | `False` | `False` |
>
> ⚠️ 일반적인 정수 입력 검증에는 `isdigit()`으로 충분하지만,  
> 유니코드 숫자 문자까지 포함해야 한다면 `isnumeric()`을 사용하세요.
