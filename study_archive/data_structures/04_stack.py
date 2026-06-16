# STACK ADT
# 데이터: 후입선출(LIFO)의 접근 방법을 유지하는 항목들의 모음


class ADT_stack:
    def __init__(self):
        self.maxsize = 10
        self.bag     = [None] * self.maxsize
        self.top     = -1  # 맨 위 요소의 인덱스 (-1 = 비어 있음)


    # ── push(e) ───────────────────────────────────────
    # 스택의 맨 위에 항목 e를 추가
    # 매개변수: e(추가할 항목)
    # 반환값: 성공이면 True, 실패(가득 참)면 False
    def push(self, e):

        # 가득 찬 경우 → 추가 불가
        # top이 마지막 인덱스(maxsize - 1)면 가득 찬 것
        if self.top == self.maxsize - 1:
            return False

        self.top += 1           # top을 한 칸 위로 이동
        self.bag[self.top] = e  # 새 top 위치에 e 저장
        return True             # 추가 성공


    # ── pop() ─────────────────────────────────────────
    # 스택의 맨 위 항목을 꺼내서 반환
    # 반환값: 꺼낸 항목, 실패(비어 있음)면 None
    def pop(self):

        # 비어 있는 경우 → 꺼낼 수 없음
        # top이 -1이면 비어 있는 것
        if self.top == -1:
            return None

        popped           = self.bag[self.top]  # 꺼낼 항목 저장
        self.bag[self.top] = None              # 꺼낸 자리 비우기
        self.top        -= 1                   # top을 한 칸 아래로 이동
        return popped                          # 꺼낸 항목 반환


    # ── isFull() ──────────────────────────────────────
    # 스택이 가득 찼는지 검사
    # 반환값: 가득 찼으면 True, 아니면 False
    def isFull(self):
        return self.top == self.maxsize - 1  # top이 마지막 인덱스면 가득 참


    # ── isEmpty() ─────────────────────────────────────
    # 스택이 비어 있는지 검사
    # 반환값: 비어 있으면 True, 아니면 False
    def isEmpty(self):
        return self.top == -1  # top이 -1이면 비어 있음


    # ── peek() ────────────────────────────────────────
    # 스택의 맨 위 항목을 꺼내지 않고 반환
    # 반환값: 맨 위 항목, 실패(비어 있음)면 None
    def peek(self):

        # 비어 있는 경우 → 볼 수 없음
        if self.top == -1:
            return None

        return self.bag[self.top]  # 맨 위 항목 반환 (제거하지 않음)


    # ── size() ────────────────────────────────────────
    # 스택에 저장된 항목 수를 반환
    # 반환값: 현재 저장된 항목 수
    def size(self):
        return self.top + 1  # top은 0부터 시작하므로 +1이 실제 개수


    # ── clear() ───────────────────────────────────────
    # 스택을 초기화
    # 반환값: 없음
    def clear(self):
        self.bag = [None] * self.maxsize  # 모든 자리를 빈 상태로 초기화
        self.top = -1                     # top을 초기 상태(-1)로 되돌림


    # ── display() ─────────────────────────────────────
    # 스택을 화면에 출력 (출력 전용 함수)
    # 반환값: 없음
    def display(self):

        # 비어 있는 경우
        if self.top == -1:
            print("스택: []  (공백)")

        else:
            # [:self.top + 1]  → 저장된 항목만 추출
            # [::-1]           → 뒤집어서 top이 앞에 오도록 출력
            print(f"스택 (top → bottom): {self.bag[:self.top + 1][::-1]}")


########################################################
###########              TEST              #############
########################################################

# ── 기본 push / pop ───────────────────────────────────
s = ADT_stack()
print(s.push(10))   # True  → 삽입 성공
print(s.push(20))   # True  → 삽입 성공
print(s.push(30))   # True  → 삽입 성공
s.display()         # 스택 (top → bottom): [30, 20, 10]

# ── peek ──────────────────────────────────────────────
print(s.peek())     # 30    → 맨 위 항목 확인 (제거 안 함)
s.display()         # 스택 (top → bottom): [30, 20, 10]  ← 변화 없음

# ── pop ───────────────────────────────────────────────
print(s.pop())      # 30    → 꺼내서 반환
print(s.pop())      # 20    → 꺼내서 반환
s.display()         # 스택 (top → bottom): [10]

# ── size ──────────────────────────────────────────────
print(s.size())     # 1

# ── isEmpty / isFull ──────────────────────────────────
print(s.isEmpty())  # False → 비어 있지 않음
print(s.isFull())   # False → 가득 차지 않음

# ── 가득 찬 경우 ────────────────────────────────────────
s2 = ADT_stack()
for i in range(10):
    s2.push(i)
print(s2.push(99))  # False → 가득 참
print(s2.isFull())  # True

# ── 비어 있는 경우 ──────────────────────────────────────
s3 = ADT_stack()
print(s3.pop())     # None  → 비어 있음
print(s3.peek())    # None  → 비어 있음
print(s3.isEmpty()) # True

# ── clear ─────────────────────────────────────────────
s.clear()
print(s.isEmpty())  # True  → 초기화 확인
s.display()         # 스택: []  (공백)

