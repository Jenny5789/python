class ADT_circular_queue:
    def __init__(self, capacity=10):
        self.maxsize = capacity               # 큐의 최대 크기 (실제 저장 가능: maxsize - 1)
        self.bag     = [None] * self.maxsize  # 큐 데이터를 저장할 배열
        self.front   = 0                      # 첫 번째 요소 바로 앞 인덱스
        self.rear    = 0                      # 마지막 요소의 인덱스
                                              # 초기: front == rear → 공백 상태

########################################################
###########       미로 탐색 _ 너비 우선 탐색       #############
########################################################

# 미로: '1' = 벽, '0' = 통로, 'e' = 시작, 'x' = 출구
# 너비 우선 탐색(BFS): 큐를 활용해 가까운 곳부터 탐색
# → DFS(스택)와 달리 항상 최단 경로를 보장

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


# ── bfs_maze(maze) ────────────────────────────────────
# 너비 우선 탐색(BFS)으로 미로의 출구를 찾음
# DFS(스택)와 달리 큐를 사용 → 가까운 곳부터 탐색 → 최단 경로 보장
# 매개변수: maze(미로 배열)
# 반환값: 최단 경로 리스트 [(행, 열), ...], 출구 없으면 None
def bfs_maze(maze):

    start_pos = find_pos(maze, 'e')  # 시작 위치 자동 탐색
    exit_pos  = find_pos(maze, 'x')  # 출구 위치 자동 탐색

    # 시작 또는 출구가 없는 경우 → 탐색 불가
    if start_pos is None or exit_pos is None:
        return None

    # ⚠️ DFS는 stack.pop() / BFS는 queue.dequeue() → 이 차이가 핵심
    queue   = ADT_circular_queue(100)  # 큐 사용 (스택 대신)
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]
    parent  = {}

    # 1. 시작 위치를 큐에 enqueue
    queue.enqueue(start_pos)
    parent[start_pos] = None

    # 2. 큐가 비어 있지 않은 동안 반복
    while not queue.isEmpty():
        current  = queue.dequeue()  # 맨 앞에서 꺼냄 (FIFO → 가까운 곳 먼저)
        row, col = current

        # 이미 방문한 위치면 건너뜀
        if visited[row][col]:
            continue

        # 현재 위치 방문 표시
        visited[row][col] = True

        # 3. 출구 도달 → 탐색 성공 (BFS이므로 처음 도달한 경로 = 최단 경로)
        if current == exit_pos:
            return reconstruct_path(parent, exit_pos)

        # 4. 4방향 탐색 (상, 하, 좌, 우)
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc

            if 0 <= nr < MAZE_SIZE and 0 <= nc < MAZE_SIZE:
                if maze[nr][nc] in PASSABLE and not visited[nr][nc]:
                    if (nr, nc) not in parent:
                        parent[(nr, nc)] = current
                    queue.enqueue((nr, nc))  # 스택이 아닌 큐에 추가

    # 5. 큐가 비었는데 출구를 못 찾음 → 출구 없음
    return None


########################################################
###########              TEST              #############
########################################################

# ── 탐색 전 미로 출력 ─────────────────────────────────
print("── 미로 (탐색 전) ───────────────────────────────")
display_maze(MAZE)

# ── BFS 탐색 실행 ─────────────────────────────────────
path = bfs_maze(MAZE)

# ── 결과 출력 ─────────────────────────────────────────
if path:
    print("── 탐색 성공 ✅ ─────────────────────────────────")
    print(f"경로 길이: {len(path)}칸  ← 최단 경로 보장")
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
result = bfs_maze(BLOCKED_MAZE)
print("결과:", "✅ 경로 있음" if result else "❌ 출구 없음")