class ADT_Bag:
    def __init__(self):
        self.maxsize = 10              # 가방의 최대 크기
        self.bag = [None] * self.maxsize  # 가방 초기화 (빈 자리 = None)
        self.length = 0               # 현재 저장된 항목 수

    # ── insert(e): ─  ───────────────────────────────────
    #가방에 항목 e를 삽입
    # 삽입 성공이면 True, 실패(가득 참)면 False 반환
    def insert(self, e):

        # 가방이 가득 찬 경우 → 삽입 불가
        if self.length == self.maxsize:
            return False

        # 가방에서 빈 자리(None)를 앞에서부터 순서대로 탐색
        for i in range(self.maxsize):
            if self.bag[i] is None:   # 빈 자리 발견
                self.bag[i] = e       # 해당 자리에 항목 삽입
                self.length += 1      # 항목 수 1 증가
                return True           # 삽입 성공

        return False                  # 안전장치 (빈 자리를 못 찾은 경우)


    # ── remove(e) ─────────────────────────────────────
    # 가방에서 항목 e를 제거
    # 제거 성공이면 True, 실패(비어있거나 항목 없음)면 False 반환
    def remove(self, e):

        # 가방이 비어 있는 경우 → 제거 불가
        if self.length == 0:
            return False

        # 가방에 항목 e가 없는 경우 → 제거 불가
        if e not in self.bag:
            return False

        # 항목 e의 위치를 찾아서 제거 (None으로 되돌림)
        pos = self.bag.index(e)  # e가 있는 자리(인덱스) 탐색
        self.bag[pos] = None     # 해당 자리를 빈 자리로 변경
        self.length -= 1         # 항목 수 1 감소
        return True              # 제거 성공


    # ── __contains__(e) ──────────────────────────────────
    # 가방에 항목 e가 있는지 확인
    # 있으면 True, 없으면 False 반환
    # → 'e in bag' 형태로 사용 가능
    def __contains__(self, e):
        return e in self.bag


    # ── count() ──────────────────────────────────────
    #가방에 현재 저장된 항목 수를 반환
    def count(self):
        return self.length
    
######################    TEST  ########################
bag = ADT_Bag()

# ── insert 테스트 ──────────────────────────────────────
print(bag.insert(10))   # True  → 삽입 성공
print(bag.insert(20))   # True  → 삽입 성공
print(bag.insert(10))   # True  → 중복 허용이므로 삽입 성공

# ── count 테스트 ──────────────────────────────────────
print(bag.count())      # 3

# ── contains 테스트 ────────────────────────────────────
print(10 in bag)        # True  → 있음
print(99 in bag)        # False → 없음

# ── remove 테스트 ──────────────────────────────────────
print(bag.remove(10))   # True  → 제거 성공
print(bag.remove(99))   # False → 없는 항목
print(bag.count())      # 2

# ── 가득 찬 경우 ───────────────────────────────────────
for i in range(8):
    bag.insert(i)
print(bag.insert(99))   # False → 가득 참

# ── 비어 있는 경우 ──────────────────────────────────────
bag2 = ADT_Bag()
print(bag2.remove(10))  # False → 비어 있음
print(bag2.count())     # 0



