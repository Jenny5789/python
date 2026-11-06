# Phonenumber Book &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<sup><sub>2026.04</sub></sup>

Flet으로 만든 전화번호부 앱.

연락처를 추가 · 검색 · 조회 · 삭제하고, 이름을 키로 하는 딕셔너리로 관리.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-02569B?style=for-the-badge)

<img src="./images/list.png" width="150" alt="연락처 목록 화면">

## 핵심 코드

### 연락처 추가

[flet_phonenumber_class.py](flet_phonenumber_class.py) · 이론 정리: [클래스](../../study_archive/theory/14_classes_oop.md) · [자료형](../../study_archive/theory/03_data_types.md) · [흐름 제어](../../study_archive/theory/07_flow_control.md)

빈 이름과 중복 이름을 먼저 막고, 이름을 키로 연락처 정보를 딕셔너리에 저장.

```python
def add_contact(self, e):
    name = self.name_field.value.strip()

    if not name:                              # 빈 이름 차단
        self.show_message("이름을 입력하세요!")
        return

    if name in self.phone_book:               # 중복 이름 차단
        self.show_message("이미 존재하는 이름입니다.")
        return

    self.phone_book[name] = {                 # 이름 → 연락처 정보
        "전화번호": self.phone_field.value.strip(),
        "이메일": self.email_field.value.strip(),
        "직업": self.job_field.value.strip()
    }

    self.clear_fields()
    self.refresh_list()                       # 카드 목록 다시 그림
    self.show_message("추가되었습니다.")       # SnackBar 안내
```

## 주요 기능

| 기능 | 설명 |
|---|---|
| 연락처 관리 | 추가, 이름 검색, 목록 조회, 삭제 |
| 입력 검증 | 빈 이름, 중복 이름 차단 |
| 카드 목록 | 연락처를 `ft.Card`로 나열, 카드별 삭제 버튼 |
| UI 재사용 | `create_menu_button()`, `create_card()`로 반복 UI 함수화 |
| 처리 안내 | `SnackBar`로 결과 메시지 표시 |

<details>
<summary>전체 화면 보기</summary>

| 시작 화면 | 추가 | 검색 |
|---|---|---|
| <img src="./images/home.png" width="120" alt="시작 화면"> | <img src="./images/add.png" width="120" alt="추가"> | <img src="./images/search.png" width="120" alt="검색"> |

</details>

## 개선 방향

- 수정 기능 추가, SQLite 연동으로 데이터 영속화
- 전화번호 · 이메일 형식 검증

## 파일 구조

```
phonenumber_book/
├── flet_phonenumber_class.py   # 전체 코드
├── images/                     # README 스크린샷
└── README.md
```

## 실행 방법

```
pip install flet
python flet_phonenumber_class.py
```
