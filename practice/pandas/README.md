# pandas

- 목적: pandas로 대기오염 측정 데이터 정리·시각화 학습
- 데이터: [에어코리아](https://www.airkorea.or.kr) 도시대기 측정망 2025년 5월 시도별·항목별 농도 (`data/airkorea.xlsx`)

## 구현 경험
| 항목 | 구현 내용 |
|---|---|
| 데이터 불러오기 | `read_excel`로 엑셀 읽기, `skiprows`로 머리글 건너뛰기, 헤더가 불규칙해 컬럼명 직접 지정 |
| 데이터 정리 | `dropna`로 빈 행 제거, `drop`으로 불필요한 열 제거, `reset_index`, 조건식으로 시도별 행 추출 |
| 이상 행 제거 | `apply`와 `lambda`로 숫자가 아닌 하단 주석 행 제거 |
| 파생 값 계산 | 전국 평균 대비 시도별 PM2.5 차이 계산 |
| 시각화 | `matplotlib` 막대그래프, 평균 초과·미만 색 구분, 전국 평균 기준선, 막대 위 수치 표시 |
| 한글 폰트 설정 | Colab에서 나눔고딕 설치 후 `matplotlib`에 등록, 음수 기호 깨짐 방지 |

## 사용 라이브러리
- 외부 라이브러리: `pandas`, `matplotlib` (`pyplot`, `font_manager`)
- 표준 라이브러리: 없음
- 환경: Google Colab, Python 3.12.13, 나눔고딕 폰트(`fonts-nanum`)

## 파일 구성
| 파일 | 내용 |
|---|---|
| [`air_pollution_pandas.ipynb`](air_pollution_pandas.ipynb) | 시도별 PM2.5 비교 분석 노트북 |
| [`data/airkorea.xlsx`](data/airkorea.xlsx) | 분석 데이터 (에어코리아) |

## 실행 방법
- Colab에서 노트북 실행
- `airkorea.xlsx`를 노트북과 같은 위치(Colab 세션 저장소)에 업로드 후 실행

## 범위
- 사용 시트: 3.1.1 시도별 항목별 농도 (엑셀 시트 3개 중 첫 번째)
- 분석 대상: 2025년 5월, 시도별 PM2.5 월평균 비교
- 불러오기만 하고 분석하지 않은 항목: SO2, NO2, O3, CO, PM10
- 미사용 시트: 3.1.2 도시별 항목별 농도, 3.1.3 주요도시 전년동월대비 농도

## 응용 프로젝트
- [hangang-water-quality](https://github.com/Jenny5789/hangang-water-quality): 한강 지점별 수질 분석, pandas 분석과 Streamlit 대시보드