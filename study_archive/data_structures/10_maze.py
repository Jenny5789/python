########################################################
###########      우선순위 큐 미로 탐색 응용     #############
########################################################

# 미로: '1' = 벽, '0' = 통로, 'e' = 시작, 'x' = 출구
# 우선순위 탐색: 맨해튼 거리가 작은 위치부터 탐색 → 출구 방향으로 유도
# → BFS(균등 탐색)보다 효율적으로 탐색 가능
#
# ── 맨해튼 거리란? ────────────────────────────────────
# 격자에서 두 점 사이를 가로 + 세로 이동 횟수로 계산하는 방법
# 대각선 이동 없이 상하좌우로만 이동할 때 사용
#
# 예시:
#   현재 위치: (1, 0)
#   출구 위치: (3, 5)
#   맨해튼 거리 = |3-1| + |5-0| = 2 + 5 = 7
#
# 거리가 작을수록 출구에 가깝다는 의미
# → 우선순위 큐에서 거리가 작은 위치를 먼저 꺼내 탐색
# → DFS/BFS와 달리 출구 방향으로 유도하며 탐색 가능
# ─────────────────────────────────────────────────────


class Node:
    def __init__(self, priority, data):
        self.priority = priority
        self.data     = data

    def __str__(self):
        return f"[{self.priority}순위: {self.data}]"


class ADT_priority_queue:
    def __init__(self, capacity=100):
        self.maxsize = capacity
        self.bag     = [None] * self.maxsize
        self.length  = 0

    def _find_pos(self, priority):
        for i in range(self.length):
            if self.bag[i].priority > priority:
                return i
        return self.length

    def isFull(self):
        return self.length == self.maxsize

    def isEmpty(self):
        return self.length == 0

    def enqueue(self, priority, data):
        if self.isFull():
            return False
        new_node = Node(priority, data)
        pos      = self._find_pos(priority)
        for i in range(self.length, pos, -1):
            self.bag[i] = self.bag[i - 1]
        self.bag[pos]  = new_node
        self.length   += 1
        return True

    def dequeue(self):
        if self.isEmpty():
            return None
        item = self.bag[0]
        for i in range(self.length - 1):
            self.bag[i] = self.bag[i + 1]
        self.bag[self.length - 1]  = None
        self.length               -= 1
        return item

    def peek(self):
        if self.isEmpty():
            return None
        return self.bag[0]

    def size(self):
        return self.length

    def display(self):
        if self.isEmpty():
            print("우선순위 큐: []  (공백)")
            return
        items = [str(self.bag[i]) for i in range(self.length)]
        print(f"우선순위 큐: {' → '.join(items)}")


# ── 미로 정의 ─────────────────────────────────────────
MAZE = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1'],
]

MAZE_SIZE  = 6
PASSABLE   = {'0', 'e', 'x'}    # 지나갈 수 있는 셀

# 이동 방향: 상, 하, 좌, 우
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# ── find_pos(maze, target) ────────────────────────────
# 미로에서 특정 문자의 위치를 찾아 반환
# 매개변수: maze(미로 배열), target(찾을 문자 'e' 또는 'x')
# 반환값: (행, 열) 튜플, 없으면 None
def find_pos(maze, target):
    for r in range(MAZE_SIZE):
        for c in range(MAZE_SIZE):
            if maze[r][c] == target:
                return (r, c)
    return None


# ── manhattan(r, c, exit_pos) ─────────────────────────
# 현재 위치에서 출구까지의 맨해튼 거리 계산 (우선순위로 사용)
# 거리가 작을수록 출구에 가까움 → 높은 우선순위
# 반환값: 맨해튼 거리 (정수)
def manhattan(r, c, exit_pos):
    er, ec = exit_pos
    return abs(er - r) + abs(ec - c)  # 행 차이 + 열 차이


# ── display_maze(maze, path) ──────────────────────────
# 미로와 탐색 경로를 시각적으로 출력
# 매개변수: maze(미로 배열), path(경로 리스트, 기본값 None)
# 반환값: 없음 (출력 전용)
def display_maze(maze, path=None):
    path_set = set(path) if path else set()

    print("    0  1  2  3  4  5")
    for r in range(MAZE_SIZE):
        row_str = f"{r}  "
        for c in range(MAZE_SIZE):
            cell = maze[r][c]
            if cell == 'e':
                row_str += " e "
            elif cell == 'x':
                row_str += " x "
            elif (r, c) in path_set and cell == '0':
                row_str += " · "
            elif cell == '1':
                row_str += " █ "
            else:
                row_str += "   "
        print(row_str)
    print()


# ── reconstruct_path(parent, exit_pos) ───────────────
# 부모 딕셔너리를 역추적해서 시작 → 출구 경로를 재구성
# 매개변수: parent(각 위치의 이전 위치 딕셔너리), exit_pos(출구 위치)
# 반환값: 경로 리스트 [(행, 열), ...]
def reconstruct_path(parent, exit_pos):
    path = []
    pos  = exit_pos

    while pos is not None:
        path.append(pos)
        pos = parent[pos]

    return list(reversed(path))


# ── priority_maze(maze) ───────────────────────────────
# 우선순위 큐를 활용해 미로의 출구를 찾음
# 맨해튼 거리가 작은 위치부터 탐색 → 출구 방향으로 유도
# 매개변수: maze(미로 배열)
# 반환값: 경로 리스트 [(행, 열), ...], 출구 없으면 None
def priority_maze(maze):

    start_pos = find_pos(maze, 'e')  # 시작 위치 자동 탐색
    exit_pos  = find_pos(maze, 'x')  # 출구 위치 자동 탐색

    # 시작 또는 출구가 없는 경우 → 탐색 불가
    if start_pos is None or exit_pos is None:
        return None

    # ⚠️ BFS는 queue.dequeue() / 우선순위 탐색은 pq.dequeue() → 높은 우선순위 먼저
    pq      = ADT_priority_queue(100)
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]
    parent  = {}

    # 1. 시작 위치를 우선순위 큐에 삽입 (맨해튼 거리를 우선순위로 사용)
    sr, sc = start_pos
    pq.enqueue(manhattan(sr, sc, exit_pos), start_pos)
    parent[start_pos] = None

    # 2. 우선순위 큐가 비어 있지 않은 동안 반복
    while not pq.isEmpty():
        node     = pq.dequeue()  # 출구에 가장 가까운 위치 꺼냄
        current  = node.data
        row, col = current

        # 이미 방문한 위치면 건너뜀
        if visited[row][col]:
            continue

        # 현재 위치 방문 표시
        visited[row][col] = True

        # 3. 출구 도달 → 탐색 성공
        if current == exit_pos:
            return reconstruct_path(parent, exit_pos)

        # 4. 4방향 탐색 → 맨해튼 거리를 우선순위로 삽입
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc

            if 0 <= nr < MAZE_SIZE and 0 <= nc < MAZE_SIZE:
                if maze[nr][nc] in PASSABLE and not visited[nr][nc]:
                    if (nr, nc) not in parent:
                        parent[(nr, nc)] = current
                    pq.enqueue(manhattan(nr, nc, exit_pos), (nr, nc))

    # 5. 우선순위 큐가 비었는데 출구를 못 찾음 → 출구 없음
    return None

########################################################
###########              TEST              #############
########################################################

# ── 탐색 전 미로 출력 ─────────────────────────────────
print("── 미로 (탐색 전) ───────────────────────────────")
display_maze(MAZE)

# ── 우선순위 탐색 실행 ────────────────────────────────
path = priority_maze(MAZE)

# ── 결과 출력 ─────────────────────────────────────────
if path:
    print("── 탐색 성공 ✅ ─────────────────────────────────")
    print(f"경로 길이: {len(path)}칸")
    print(f"경로: {' → '.join(str(p) for p in path)}")
    print()
    print("── 미로 (탐색 후) ───────────────────────────────")
    display_maze(MAZE, path)
else:
    print("── 탐색 실패 ❌: 출구 없음 ─────────────────────")

# ── 출구 없는 미로 테스트 ─────────────────────────────
print("── 출구 없는 미로 테스트 ────────────────────────")
BLOCKED_MAZE = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', 'x'],
    ['1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1'],
]
result = priority_maze(BLOCKED_MAZE)
print("결과:", "✅ 경로 있음" if result else "❌ 출구 없음")