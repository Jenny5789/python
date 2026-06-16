class ADT_list:
    def __init__(self):
        self.maxsize = 10                 # 리스트의 최대 크기
        self.bag = [None] * self.maxsize  # 리스트 초기화 (빈 자리 = None)
        self.length = 0                   # 현재 저장된 항목 수


    # ── isEmpty() ─────────────────────────────────────
    # 리스트가 비어 있는지 검사
    # 반환값: 비어 있으면 True, 아니면 False
    def isEmpty(self):
        return self.length == 0


    # ── isFull() ──────────────────────────────────────
    # 리스트가 가득 찼는지 검사
    # 반환값: 가득 찼으면 True, 아니면 False
    def isFull(self):
        return self.length == self.maxsize


    # ── insert(pos, e) ────────────────────────────────
    # pos 위치에 새로운 요소 e를 삽입
    # 반환값: 삽입 성공이면 True, 실패면 False
    def insert(self, pos, e):

        # 범위를 벗어난 경우 → 삽입 불가
        if pos < 0 or pos > self.length:
            return False

        # 가득 찬 경우 → 삽입 불가
        if self.length == self.maxsize:
            return False

        # pos 위치에 자리를 만들기 위해 뒤에서부터 한 칸씩 밀기
        # ex) [A, B, C, _]에 pos=1 삽입 → [A, _, B, C]
        for i in range(self.length, pos, -1):
            self.bag[i] = self.bag[i - 1]  # 한 칸 뒤로 이동

        self.bag[pos] = e   # pos 위치에 e 삽입
        self.length += 1    # 항목 수 1 증가
        return True         # 삽입 성공


    # ── delete(pos) ───────────────────────────────────
    # pos 위치에 있는 요소를 삭제하고 반환
    # 반환값: 삭제된 요소, 실패면 None
    def delete(self, pos):

        # 범위를 벗어난 경우 → 삭제 불가
        if pos < 0 or pos >= self.length:
            return None

        # 비어 있는 경우 → 삭제 불가
        if self.length == 0:
            return None

        deleted = self.bag[pos]  # 삭제할 요소 저장 (나중에 반환하기 위해)

        # 삭제 후 빈 자리를 채우기 위해 앞에서부터 한 칸씩 당기기
        # ex) [A, B, C, D]에서 pos=1 삭제 → [A, C, D, _]
        for i in range(pos, self.length - 1):
            self.bag[i] = self.bag[i + 1]  # 한 칸 앞으로 이동

        self.bag[self.length - 1] = None  # 마지막 자리 빈 자리로 변경
        self.length -= 1                  # 항목 수 1 감소
        return deleted                    # 삭제된 요소 반환


    # ── getEntry(pos) ─────────────────────────────────
    # pos 위치에 있는 요소를 반환
    # 반환값: 해당 요소, 실패면 None
    def getEntry(self, pos):

        # 범위를 벗어난 경우 → 반환 불가
        if pos < 0 or pos >= self.length:
            return None

        return self.bag[pos]  # 해당 위치의 요소 반환


    # ── size() ────────────────────────────────────────
    # 리스트 안의 요소 개수를 반환
    # 반환값: 현재 저장된 항목 수
    def size(self):
        return self.length


    # ── clear() ───────────────────────────────────────
    # 리스트를 초기화
    # 반환값: 없음
    def clear(self):
        self.bag = [None] * self.maxsize  # 가방을 빈 상태로 초기화
        self.length = 0                   # 항목 수 0으로 초기화


    # ── find(item) ────────────────────────────────────
    # 리스트에서 item의 인덱스를 반환
    # 반환값: 찾으면 인덱스, 없으면 -1
    def find(self, item):

        # 앞에서부터 순서대로 item 탐색
        for i in range(self.length):
            if self.bag[i] == item:  # item 발견
                return i             # 해당 인덱스 반환

        return -1  # 끝까지 못 찾은 경우


    # ── replace(pos, item) ────────────────────────────
    # pos 위치의 항목을 item으로 교체
    # 반환값: 성공이면 True, 실패면 False
    def replace(self, pos, item):

        # 범위를 벗어난 경우 → 교체 불가
        if pos < 0 or pos >= self.length:
            return False

        self.bag[pos] = item  # 해당 위치의 항목을 item으로 교체
        return True           # 교체 성공


    # ── sort() ────────────────────────────────────────
    # 리스트의 항목들을 오름차순으로 정렬 (버블 정렬)
    # 반환값: 성공이면 True, 실패(비어 있음)면 False
    def sort(self):

        # 비어 있는 경우 → 정렬 불가
        if self.length == 0:
            return False

        # 버블 정렬: 인접한 두 요소를 비교해 큰 값을 뒤로 보냄
        # i가 증가할수록 뒤쪽은 이미 정렬된 상태이므로 범위에서 제외
        for i in range(self.length - 1):
            for j in range(self.length - 1 - i):
                if self.bag[j] > self.bag[j + 1]:
                    self.bag[j], self.bag[j + 1] = self.bag[j + 1], self.bag[j]  # 두 요소 위치 교환

        return True  # 정렬 성공


    # ── merge(lst) ────────────────────────────────────
    # 다른 리스트 lst를 현재 리스트에 추가
    # 반환값: 실제로 추가된 항목 수
    def merge(self, lst):
        count = 0  # 추가된 항목 수 카운트

        for i in range(lst.length):

            # 용량 초과 시 중단
            if self.length == self.maxsize:
                break

            self.bag[self.length] = lst.bag[i]  # 현재 리스트 맨 뒤에 항목 추가
            self.length += 1                     # 항목 수 1 증가
            count += 1                           # 추가된 항목 수 1 증가

        return count  # 실제로 추가된 항목 수 반환


    # ── display() ─────────────────────────────────────
    # 리스트를 화면에 출력 (출력 전용 함수)
    # 반환값: 없음
    def display(self):

        # 비어 있는 경우
        if self.length == 0:
            print("리스트가 비어 있습니다.")
        else:
            # self.bag[:self.length] → None 제외하고 항목만 출력
            print(f"리스트 (크기: {self.length}): {self.bag[:self.length]}")


    # ── append(e) ─────────────────────────────────────
    # 리스트의 맨 뒤에 새로운 항목을 추가
    # 반환값: 성공이면 True, 실패(가득 참)면 False
    def append(self, e):

        # 가득 찬 경우 → 추가 불가
        if self.length == self.maxsize:
            return False

        self.bag[self.length] = e  # 현재 마지막 자리 다음에 e 추가
        self.length += 1           # 항목 수 1 증가
        return True                # 추가 성공


#####################     TEST  ##########################
lst = ADT_list()

# ── isEmpty / isFull ──────────────────────────────────
print(lst.isEmpty())   # True  → 비어 있음
print(lst.isFull())    # False → 가득 차지 않음

# ── append ────────────────────────────────────────────
print(lst.append(10))  # True  → 삽입 성공
print(lst.append(20))  # True  → 삽입 성공
print(lst.append(30))  # True  → 삽입 성공
lst.display()          # 리스트 (크기: 3): [10, 20, 30]

# ── insert ────────────────────────────────────────────
print(lst.insert(1, 99))   # True  → 1번 자리에 99 삽입
lst.display()               # 리스트 (크기: 4): [10, 99, 20, 30]
print(lst.insert(-1, 99))  # False → 범위 벗어남

# ── delete ────────────────────────────────────────────
print(lst.delete(1))   # 99    → 1번 자리 삭제 후 반환
lst.display()          # 리스트 (크기: 3): [10, 20, 30]
print(lst.delete(99))  # None  → 범위 벗어남

# ── getEntry ──────────────────────────────────────────
print(lst.getEntry(0))   # 10   → 0번 자리 요소 반환
print(lst.getEntry(99))  # None → 범위 벗어남

# ── size ──────────────────────────────────────────────
print(lst.size())   # 3

# ── find ──────────────────────────────────────────────
print(lst.find(20))  # 1    → 20이 1번 자리에 있음
print(lst.find(99))  # -1   → 없음

# ── replace ───────────────────────────────────────────
print(lst.replace(0, 77))  # True  → 0번 자리를 77로 교체
lst.display()               # 리스트 (크기: 3): [77, 20, 30]
print(lst.replace(99, 77)) # False → 범위 벗어남

# ── sort ──────────────────────────────────────────────
lst.append(5)
lst.display()   # 리스트 (크기: 4): [77, 20, 30, 5]
print(lst.sort())  # True
lst.display()      # 리스트 (크기: 4): [5, 20, 30, 77]

# ── merge ─────────────────────────────────────────────
lst2 = ADT_list()
lst2.append(100)
lst2.append(200)
print(lst.merge(lst2))  # 2    → 2개 추가됨
lst.display()            # 리스트 (크기: 6): [5, 20, 30, 77, 100, 200]

# ── clear ─────────────────────────────────────────────
lst.clear()
lst.display()    # 리스트가 비어 있습니다.
print(lst.size())  # 0