# 📚 Study Archive

Python 이론 · 자료구조 구현 아카이브

## 📁 theory

파이썬 이론 노트. 전체 목차와 표기 규칙은 [theory/README.md](theory/README.md), 노트 스캔 이미지는 [theory/assets/](theory/assets/).

### 기초 문법

| 파일 | 내용 |
|---|---|
| [01_python_basics.md](theory/01_python_basics.md) | 특징, 키워드, 식별자, 들여쓰기, 주석 |
| [02_variables_literals.md](theory/02_variables_literals.md) | 변수, 상수, 리터럴, None |
| [03_data_types.md](theory/03_data_types.md) | 숫자, list, tuple, set, dict, 복사 |
| [04_type_casting_io.md](theory/04_type_casting_io.md) | 형변환, print, format, input |
| [05_operators.md](theory/05_operators.md) | 연산자 |
| [06_import_namespace.md](theory/06_import_namespace.md) | import, 모듈, 네임스페이스 |

### 흐름 제어와 함수

| 파일 | 내용 |
|---|---|
| [07_flow_control.md](theory/07_flow_control.md) | if, for, while, 리스트 컴프리헨션 |
| [08_functions.md](theory/08_functions.md) | 함수, lambda, 타입 힌트 |

### 문제 풀이와 실습

| 파일 | 내용 |
|---|---|
| [09_rps_game.md](theory/09_rps_game.md) | 가위바위보 게임 설계 |
| [10_practice.md](theory/10_practice.md) | 약수 구하기, 업다운 게임 |
| [11_algorithm_problems.md](theory/11_algorithm_problems.md) | 정렬, 비밀번호 검증, 소수, 볼링 점수 |
| [12_shopping_cart_sales_system.md](theory/12_shopping_cart_sales_system.md) | 장바구니, 매출 시스템 설계 |

### 예외, 클래스, 파일

| 파일 | 내용 |
|---|---|
| [13_exceptions.md](theory/13_exceptions.md) | 예외 처리 |
| [14_classes_oop.md](theory/14_classes_oop.md) | 클래스와 객체지향 |
| [15_file_io_csv_excel.md](theory/15_file_io_csv_excel.md) | 파일 입출력, csv, 엑셀 |

## 📁 data_structures

자료구조 구현. 파일별 주요 메서드는 [data_structures/README.md](data_structures/README.md).

### 기본 자료구조

| 파일 | 내용 |
|---|---|
| [00_bag.py](data_structures/00_bag.py) | 백(Bag) ADT |
| [01_list.py](data_structures/01_list.py) | 리스트 ADT |
| [02_line_editor.py](data_structures/02_line_editor.py) | 줄 편집기 |
| [03_set.py](data_structures/03_set.py) | 집합(Set) ADT |
| [data_structure_list.py](data_structures/data_structure_list.py) | 배열 구조 리스트, 연결된 구조 리스트 |

### 스택과 큐

| 파일 | 내용 |
|---|---|
| [04_stack.py](data_structures/04_stack.py) | 스택 ADT |
| [06_queue.py](data_structures/06_queue.py) | 선형 큐 ADT, 원형 큐 ADT |
| [08_deque.py](data_structures/08_deque.py) | 덱(Deque) ADT |
| [09_priorityqueue.py](data_structures/09_priorityqueue.py) | 우선순위 큐 ADT |

### 미로 탐색

| 파일 | 내용 |
|---|---|
| [05_DFS.py](data_structures/05_DFS.py) | 스택을 이용한 미로 탐색 (깊이 우선 탐색) |
| [07_BFS.py](data_structures/07_BFS.py) | 원형 큐를 이용한 미로 탐색 (너비 우선 탐색) |
| [10_maze.py](data_structures/10_maze.py) | 우선순위 큐를 이용한 미로 탐색 |

### 트리

| 파일 | 내용 |
|---|---|
| [tree.ipynb](data_structures/tree.ipynb) | 이진 트리 (순회, 노드 개수, 높이, 모르스 코드 결정 트리) |