# PRIORITY QUEUE ADT
# 데이터: 우선순위가 높은 항목이 먼저 나오는 항목들의 모음
# 구조: 정렬된 배열 - 삽입 시 우선순위 순서대로 정렬 유지
#       숫자가 작을수록 높은 우선순위 (1순위 > 2순위 > 3순위 ...)


# ── Node 클래스 ───────────────────────────────────────
# 우선순위 큐의 각 항목을 표현하는 노드
# 매개변수: priority(우선순위), data(저장할 데이터)
class Node:
    def __init__(self, priority, data):
        self.priority = priority  # 우선순위 (숫자가 작을수록 높은 우선순위)
        self.data     = data      # 저장할 데이터

    def __str__(self):
        return f"[{self.priority}순위: {self.data}]"


class ADT_priority_queue:
    def __init__(self, capacity=100):
        self.maxsize = capacity               # 우선순위 큐의 최대 크기
        self.bag     = [None] * self.maxsize  # 데이터를 저장할 배열 (정렬 유지)
        self.length  = 0                      # 현재 저장된 항목 수


    # ── _find_pos(priority) ───────────────────────────
    # 새 항목의 삽입 위치를 탐색 (내부 헬퍼 함수)
    # 우선순위 순서가 유지되도록 삽입할 인덱스를 반환
    # 매개변수: priority(삽입할 항목의 우선순위)
    # 반환값: 삽입할 인덱스
    def _find_pos(self, priority):

        # 앞에서부터 순서대로 탐색
        for i in range(self.length):

            # 현재 항목의 우선순위보다 낮은 항목 발견 → 그 앞에 삽입
            # ex) 기존: [1, 2, 4], 새 항목: 3 → 4 앞(인덱스 2)에 삽입
            if self.bag[i].priority > priority:
                return i

        return self.length  # 가장 낮은 우선순위 → 맨 뒤에 삽입


    # ── isFull() ──────────────────────────────────────
    # 우선순위 큐가 가득 찼는지 검사
    # 반환값: 가득 찼으면 True, 아니면 False
    def isFull(self):
        return self.length == self.maxsize


    # ── isEmpty() ─────────────────────────────────────
    # 우선순위 큐가 비어 있는지 검사
    # 반환값: 비어 있으면 True, 아니면 False
    def isEmpty(self):
        return self.length == 0


    # ── enqueue(priority, data) ───────────────────────
    # 우선순위 큐에 항목을 삽입 (우선순위 순서 유지)
    # 매개변수: priority(우선순위), data(저장할 데이터)
    # 반환값: 성공이면 True, 실패(가득 참)면 False
    def enqueue(self, priority, data):

        # 가득 찬 경우 → 삽입 불가
        if self.isFull():
            return False

        new_node = Node(priority, data)      # 새 노드 생성
        pos      = self._find_pos(priority)  # 삽입 위치 탐색

        # 삽입 위치 뒤의 항목들을 한 칸씩 뒤로 이동 (자리 만들기)
        for i in range(self.length, pos, -1):
            self.bag[i] = self.bag[i - 1]

        self.bag[pos]  = new_node  # 해당 위치에 새 노드 삽입
        self.length   += 1         # 항목 수 1 증가
        return True                # 삽입 성공


    # ── dequeue() ─────────────────────────────────────
    # 가장 높은 우선순위 항목을 꺼내 반환 (맨 앞 = 가장 높은 우선순위)
    # 반환값: 꺼낸 Node, 실패(비어 있음)면 None
    def dequeue(self):

        # 비어 있는 경우 → 꺼낼 수 없음
        if self.isEmpty():
            return None

        item = self.bag[0]  # 맨 앞 항목 저장 (가장 높은 우선순위)

        # 나머지 항목들을 한 칸씩 앞으로 이동
        for i in range(self.length - 1):
            self.bag[i] = self.bag[i + 1]

        self.bag[self.length - 1]  = None  # 마지막 자리 비우기
        self.length               -= 1     # 항목 수 1 감소
        return item                        # 꺼낸 항목 반환


    # ── peek() ────────────────────────────────────────
    # 가장 높은 우선순위 항목을 꺼내지 않고 반환
    # 반환값: 맨 앞 Node, 실패(비어 있음)면 None
    def peek(self):

        # 비어 있는 경우 → 볼 수 없음
        if self.isEmpty():
            return None

        return self.bag[0]  # 맨 앞 항목 반환 (제거하지 않음)


    # ── size() ────────────────────────────────────────
    # 우선순위 큐에 저장된 항목 수를 반환
    # 반환값: 현재 저장된 항목 수
    def size(self):
        return self.length


    # ── display() ─────────────────────────────────────
    # 우선순위 큐를 화면에 출력 (출력 전용 함수)
    # 반환값: 없음
    def display(self):

        # 비어 있는 경우
        if self.isEmpty():
            print("우선순위 큐: []  (공백)")
            return

        # 우선순위 순서대로 출력 (앞 = 높은 우선순위)
        items = [str(self.bag[i]) for i in range(self.length)]
        print(f"우선순위 큐: {' → '.join(items)}")
        
########################################################
###########              TEST              #############
########################################################
pq = ADT_priority_queue()

# ── isEmpty / isFull ──────────────────────────────────
print(pq.isEmpty())              # True  → 비어 있음
print(pq.isFull())               # False → 가득 차지 않음

# ── enqueue ───────────────────────────────────────────
print(pq.enqueue(3, "환자C"))    # True  → 3순위 삽입
print(pq.enqueue(1, "환자A"))    # True  → 1순위 삽입 → 맨 앞으로
print(pq.enqueue(2, "환자B"))    # True  → 2순위 삽입 → 중간으로
print(pq.enqueue(1, "환자D"))    # True  → 1순위 중복 삽입
pq.display()
# 우선순위 큐: [1순위: 환자A] → [1순위: 환자D] → [2순위: 환자B] → [3순위: 환자C]

# ── peek ──────────────────────────────────────────────
print(pq.peek())                 # [1순위: 환자A] → 확인만 (제거 안 함)

# ── dequeue ───────────────────────────────────────────
print(pq.dequeue())              # [1순위: 환자A] → 가장 높은 우선순위 꺼냄
print(pq.dequeue())              # [1순위: 환자D]
pq.display()
# 우선순위 큐: [2순위: 환자B] → [3순위: 환자C]

# ── size ──────────────────────────────────────────────
print(pq.size())                 # 2

# ── 비어 있는 경우 ──────────────────────────────────────
pq2 = ADT_priority_queue()
print(pq2.dequeue())             # None → 비어 있음
print(pq2.peek())                # None → 비어 있음
