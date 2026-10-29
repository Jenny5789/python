# 파이썬 기초 이론 정리

손글씨 수업 노트(2026-03-11 ~ 03-26 30장 + 4월 25장, 총 55장)를 주제별로 옮겨 적은 문서입니다. 원본 이미지는 `assets/`에 있고, 각 문서 상단에서 해당 페이지로 연결됩니다.

## 목차
| 문서 | 내용 | 원본 노트 |
|---|---|---|
| [01_python_basics](01_python_basics.md) | 특징, 키워드, 식별자, 문장, 들여쓰기, 주석, 독스트링 | note_01, 02, 26 |
| [02_variables_literals](02_variables_literals.md) | 변수, 상수, 리터럴, None, 객체 | note_02, 03, 04, 26 |
| [03_data_types](03_data_types.md) | 숫자, list, tuple, string, set, dict 비교 | note_04 ~ 07, 27 |
| [04_type_casting_io](04_type_casting_io.md) | 형변환, print, str.format, input | note_07, 08, 27, 28 |
| [05_operators](05_operators.md) | 산술, 비교, 논리, 비트, 대입, 항등 연산자 | note_08 ~ 10, 28 |
| [06_import_namespace](06_import_namespace.md) | import, 모듈, 패키지, 네임스페이스, global, nonlocal | note_10, 11, 20, 28 |
| [07_flow_control](07_flow_control.md) | if, for, range, while, break, continue, pass | note_12 ~ 15, 29 |
| [08_functions](08_functions.md) | def, return, 인자, 재귀, lambda, filter, map | note_15, 17 ~ 19, 30 |
| [09_rps_game](09_rps_game.md) | 가위바위보 5판 3승 설계와 최종 코드 | note_22 ~ 25, 30 |
| [10_practice](10_practice.md) | 약수 구하기, 업다운 게임 | note_16, 17, 21 |
| [11_algorithm_problems](11_algorithm_problems.md) | 정렬(3개 -> N개), 비밀번호 검증, 소수 판별, 볼링 점수 | note_31, 32, 41~46 |
| [12_shopping_cart_sales_system](12_shopping_cart_sales_system.md) | 장바구니·매출 시스템 설계, dict DB, 랜덤 데이터 | note_33, 34, 39~41, 54 |
| [13_exceptions](13_exceptions.md) | try/except/else/finally, raise, assert, 사용자 정의 예외 | note_47~49, 53 |
| [14_classes_oop](14_classes_oop.md) | 클래스, 상속, 캡슐화, 오버로딩/오버라이딩, 다형성, 계산기, 전화번호부 | note_38, 47, 49~52, 54, 55 |
| [15_file_io_csv_excel](15_file_io_csv_excel.md) | open/with, os/shutil, csv, pandas/openpyxl | note_48, 53~55 |

4월 노트 중 일부는 기존 문서에 합쳤습니다: 03(dict/list 메서드, 복사, Decimal 등: note_35, 37, 38), 07(리스트 컴프리헨션: note_36), 08(타입 힌트: note_38).

## 표기 규칙
- `[판독 불확실]`, `[추정]`: 손글씨를 확실히 읽지 못한 부분
- `보충`: 노트 내용과 사실이 달라서 바로잡거나 덧붙인 부분
- 코드 예제는 모두 실행해서 확인했고, 표준 라이브러리(`random`, `math`, `copy`, `csv`, `os` 등)를 썼습니다. 엑셀 예제만 `pandas`, `openpyxl`이 필요합니다.

## 이미지 폴더
- `assets/`: `note_01_...jpg` ~ `note_55_...jpg`
  - note_01 ~ 30은 날짜순 번호
  - note_01 ~ 09: 3/11~12
  - note_10 ~ 21: 3/18~19
  - note_22 ~ 25: 3/25
  - note_26 ~ 30: 3/26 요약
  - note_31 ~ 55 (4월): 날짜가 적힌 페이지가 일부뿐이라 번호가 정확한 날짜순이 아닐 수 있음 (확인된 날짜: note_31 4/1, note_33 4/2, note_39 4/8, note_48 4/9, note_55 4/15, note_46 4/16, note_42 4/22)
