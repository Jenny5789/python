class ADT_stack:
    def __init__(self):
        self.maxsize = 10
        self.bag     = [None] * self.maxsize
        self.top     = -1  # 맨 위 요소의 인덱스 (-1 = 비어 있음)

########################################################
###########           미로 탐색            #############
########################################################

# 미로: '1' = 벽, '0' = 통로, 'e' = 시작, 'x' = 출구
# 깊이 우선 탐색(DFS): 스택에 지나온 경로를 저장하며 출구를 찾아감

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
PASSABLE   = {'0', 'e', 'x'}  # 지나갈 수 있는 셀

# 이동 방향: 상, 하, 좌, 우 (행 변화량, 열 변화량)
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
    path_set = set(path) if path else set()  # 경로를 집합으로 변환 (빠른 탐색용)

    print("    0  1  2  3  4  5")
    for r in range(MAZE_SIZE):
        row_str = f"{r}  "
        for c in range(MAZE_SIZE):
            cell = maze[r][c]
            if cell == 'e':
                row_str += " e "   # 시작
            elif cell == 'x':
                row_str += " x "   # 출구
            elif (r, c) in path_set and cell == '0':
                row_str += " · "   # 탐색 경로
            elif cell == '1':
                row_str += " █ "   # 벽
            else:
                row_str += "   "   # 빈 통로
        print(row_str)
    print()


# ── reconstruct_path(parent, exit_pos) ───────────────
# 부모 딕셔너리를 역추적해서 시작 → 출구 경로를 재구성
# 매개변수: parent(각 위치의 이전 위치 딕셔너리), exit_pos(출구 위치)
# 반환값: 경로 리스트 [(행, 열), ...]
def reconstruct_path(parent, exit_pos):
    path = []
    pos  = exit_pos  # 출구에서부터 역추적 시작

    while pos is not None:
        path.append(pos)
        pos = parent[pos]  # 이전 위치로 이동

    return list(reversed(path))  # 뒤집어서 시작 → 출구 순서로 반환


# ── solve_maze(maze) ──────────────────────────────────
# 깊이 우선 탐색(DFS)으로 미로의 출구를 찾음
# 매개변수: maze(미로 배열)
# 반환값: 경로 리스트 [(행, 열), ...], 출구 없으면 None
def solve_maze(maze):

    start_pos = find_pos(maze, 'e')  # 시작 위치 자동 탐색
    exit_pos  = find_pos(maze, 'x')  # 출구 위치 자동 탐색

    # 시작 또는 출구가 없는 경우 → 탐색 불가
    if start_pos is None or exit_pos is None:
        return None

    stack   = ADT_stack(100)  # 미로 크기에 맞게 용량 설정
    visited = [[False] * MAZE_SIZE for _ in range(MAZE_SIZE)]  # 방문 여부 배열
    parent  = {}  # parent[(r,c)] = 이전 위치 → 경로 재구성에 사용

    # 1. 시작 위치를 스택에 push
    stack.push(start_pos)
    parent[start_pos] = None  # 시작점은 이전 위치가 없음

    # 2. 스택이 비어 있지 않은 동안 반복
    while not stack.isEmpty():
        current  = stack.pop()  # 현재 위치를 스택에서 꺼냄
        row, col = current

        # 이미 방문한 위치면 건너뜀
        if visited[row][col]:
            continue

        # 현재 위치 방문 표시
        visited[row][col] = True

        # 3. 출구 도달 → 탐색 성공
        if current == exit_pos:
            return reconstruct_path(parent, exit_pos)

        # 4. 4방향 탐색 (상, 하, 좌, 우)
        for dr, dc in DIRECTIONS:
            nr, nc = row + dr, col + dc  # 다음 위치 계산

            # 미로 범위 안인지 확인
            if 0 <= nr < MAZE_SIZE and 0 <= nc < MAZE_SIZE:

                # 지나갈 수 있고 아직 방문 전인 경우 → 스택에 push
                if maze[nr][nc] in PASSABLE and not visited[nr][nc]:
                    if (nr, nc) not in parent:  # 처음 발견한 경우에만 부모 기록
                        parent[(nr, nc)] = current
                    stack.push((nr, nc))

    # 5. 스택이 비었는데 출구를 못 찾음 → 출구 없음
    return None

########################################################
###########              TEST              #############
########################################################

# ── 탐색 전 미로 출력 ─────────────────────────────────
print("── 미로 (탐색 전) ───────────────────────────────")
display_maze(MAZE)

# ── DFS 탐색 실행 ─────────────────────────────────────
path = solve_maze(MAZE)

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
    ['e', '0', '0', '1', '1', '1'],  # 출구 방향 막힘
    ['1', '0', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', 'x'],  # 출구가 고립됨
    ['1', '1', '1', '1', '1', '1'],
    ['1', '1', '1', '1', '1', '1'],
]
result = solve_maze(BLOCKED_MAZE)
print("결과:", "✅ 경로 있음" if result else "❌ 출구 없음")