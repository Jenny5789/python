# python_basics

- 목적: 파이썬 기초 문법 연습 및 문제 풀이 기록
- 시기: 2026년 3월 22일, 4월 2일 (파일명 숫자는 작성일)

## 구현 경험
| 항목 | 구현 내용 | 파일 |
|---|---|---|
| 문자열 메서드 | `format`, `lower`, `upper`, `join`, `split`, `find`, `replace` 사용 예시 | [strformat](20260322_strformat.ipynb) |
| 요구사항 정리 | 마트 프로그램 필요 기능 3개 도출, 구현 전 결정 사항 정리 | [mart_db_TIL](20260402_mart_db_TIL.ipynb) |
| 자료구조 설계 | 중첩 딕셔너리(`{품목: {단가, 재고}}`)로 상품 DB 구성 | [mart_db_TIL](20260402_mart_db_TIL.ipynb) |
| 반복문 활용 | `for`문으로 87개 품목 데이터 일괄 생성·출력 | [mart_db_TIL](20260402_mart_db_TIL.ipynb) |
| 난수 활용 | `random`으로 단가·재고 임의 생성 | [mart_db_TIL](20260402_mart_db_TIL.ipynb) |

## 사용 라이브러리
- 표준 라이브러리: `random` (단가·재고 난수 생성, `mart_db_TIL`)
- 외부 라이브러리: 없음

## 파일 구성
| 파일 | 내용 |
|---|---|
| [`20260322_strformat.ipynb`](20260322_strformat.ipynb) | 문자열 메서드 예시 실습 |
| [`20260402_mart_db_TIL.ipynb`](20260402_mart_db_TIL.ipynb) | 마트 재고·매출 프로그램 문제 풀이 (TIL 형식) |

## 범위
- `mart_db_TIL`: 상품 DB 구성까지 구현
  - 상품 DB: 딕셔너리로 구현 (별도 DB 미사용)
  - 미구현: 장바구니 계산, 재고·매출 확인