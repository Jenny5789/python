# Flet Projects

파이썬 이론으로 배운 내용을 Flet 데스크톱 앱 6개로 만들어 본 프로젝트 모음입니다.<br>
이벤트 처리 → 상태 관리 → 클래스 → DB 연동 순서로 연습했습니다.

---

## 🔢 UP-DOWN Game

> 컴퓨터가 고른 숫자를 UP / DOWN 힌트로 맞히는 게임 *(이벤트 처리 · 난수)*
>
> - 핵심: 입력 → 판정 → 출력 흐름을 30줄 단일 파일로 구현
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./up_down_game/images/updowngame.png" height="200"> <img src="./up_down_game/images/updown_up.png" height="200"> <img src="./up_down_game/images/updown_correct.png" height="200">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flet](https://img.shields.io/badge/Flet-555555?style=flat-square&logo=flutter&logoColor=white)
>
> [상세보기 →](./up_down_game/)

## ✊ Rock Paper Scissors

> 5판 3승제 가위바위보 게임 *(상태 관리 · `nonlocal`)*
>
> - 핵심: 라운드 진행과 승패 판정 로직을 GUI로 구현
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./RSP_game/images/home.png" height="300"> <img src="./RSP_game/images/round4.png" height="300"> <img src="./RSP_game/images/userwin.png" height="300">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flet](https://img.shields.io/badge/Flet-555555?style=flat-square&logo=flutter&logoColor=white)
>
> [상세보기 →](./RSP_game/)

## 📒 Phonenumber Book

> 연락처를 추가 · 검색 · 조회 · 삭제하는 앱 *(클래스 · 딕셔너리)*
>
> - 핵심: 연락처 추가 · 조회 · 삭제(CRUD) 구조를 클래스로 구현
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./phonenumber_book/images/home.png" height="300"> <img src="./phonenumber_book/images/add.png" height="300"> <img src="./phonenumber_book/images/list.png" height="300">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flet](https://img.shields.io/badge/Flet-555555?style=flat-square&logo=flutter&logoColor=white)
>
> [상세보기 →](./phonenumber_book/)

## 🧮 Number Data Handler

> 7종 연산 · 통계를 계산하는 앱 *(정규식 · 함수형과 클래스형 비교)*
>
> - 핵심: 같은 기능을 함수형과 클래스형으로 각각 구현해 구조 비교
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./Calculator/images/input.png" height="280"> <img src="./Calculator/images/output.png" height="280">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flet](https://img.shields.io/badge/Flet-555555?style=flat-square&logo=flutter&logoColor=white)
>
> [상세보기 →](./Calculator/)

## 🎳 Bowling Score

> 스트라이크 · 스페어를 반영해 점수를 계산하는 앱 *(점수 계산 알고리즘)*
>
> - 핵심: 프레임별 보너스 규칙을 반영한 점수 계산, 버튼 상태 제어
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./Bowling_score/images/home.png" height="200"> <img src="./Bowling_score/images/no3.png" height="200">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flet](https://img.shields.io/badge/Flet-555555?style=flat-square&logo=flutter&logoColor=white)
>
> [상세보기 →](./Bowling_score/)

## 🛒 POS System

> 편의점 POS와 관리자 화면을 갖춘 판매 시스템 *(SQLite · 집계 쿼리)*
>
> - 핵심: 딕셔너리로 설계한 장바구니 · 매출 시스템을 SQLite DB 연동 앱으로 확장
>
> <details>
> <summary>실행 화면</summary>
>
> <img src="./POS_system/images/pos.png" height="200"> <img src="./POS_system/images/admin_after.png" height="200">
>
> </details>
>
> ![Python](https://img.shields.io/badge/Python-555555?style=flat-square&logo=python&logoColor=white) ![Flet](https://img.shields.io/badge/Flet-555555?style=flat-square&logo=flutter&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-555555?style=flat-square&logo=sqlite&logoColor=white)
>
> [상세보기 →](./POS_system/)

---

## 실행 방법

```bash
pip install flet
cd <프로젝트 폴더>
python <실행 파일>
```

Flet은 버전에 따라 API 이름이 달라서, 실행이 안 되면 `pip install flet==<버전>`으로 버전을 맞춰 설치해야 합니다.
