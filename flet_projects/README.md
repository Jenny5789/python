# Flet Projects

## 목표
- 파이썬 이론 학습 내용을 Flet GUI 앱으로 구현
- 입력·이벤트 처리 → 상태 관리 → 클래스 구조 → DB 연동 순으로 규모를 키우며 연습
- 이론 정리: [study_archive/theory](../study_archive/theory/README.md)

## 통합 역량
| 역량 | 구현 내용 | 프로젝트 | 이론 문서 |
|---|---|---|---|
| 이벤트 처리, 화면 상태 관리 | `on_click`, `on_change`, 상태 변경 후 `page.update()` | 전체 | [08_functions](../study_archive/theory/08_functions.md) |
| 객체지향 설계 | 클래스 기반 UI, `ft.Container` 상속, 속성으로 상태 관리 | Number Data Handler, Bowling Score, Phonenumber Book | [14_classes_oop](../study_archive/theory/14_classes_oop.md) |
| 자료구조 활용 | 딕셔너리(연락처, 장바구니), 리스트(롤 기록) | Phonenumber Book, POS System, Bowling Score | [03_data_types](../study_archive/theory/03_data_types.md) |
| 알고리즘 구현 | 프레임별 점수 계산(스트라이크·스페어 보너스), 승패 판정 | Bowling Score, Rock Paper Scissors | [11_algorithm_problems](../study_archive/theory/11_algorithm_problems.md), [09_rps_game](../study_archive/theory/09_rps_game.md) |
| 입력 검증, 예외 처리 | 정규식 숫자 판별, 비숫자 분류, 0 나눗셈 처리, `try/except` | Number Data Handler, POS System | [13_exceptions](../study_archive/theory/13_exceptions.md) |
| DB 연동 | SQLite 생성·조회·수정, 집계 쿼리, `?` 바인딩 | POS System | [12_shopping_cart_sales_system](../study_archive/theory/12_shopping_cart_sales_system.md) |
| 구조 비교 | 같은 기능을 함수형·클래스형으로 구현 | Number Data Handler | [08_functions](../study_archive/theory/08_functions.md), [14_classes_oop](../study_archive/theory/14_classes_oop.md) |

## 프로젝트
| 프로젝트명 | 한 줄 소개 | 핵심 기술 |
|---|---|---|
| [UP-DOWN Game](up_down_game/) | 숫자 맞추기 게임 (UP/DOWN 피드백) | 난수 비교, 이벤트 처리 |
| [Phonenumber Book](phonenumber_book/) | 연락처 추가·검색·조회·삭제 앱 | 클래스, 딕셔너리 |
| [Rock Paper Scissors](RSP_game/) | 5판 3승제 가위바위보 게임 | 상태 관리(`nonlocal`), 승패 판정 |
| [POS System](POS_system/) | 편의점 POS·관리자 시스템 | SQLite, 집계 쿼리 |
| [Number Data Handler](Calculator/) | 7종 연산·통계 계산 앱 | 정규식 파싱, 함수형·클래스형 비교 |
| [Bowling Score](Bowling_score/) | 스트라이크·스페어 반영 점수 계산 앱 | 점수 계산 알고리즘, 버튼 상태 제어 |

## 실행 방법
```bash
pip install flet
cd <프로젝트 폴더>
python <실행 파일>
```

| 프로젝트 | 실행 파일 |
|---|---|
| UP-DOWN Game | `up_down_game.py` |
| Phonenumber Book | `flet_phonenumber_class.py` |
| Rock Paper Scissors | `flet_RSP_game.py` |
| POS System | `flet_pos_system.py` |
| Number Data Handler | `flet_calculator_class.py` |
| Bowling Score | `flet_bowlingpoints.py` |

- 개발 시 사용한 Flet 버전: (`pip show flet` 결과를 여기에 기입)
- Flet은 버전에 따라 API 이름이 달라서, 위 버전으로 맞춰 설치 권장: `pip install flet==<버전>`