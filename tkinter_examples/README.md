# tkinter 기초 예제

- 목적: tkinter 기본 위젯과 이벤트 처리 방식 학습
- 시기: 2026년 3월 (파일명 숫자는 작성일)

## 구현 경험
| 항목 | 구현 내용 | 파일 |
|---|---|---|
| 버튼 이벤트 처리 | 클릭 시 카운터 증감, `lambda` 콜백 | [0306](20260306_tkinter_basics.py), [0320](20260320_tkinter.py) |
| 키 입력 이벤트 | Enter 키로 입력값 처리 (`bind`) | [0306](20260306_tkinter_basics.py), [0309](20260309_tkinter.py) |
| 화면 상태 갱신 | `config`, `StringVar`로 Label 변경 | [0306](20260306_tkinter_basics.py), [0309](20260309_tkinter.py), [0320](20260320_tkinter.py) |
| 입력값 검증 | 빈 값 확인, `isdigit()` 숫자 검사, 경고 창 | [0309](20260309_tkinter.py) |
| 대화상자 | 안내 창, 예/아니오 확인 창 | [0320](20260320_tkinter.py) |
| 화면 배치 | `pack`, `Frame` 묶음, 폰트·색 스타일 | [0309](20260309_tkinter.py), [0320](20260320_tkinter.py) |

## 파일 구성
| 파일 | 내용 |
|---|---|
| [`20260306_tkinter_basics.py`](20260306_tkinter_basics.py) | 빈 창, 창 설정, Label 속성, Button 카운터, Entry + Enter 키 계산 |
| [`20260309_tkinter.py`](20260309_tkinter.py) | Label 스타일·`StringVar`, Entry 검증·읽기 전용, Text/ScrolledText, Frame |
| [`20260320_tkinter.py`](20260320_tkinter.py) | Button 클릭 이벤트, `lambda` 콜백, `messagebox` |

## 실행 방법
- `20260306_tkinter_basics.py`
  - 구성: 한 파일에 예제 여러 개 수록
  - 동작: 창 하나씩 순서대로 실행, 창 종료 시 다음 예제 창 실행
- `20260309_tkinter.py`
  - 구성: 앞부분 예제는 `'''`로 주석 처리
  - 동작: 마지막 Text 예제만 실행
- 주의: `eval` 사용 예제 포함, 학습용으로만 사용