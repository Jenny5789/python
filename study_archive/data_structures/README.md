# Study Archive/data_structures

파이썬으로 구현한 자료구조 코드 모음.

## Repository Structure

| 파일 | 내용 | 주요 메서드 |
|---|---|---|
| [00_bag.py](00_bag.py) | 백(Bag) ADT | `insert`, `remove`, `__contains__`, `count` |
| [01_list.py](01_list.py) | 리스트 ADT | `isEmpty`, `isFull`, `insert`, `delete`, `getEntry`, `size`, `clear`, `find`, `replace`, `sort`, `merge`, `display`, `append` |
| [02_line_editor.py](02_line_editor.py) | 줄 편집기 | `insert`, `delete`, `replace`, `print_all`, `load`, `save` |
| [03_set.py](03_set.py) | 집합(Set) ADT | `contain`, `insert`, `delete`, `isFull`, `isEmpty`, `union`, `intersect`, `difference`, `equals`, `size`, `display` |
| [04_stack.py](04_stack.py) | 스택 ADT (후입선출) | `push`, `pop`, `isFull`, `isEmpty`, `peek`, `size`, `clear`, `display` |
| [05_DFS.py](05_DFS.py) | 스택을 이용한 미로 탐색 (깊이 우선 탐색) | |
| [06_queue.py](06_queue.py) | 선형 큐 ADT, 원형 큐 ADT (선입선출) | `enqueue`, `dequeue`, `isFull`, `isEmpty`, `peek`, `size`, `clear`, `display` |
| [07_BFS.py](07_BFS.py) | 원형 큐를 이용한 미로 탐색 (너비 우선 탐색) | |
| [08_deque.py](08_deque.py) | 덱(Deque) ADT (원형 덱) | `add_front`, `delete_front`, `get_front`, `add_rear`, `delete_rear`, `get_rear`, `isFull`, `isEmpty`, `clear`, `size`, `display` |
| [09_priorityqueue.py](09_priorityqueue.py) | 우선순위 큐 ADT (정렬된 배열, 숫자가 작을수록 높은 우선순위) | `enqueue`, `dequeue`, `peek`, `isFull`, `isEmpty`, `size`, `display` |
| [10_maze.py](10_maze.py) | 우선순위 큐를 이용한 미로 탐색 (맨해튼 거리가 작은 위치부터 탐색) | |
| [data_structure_list.py](data_structure_list.py) | 배열 구조 리스트, 연결된 구조 리스트 (`Node`, `LinkedList`) | |
| [tree.ipynb](tree.ipynb) | 이진 트리: 전위·중위·후위·레벨 순회, 노드 개수, 단말 노드 개수, 높이, 모르스 코드 결정 트리 | |