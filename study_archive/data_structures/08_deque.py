# DEQUE ADT (Double-Ended Queue)
# 데이터: 앞(front)과 뒤(rear) 양쪽에서 삽입/삭제가 가능한 항목들의 모음
# 구조: 원형 덱 - 원형 큐를 확장해 양방향 삽입/삭제 지원
#
# front: 첫 번째 요소 바로 앞의 인덱스 (해당 자리는 항상 비어 있음)
# rear : 마지막 요소의 인덱스
# 공백 상태: front == rear
# 포화 상태: (rear + 1) % M == front


class ADT_deque:
    def __init__(self, capacity=10):
        self.maxsize = capacity               # 덱의 최대 크기 (실제 저장 가능: maxsize - 1)
        self.bag     = [None] * self.maxsize  # 덱 데이터를 저장할 배열
        self.front   = 0                      # 첫 번째 요소 바로 앞 인덱스
        self.rear    = 0                      # 마지막 요소의 인덱스
                                              # 초기: front == rear → 공백 상태

    def _next(self, index):
        return (index + 1) % self.maxsize             # 시계 방향 순환

    def _prev(self, index):
        return (index - 1 + self.maxsize) % self.maxsize  # 반시계 방향 순환


    # ── isFull() ──────────────────────────────────────
    # 반환값: 가득 찼으면 True, 아니면 False
    def isFull(self):
        return self._next(self.rear) == self.front


    # ── isEmpty() ─────────────────────────────────────
    # 반환값: 비어 있으면 True, 아니면 False
    def isEmpty(self):
        return self.front == self.rear


    # ── add_front(e) ──────────────────────────────────
    # 덱의 맨 앞에 요소 e를 삽입
    # 반환값: 성공이면 True, 실패(가득 참)면 False
    def add_front(self, e):
        if self.isFull():
            return False
        self.bag[self.front] = e
        self.front           = self._prev(self.front)
        return True


    # ── delete_front() ────────────────────────────────
    # 덱의 맨 앞 요소를 꺼내 반환
    # 반환값: 꺼낸 요소, 실패(비어 있음)면 None
    def delete_front(self):
        if self.isEmpty():
            return None
        self.front           = self._next(self.front)
        item                 = self.bag[self.front]
        self.bag[self.front] = None
        return item


    # ── get_front() ───────────────────────────────────
    # 덱의 맨 앞 요소를 꺼내지 않고 반환
    # 반환값: 맨 앞 요소, 실패(비어 있음)면 None
    def get_front(self):
        if self.isEmpty():
            return None
        return self.bag[self._next(self.front)]


    # ── add_rear(e) ───────────────────────────────────
    # 덱의 맨 뒤에 요소 e를 삽입
    # 반환값: 성공이면 True, 실패(가득 참)면 False
    def add_rear(self, e):
        if self.isFull():
            return False
        self.rear           = self._next(self.rear)
        self.bag[self.rear] = e
        return True


    # ── delete_rear() ─────────────────────────────────
    # 덱의 맨 뒤 요소를 꺼내 반환
    # 반환값: 꺼낸 요소, 실패(비어 있음)면 None
    def delete_rear(self):
        if self.isEmpty():
            return None
        item                = self.bag[self.rear]
        self.bag[self.rear] = None
        self.rear           = self._prev(self.rear)
        return item


    # ── clear() ───────────────────────────────────────
    # 덱을 공백 상태로 만든다
    # 반환값: 없음
    def clear(self):
        self.bag   = [None] * self.maxsize
        self.front = 0
        self.rear  = 0


    # ── get_rear() ────────────────────────────────────
    # 덱의 맨 뒤 요소를 꺼내지 않고 반환
    # 반환값: 맨 뒤 요소, 실패(비어 있음)면 None
    def get_rear(self):
        if self.isEmpty():
            return None
        return self.bag[self.rear]


    # ── size() ────────────────────────────────────────
    # 반환값: 현재 저장된 요소 수
    def size(self):
        return (self.rear - self.front + self.maxsize) % self.maxsize


    # ── display() ─────────────────────────────────────
    # 덱을 화면에 출력 (출력 전용 함수)
    def display(self):
        if self.isEmpty():
            print("덱: []  (공백)")
            return
        items = []
        i = self._next(self.front)
        while True:
            items.append(self.bag[i])
            if i == self.rear:
                break
            i = self._next(i)
        print(f"덱 (front → rear): {items}")

########################################################
###########              TEST              #############
########################################################
d = ADT_deque()

# ── isEmpty / isFull ──────────────────────────────────
print(d.isEmpty())       # True  → 비어 있음
print(d.isFull())        # False → 가득 차지 않음

# ── add_front / add_rear ──────────────────────────────
print(d.add_rear(10))    # True  → 뒤에 삽입
print(d.add_rear(20))    # True  → 뒤에 삽입
print(d.add_front(5))    # True  → 앞에 삽입
print(d.add_front(1))    # True  → 앞에 삽입
d.display()              # 덱 (front → rear): [1, 5, 10, 20]

# ── get_front / get_rear ──────────────────────────────
print(d.get_front())     # 1     → 맨 앞 확인 (제거 안 함)
print(d.get_rear())      # 20    → 맨 뒤 확인 (제거 안 함)

# ── delete_front / delete_rear ────────────────────────
print(d.delete_front())  # 1     → 앞에서 꺼냄
print(d.delete_rear())   # 20    → 뒤에서 꺼냄
d.display()              # 덱 (front → rear): [5, 10]

# ── size ──────────────────────────────────────────────
print(d.size())          # 2

# ── 가득 찬 경우 (maxsize=10 → 실제 저장 가능: 9개) ────
d2 = ADT_deque()
for i in range(9):
    d2.add_rear(i)
print(d2.isFull())       # True
print(d2.add_rear(99))   # False → 가득 참
print(d2.add_front(99))  # False → 가득 참

# ── 비어 있는 경우 ──────────────────────────────────────
d3 = ADT_deque()
print(d3.delete_front()) # None → 비어 있음
print(d3.delete_rear())  # None → 비어 있음
print(d3.get_front())    # None → 비어 있음
print(d3.get_rear())     # None → 비어 있음

# ── clear ─────────────────────────────────────────────
d.clear()
print(d.isEmpty())       # True  → front == rear
d.display()              # 덱: []  (공백)