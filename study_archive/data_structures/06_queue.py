# LINEAR QUEUE ADT
# 데이터: 선입선출(FIFO)의 접근 방법을 유지하는 항목들의 모음
# 구조: 선형 큐 - 앞에서 꺼내고 뒤에서 삽입 (단, 앞쪽 빈 공간은 재사용 불가)


class ADT_linear_queue:
    def __init__(self, capacity=10):
        self.maxsize = capacity               # 큐의 최대 크기
        self.bag     = [None] * self.maxsize  # 큐 데이터를 저장할 배열
        self.front   = 0                      # 맨 앞 요소의 인덱스
        self.rear    = -1                     # 맨 뒤 요소의 인덱스 (-1 = 비어 있음)
        self.length  = 0                      # 현재 저장된 요소 수


    # ── enqueue(e) ────────────────────────────────────
    # 요소 e를 큐의 맨 뒤에 추가
    # 매개변수: e(추가할 요소)
    # 반환값: 성공이면 True, 실패(가득 참)면 False
    def enqueue(self, e):

        # 가득 찬 경우 → 추가 불가
        # rear가 배열의 마지막 인덱스에 도달하면 앞쪽 빈 공간이 있어도 삽입 불가
        if self.isFull():
            return False

        self.rear           += 1   # rear를 한 칸 뒤로 이동
        self.bag[self.rear]  = e   # rear 위치에 e 저장
        self.length         += 1   # 요소 수 1 증가
        return True                # 추가 성공


    # ── dequeue() ─────────────────────────────────────
    # 큐의 맨 앞 요소를 꺼내 반환
    # 반환값: 꺼낸 요소, 실패(비어 있음)면 None
    def dequeue(self):

        # 비어 있는 경우 → 꺼낼 수 없음
        if self.isEmpty():
            return None

        item                  = self.bag[self.front]  # 꺼낼 요소 저장
        self.bag[self.front]  = None                  # 꺼낸 자리 비우기
        self.front           += 1                     # front를 한 칸 뒤로 이동
        self.length          -= 1                     # 요소 수 1 감소
        return item                                   # 꺼낸 요소 반환


    # ── isFull() ──────────────────────────────────────
    # 큐가 가득 찼는지 검사
    # 반환값: 가득 찼으면 True, 아니면 False
    def isFull(self):
        # rear가 마지막 인덱스에 도달하면 가득 찬 것
        # (앞쪽에 빈 공간이 있어도 재사용 불가 → 선형 큐의 한계)
        return self.rear == self.maxsize - 1


    # ── isEmpty() ─────────────────────────────────────
    # 큐가 비어 있는지 검사
    # 반환값: 비어 있으면 True, 아니면 False
    def isEmpty(self):
        return self.length == 0  # 저장된 요소 수가 0이면 비어 있음


    # ── peek() ────────────────────────────────────────
    # 큐의 맨 앞 요소를 꺼내지 않고 반환
    # 반환값: 맨 앞 요소, 실패(비어 있음)면 None
    def peek(self):

        # 비어 있는 경우 → 볼 수 없음
        if self.isEmpty():
            return None

        return self.bag[self.front]  # 맨 앞 요소 반환 (제거하지 않음)


    # ── size() ────────────────────────────────────────
    # 큐에 저장된 요소 수를 반환
    # 반환값: 현재 저장된 요소 수
    def size(self):
        return self.length


    # ── clear() ───────────────────────────────────────
    # 큐를 초기화
    # 반환값: 없음
    def clear(self):
        self.bag    = [None] * self.maxsize  # 모든 자리를 빈 상태로 초기화
        self.front  = 0                      # front를 초기 상태로 되돌림
        self.rear   = -1                     # rear를 초기 상태(-1)로 되돌림
        self.length = 0                      # 요소 수 0으로 초기화


    # ── display() ─────────────────────────────────────
    # 큐를 화면에 출력 (출력 전용 함수)
    # 반환값: 없음
    def display(self):

        # 비어 있는 경우
        if self.isEmpty():
            print("큐: []  (공백)")
            return

        # front부터 rear까지 순서대로 출력
        print(f"큐 (front → rear): {self.bag[self.front:self.rear + 1]}")

        ########################################################
###########              TEST              #############
########################################################
q = ADT_linear_queue()

# ── isEmpty / isFull ──────────────────────────────────
print(q.isEmpty())    # True  → 비어 있음
print(q.isFull())     # False → 가득 차지 않음

# ── enqueue ───────────────────────────────────────────
print(q.enqueue(10))  # True  → 삽입 성공
print(q.enqueue(20))  # True  → 삽입 성공
print(q.enqueue(30))  # True  → 삽입 성공
q.display()           # 큐 (front → rear): [10, 20, 30]

# ── peek ──────────────────────────────────────────────
print(q.peek())       # 10    → 맨 앞 요소 확인 (제거 안 함)

# ── dequeue ───────────────────────────────────────────
print(q.dequeue())    # 10    → 꺼내서 반환
print(q.dequeue())    # 20    → 꺼내서 반환
q.display()           # 큐 (front → rear): [30]

# ── size ──────────────────────────────────────────────
print(q.size())       # 1

# ── 가득 찬 경우 ────────────────────────────────────────
q2 = ADT_linear_queue()
for i in range(10):
    q2.enqueue(i)
print(q2.isFull())     # True
print(q2.enqueue(99))  # False → 가득 참

# ── 선형 큐 한계 테스트 ───────────────────────────────
# dequeue 후에도 앞쪽 빈 공간을 재사용할 수 없음
q3 = ADT_linear_queue(5)
for i in range(5):
    q3.enqueue(i)      # [0, 1, 2, 3, 4] → 가득 참
q3.dequeue()           # 0 제거 → 앞쪽 빈 공간 발생
q3.dequeue()           # 1 제거
print(q3.isFull())     # True → rear가 끝에 있어서 빈 공간 있어도 삽입 불가
print(q3.enqueue(99))  # False → 선형 큐의 한계

# ── 비어 있는 경우 ──────────────────────────────────────
q4 = ADT_linear_queue()
print(q4.dequeue())    # None  → 비어 있음
print(q4.peek())       # None  → 비어 있음

# ── clear ─────────────────────────────────────────────
q.clear()
print(q.isEmpty())     # True  → 초기화 확인
q.display()            # 큐: []  (공백)


# CIRCULAR QUEUE ADT
# 데이터: 선입선출(FIFO)의 접근 방법을 유지하는 항목들의 모음
# 구조: 원형 큐 - 배열의 끝과 시작을 연결해 빈 공간을 순환 재사용
#
# front: 첫 번째 요소 바로 앞의 인덱스 (해당 자리는 항상 비어 있음)
# rear : 마지막 요소의 인덱스
# 공백 상태: front == rear
# 포화 상태: front % M == (rear + 1) % M  →  front == (rear + 1) % M


class ADT_circular_queue:
    def __init__(self, capacity=10):
        self.maxsize = capacity               # 큐의 최대 크기 (실제 저장 가능: maxsize - 1)
        self.bag     = [None] * self.maxsize  # 큐 데이터를 저장할 배열
        self.front   = 0                      # 첫 번째 요소 바로 앞 인덱스
        self.rear    = 0                      # 마지막 요소의 인덱스
                                              # 초기: front == rear → 공백 상태


    # ── _next(index) ──────────────────────────────────
    # 원형 큐에서 다음 인덱스를 계산 (내부 헬퍼 함수)
    # 매개변수: index(현재 인덱스)
    # 반환값: 다음 인덱스 (배열 끝에서 0으로 순환)
    def _next(self, index):
        return (index + 1) % self.maxsize  # 나머지 연산으로 원형 순환


    # ── enqueue(e) ────────────────────────────────────
    # 요소 e를 큐의 맨 뒤에 추가
    # 매개변수: e(추가할 요소)
    # 반환값: 성공이면 True, 실패(가득 참)면 False
    def enqueue(self, e):

        # 가득 찬 경우 → 추가 불가
        # front == (rear + 1) % M 이면 포화 상태
        if self.isFull():
            return False

        self.rear           = self._next(self.rear)  # rear를 한 칸 앞으로 이동
        self.bag[self.rear] = e                      # 새 rear 위치에 e 저장
        return True                                  # 추가 성공


    # ── dequeue() ─────────────────────────────────────
    # 큐의 맨 앞 요소를 꺼내 반환
    # 반환값: 꺼낸 요소, 실패(비어 있음)면 None
    def dequeue(self):

        # 비어 있는 경우 → 꺼낼 수 없음
        # front == rear 이면 공백 상태
        if self.isEmpty():
            return None

        self.front           = self._next(self.front)  # front를 한 칸 앞으로 이동
        item                 = self.bag[self.front]    # 새 front 위치의 요소 저장
        self.bag[self.front] = None                    # 꺼낸 자리 비우기
        return item                                    # 꺼낸 요소 반환


    # ── isFull() ──────────────────────────────────────
    # 큐가 가득 찼는지 검사
    # 반환값: 가득 찼으면 True, 아니면 False
    def isFull(self):
        # (rear + 1) % M == front 이면 포화 상태
        # rear의 다음 위치가 front와 같으면 더 이상 삽입 불가
        return self._next(self.rear) == self.front


    # ── isEmpty() ─────────────────────────────────────
    # 큐가 비어 있는지 검사
    # 반환값: 비어 있으면 True, 아니면 False
    def isEmpty(self):
        return self.front == self.rear  # front와 rear가 같으면 공백 상태


    # ── peek() ────────────────────────────────────────
    # 큐의 맨 앞 요소를 꺼내지 않고 반환
    # 반환값: 맨 앞 요소, 실패(비어 있음)면 None
    def peek(self):

        # 비어 있는 경우 → 볼 수 없음
        if self.isEmpty():
            return None

        # front 다음 자리가 실제 첫 번째 요소
        return self.bag[self._next(self.front)]


    # ── size() ────────────────────────────────────────
    # 큐에 저장된 요소 수를 반환
    # 반환값: 현재 저장된 요소 수
    def size(self):
        # 원형 구조이므로 나머지 연산으로 계산
        # ex) maxsize=10, front=7, rear=2 → (2 - 7 + 10) % 10 = 5
        return (self.rear - self.front + self.maxsize) % self.maxsize


    # ── clear() ───────────────────────────────────────
    # 큐를 초기화
    # 반환값: 없음
    def clear(self):
        self.bag   = [None] * self.maxsize  # 모든 자리를 빈 상태로 초기화
        self.front = 0                      # front를 초기 상태로 되돌림
        self.rear  = 0                      # rear를 초기 상태로 되돌림
                                            # front == rear → 공백 상태


    # ── display() ─────────────────────────────────────
    # 큐를 화면에 출력 (출력 전용 함수)
    # 반환값: 없음
    def display(self):

        # 비어 있는 경우
        if self.isEmpty():
            print("큐: []  (공백)")
            return

        # front 다음부터 rear까지 순환하며 항목 수집
        items = []
        i = self._next(self.front)  # 실제 첫 번째 요소는 front 다음 자리
        while True:
            items.append(self.bag[i])
            if i == self.rear:      # rear까지 다 수집하면 종료
                break
            i = self._next(i)       # 다음 인덱스로 이동 (원형 순환)

        print(f"큐 (front → rear): {items}")

########################################################
###########              TEST              #############
########################################################
q = ADT_circular_queue()

# ── isEmpty / isFull ──────────────────────────────────
print(q.isEmpty())    # True  → front == rear
print(q.isFull())     # False → 가득 차지 않음

# ── enqueue ───────────────────────────────────────────
print(q.enqueue(10))  # True  → 삽입 성공
print(q.enqueue(20))  # True  → 삽입 성공
print(q.enqueue(30))  # True  → 삽입 성공
q.display()           # 큐 (front → rear): [10, 20, 30]

# ── peek ──────────────────────────────────────────────
print(q.peek())       # 10    → 맨 앞 요소 확인 (제거 안 함)

# ── dequeue ───────────────────────────────────────────
print(q.dequeue())    # 10    → 꺼내서 반환
print(q.dequeue())    # 20    → 꺼내서 반환
q.display()           # 큐 (front → rear): [30]

# ── size ──────────────────────────────────────────────
print(q.size())       # 1

# ── 가득 찬 경우 (maxsize=10 → 실제 저장 가능: 9개) ────
q2 = ADT_circular_queue()
for i in range(9):     # 10 - 1 = 9개까지만 저장 가능
    q2.enqueue(i)
print(q2.isFull())     # True
print(q2.enqueue(99))  # False → 가득 참

# ── 순환 테스트 (원형 큐 핵심) ───────────────────────────
q3 = ADT_circular_queue(5)  # 실제 저장 가능: 4개
for i in range(4):
    q3.enqueue(i)        # [0, 1, 2, 3] → 가득 참
q3.dequeue()             # 0 제거 → 앞쪽 빈 공간 발생
q3.dequeue()             # 1 제거
q3.enqueue(10)           # 빈 자리(앞쪽)에 순환 삽입 ← 선형 큐와 차이
q3.enqueue(20)
q3.display()             # 큐 (front → rear): [2, 3, 10, 20]
print(q3.size())         # 4

# ── 비어 있는 경우 ──────────────────────────────────────
q4 = ADT_circular_queue()
print(q4.dequeue())    # None  → 비어 있음
print(q4.peek())       # None  → 비어 있음

# ── clear ─────────────────────────────────────────────
q.clear()
print(q.isEmpty())     # True  → front == rear
q.display()            # 큐: []  (공백)