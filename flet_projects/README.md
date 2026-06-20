# 🎨 Flet Projects Collection

Flet을 사용한 애플리케이션 모음입니다. 게임부터 유틸리티까지 다양한 GUI 프로젝트들 입니다.

## 📦 프로젝트 목록

### 6. 🎳 Bowling Score
정식 보링 점수 계산 애플리케이션. Strike, Spare, 10프레임 규칙 완벽 구현.
- **파일**: `bowling_score.py`
- **기능**: 점수 계산, 프레임 관리, 300점 퍼펙트 게임 지원
- **특징**: 다크 테마, 네온 오렌지 UI

### 5. 🔢 Number Data Handler
숫자 데이터 입력 및 7가지 통계 계산 애플리케이션.
- **파일**: `flet_calculator_class.py`
- **기능**: 합, 차, 곱, 나눗셈, 평균, 최대, 최소 계산
- **특징**: 클래스 기반, 에러 처리 (숫자 아닌 데이터 분류)

### 4. 💳 POS System 
편의점 판매 시스템. POS 모드와 ADMIN 모드.
- **파일**: `flet_매대계산기.py`
- **기능**: 상품 판매, 재고 관리, 매출 통계
- **특징**: SQLite DB, 카테고리 필터, 실시간 결제

### 3. ✊✌️✋ Rock Paper Scissors Game
5전 3승제 가위바위보 게임
- **파일**: `flet_RSP_game.py`
- **기능**: 컴퓨터 vs 플레이어, 라운드 추적, 최종 판정
- **특징**: 벚꽃 테마 (꽃, 나비), 분홍색 UI

### 2. 📞 Phonenumber Book 
연락처 관리 애플리케이션.
- **파일**: `flet_phonenumber_book.py`
- **기능**: 추가, 검색, 목록 조회, 삭제
- **특징**: 카드 디자인, 노란색 배경

### 1. ⬆️⬇️ UP-DOWN Game 
1~100 사이의 숫자를 맞추는 게임.
- **파일**: `up_down_game.py`
- **기능**: UP/DOWN 피드백, 시도 횟수 추적
- **특징**: 간단한 UI, 초보자 친화적

## 🛠️ 설치 및 실행

### 요구사항
```bash
python >= 3.8
flet >= 0.20
sqlite3 (POS 시스템용)
```

### 설치
```bash
pip install flet
```

### 각 프로젝트 실행
```bash
# 보링 점수
python bowling_score.py

# 숫자 계산기
python flet_calculator_class.py

# POS 시스템
python flet_매대계산기.py

# 가위바위보
python flet_RSP_game.py

# 전화번호부
python flet_phonenumber_book.py

# 업다운 게임
python up_down_game.py
```

## 📁 디렉토리 구조

```
flet_projects/
├── README.md (이 파일)
├── bowling_score/
│   ├── bowling_score.py
│   ├── README.md
│   └── images/
├── calculator/
│   ├── flet_calculator_class.py
│   ├── README.md
│   └── images/
├── pos_system/
│   ├── flet_매대계산기.py
│   ├── mart.db
│   ├── README.md
│   └── images/
├── rsp_game/
│   ├── flet_RSP_game.py
│   ├── README.md
│   └── images/
├── phonenumber_book/
│   ├── flet_phonenumber_book.py
│   ├── README.md
│   └── images/
└── up_down_game/
    ├── up_down_game.py
    ├── README.md
    └── images/
```
