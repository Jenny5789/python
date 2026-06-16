# SET ADT
# 데이터: 같은 유형의 유일한 요소들의 모임
# 원소들은 순서는 없지만 서로 비교할 수 있어야 함


class ADT_set:
    def __init__(self):
        self.maxsize = 10                 # 집합의 최대 크기
        self.bag     = [None] * self.maxsize  # 집합 초기화 (빈 자리 = None)
        self.length  = 0                  # 현재 저장된 원소 수


    # ── contain(e) ────────────────────────────────────
    # 집합에 원소 e가 있는지 검사
    # 매개변수: e(찾을 원소)
    # 반환값: 있으면 True, 없으면 False
    def contain(self, e):

        # 앞에서부터 순서대로 e 탐색
        for i in range(self.length):
            if self.bag[i] == e:  # e 발견
                return True       # 있음

        return False  # 끝까지 못 찾은 경우


    # ── insert(e) ─────────────────────────────────────
    # 새로운 원소 e를 삽입 (중복 삽입 허용 안 함)
    # 매개변수: e(삽입할 원소)
    # 반환값: 삽입 성공이면 True, 실패면 False
    def insert(self, e):

        # 가득 찬 경우 → 삽입 불가
        if self.length == self.maxsize:
            return False

        # 이미 존재하는 경우 → 중복 삽입 불가 (SET은 유일한 원소만 허용)
        if self.contain(e):
            return False

        # 맨 뒤에 e 삽입 (SET은 순서가 없으므로 위치 무관)
        self.bag[self.length] = e
        self.length += 1  # 원소 수 1 증가
        return True       # 삽입 성공


    # ── delete(e) ─────────────────────────────────────
    # 원소 e를 집합에서 삭제
    # 매개변수: e(삭제할 원소)
    # 반환값: 삭제된 원소, 실패면 None
    def delete(self, e):

        # 비어 있는 경우 → 삭제 불가
        if self.length == 0:
            return None

        # e의 위치를 탐색
        for i in range(self.length):
            if self.bag[i] == e:          # e 발견

                deleted = self.bag[i]     # 삭제할 원소 저장 (반환용)

                # SET은 순서가 없으므로 마지막 원소를 빈 자리로 이동
                # ex) [A, B, C, D] 에서 B 삭제 → [A, D, C, _]
                self.bag[i] = self.bag[self.length - 1]  # 마지막 원소를 삭제 자리로 이동
                self.bag[self.length - 1] = None          # 마지막 자리 비우기
                self.length -= 1                          # 원소 수 1 감소
                return deleted                            # 삭제된 원소 반환

        return None  # e가 집합에 없는 경우


    # ── isFull() ──────────────────────────────────────
    # 집합이 가득 찼는지 검사
    # 반환값: 가득 찼으면 True, 아니면 False
    def isFull(self):
        return self.length == self.maxsize  # 원소 수가 최대 크기와 같으면 가득 참


    # ── isEmpty() ─────────────────────────────────────
    # 집합이 공집합인지 검사
    # 반환값: 비어 있으면 True, 아니면 False
    def isEmpty(self):
        return self.length == 0  # 원소 수가 0이면 공집합


    # ── union(setB) ───────────────────────────────────
    # setB와의 합집합을 새로운 집합으로 반환 (self ∪ setB)
    # 매개변수: setB(합칠 집합)
    # 반환값: 합집합 결과 (새로운 ADT_set)
    def union(self, setB):
        result = ADT_set()  # 결과를 담을 새 집합 생성

        # 자신의 원소 전부 추가
        for i in range(self.length):
            result.insert(self.bag[i])

        # setB의 원소 중 중복되지 않는 것만 추가
        # insert 내부에서 contain으로 중복을 차단하므로 별도 검사 불필요
        for i in range(setB.length):
            result.insert(setB.bag[i])

        return result  # 합집합 반환


    # ── intersect(setB) ───────────────────────────────
    # setB와의 교집합을 새로운 집합으로 반환 (self ∩ setB)
    # 매개변수: setB(교집합을 구할 집합)
    # 반환값: 교집합 결과 (새로운 ADT_set)
    def intersect(self, setB):
        result = ADT_set()  # 결과를 담을 새 집합 생성

        # 자신의 원소 중 setB에도 있는 것만 추가
        for i in range(self.length):
            if setB.contain(self.bag[i]):  # setB에도 존재하는 경우 → 교집합 원소
                result.insert(self.bag[i])

        return result  # 교집합 반환


    # ── difference(setB) ──────────────────────────────
    # setB와의 차집합을 새로운 집합으로 반환 (self - setB)
    # 매개변수: setB(뺄 집합)
    # 반환값: 차집합 결과 (새로운 ADT_set)
    def difference(self, setB):
        result = ADT_set()  # 결과를 담을 새 집합 생성

        # 자신의 원소 중 setB에 없는 것만 추가
        for i in range(self.length):
            if not setB.contain(self.bag[i]):  # setB에 없는 경우 → 차집합 원소
                result.insert(self.bag[i])

        return result  # 차집합 반환


    # ── equals(setB) ──────────────────────────────────
    # setB와 같은 집합인지 검사
    # 매개변수: setB(비교할 집합)
    # 반환값: 같으면 True, 다르면 False
    def equals(self, setB):

        # 원소 개수가 다르면 바로 다름
        if self.length != setB.length:
            return False

        # 자신의 모든 원소가 setB에도 있는지 확인
        for i in range(self.length):
            if not setB.contain(self.bag[i]):  # 하나라도 없으면 다름
                return False

        return True  # 모든 원소가 일치 → 같은 집합


    # ── size() ────────────────────────────────────────
    # 집합의 원소 개수를 반환
    # 반환값: 현재 저장된 원소 수
    def size(self):
        return self.length  # self.length 가 곧 원소 수


    # ── display() ─────────────────────────────────────
    # 집합을 화면에 출력 (출력 전용 함수)
    # 반환값: 없음
    def display(self):

        # 공집합인 경우
        if self.length == 0:
            print("집합: {}  (공집합)")

        else:
            elements = self.bag[:self.length]      # None 제외하고 원소만 추출
            print(f"집합: {set(elements)}")        # set()으로 감싸 집합 표기법 { } 사용


#####################    TEST   ########################
s = ADT_set()

# ── isEmpty / isFull ──────────────────────────────────
print(s.isEmpty())   # True  → 비어 있음
print(s.isFull())    # False → 가득 차지 않음

# ── insert ────────────────────────────────────────────
print(s.insert(10))  # True  → 삽입 성공
print(s.insert(20))  # True  → 삽입 성공
print(s.insert(30))  # True  → 삽입 성공
print(s.insert(10))  # False → 중복 삽입 불가
s.display()          # 집합: {10, 20, 30}

# ── contain ───────────────────────────────────────────
print(s.contain(10))  # True  → 있음
print(s.contain(99))  # False → 없음

# ── delete ────────────────────────────────────────────
print(s.delete(20))   # 20   → 삭제 후 반환
print(s.delete(99))   # None → 없는 원소
s.display()           # 집합: {10, 30}

# ── size ──────────────────────────────────────────────
print(s.size())   # 2

# ── union ─────────────────────────────────────────────
s2 = ADT_set()
s2.insert(30)
s2.insert(40)
s2.insert(50)

result = s.union(s2)
result.display()   # 집합: {10, 30, 40, 50}  ← 30 중복 제거

# ── intersect ─────────────────────────────────────────
result = s.intersect(s2)
result.display()   # 집합: {30}  ← 공통 원소

# ── difference ────────────────────────────────────────
result = s.difference(s2)
result.display()   # 집합: {10}  ← s에만 있는 원소

# ── equals ────────────────────────────────────────────
s3 = ADT_set()
s3.insert(10)
s3.insert(30)

print(s.equals(s3))   # True  → 같은 집합
print(s.equals(s2))   # False → 다른 집합

# ── 가득 찬 경우 ────────────────────────────────────────
s4 = ADT_set()
for i in range(10):
    s4.insert(i)
print(s4.insert(99))  # False → 가득 참
print(s4.isFull())    # True

# ── 비어 있는 경우 ──────────────────────────────────────
s5 = ADT_set()
print(s5.delete(10))  # None  → 비어 있음
print(s5.isEmpty())   # True