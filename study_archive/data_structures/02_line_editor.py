class LineEditor:
    def __init__(self):
        self.lines = []  # 라인들을 저장하는 리스트


    # ── insert(linenum, text) ─────────────────────────
    # linenum 행에 text를 삽입
    # 매개변수: linenum(행 번호), text(삽입할 문자열)
    # 반환값: 성공이면 True, 실패면 False
    def insert(self, linenum, text):

        # 범위를 벗어난 경우 → 삽입 불가
        # len(self.lines) + 1 까지 허용 (맨 마지막 행 다음에 추가 가능)
        if linenum < 1 or linenum > len(self.lines) + 1:
            return False

        self.lines.insert(linenum - 1, text)  # 파이썬 인덱스는 0부터이므로 -1
        return True                            # 삽입 성공


    # ── delete(linenum) ───────────────────────────────
    # linenum 행을 삭제하고 반환
    # 매개변수: linenum(삭제할 행 번호)
    # 반환값: 삭제된 문자열, 실패면 None
    def delete(self, linenum):

        # 문서가 비어 있는 경우 → 삭제 불가
        if len(self.lines) == 0:
            return None

        # 범위를 벗어난 경우 → 삭제 불가
        if linenum < 1 or linenum > len(self.lines):
            return None

        return self.lines.pop(linenum - 1)  # 해당 행 삭제 후 반환


    # ── replace(linenum, text) ────────────────────────
    # linenum 행의 내용을 text로 변경
    # 매개변수: linenum(변경할 행 번호), text(새 문자열)
    # 반환값: 변경 전 문자열(old), 실패면 None
    def replace(self, linenum, text):

        # 문서가 비어 있는 경우 → 변경 불가
        if len(self.lines) == 0:
            return None

        # 범위를 벗어난 경우 → 변경 불가
        if linenum < 1 or linenum > len(self.lines):
            return None

        old = self.lines[linenum - 1]   # 변경 전 내용 저장 (출력용)
        self.lines[linenum - 1] = text  # 해당 행을 새 내용으로 교체
        return old                      # 변경 전 내용 반환


    # ── print_all() ───────────────────────────────────
    # 현재 문서의 모든 내용을 행 번호와 함께 출력
    # 반환값: 없음 (출력 전용 함수)
    def print_all(self):

        # 문서가 비어 있는 경우
        if len(self.lines) == 0:
            print("문서가 비어 있습니다.")
            return

        print("---------- 현재 문서 ----------")
        for i, line in enumerate(self.lines):  # enumerate: 인덱스와 값을 함께 반환
            print(f"{i + 1}: {line}")          # 행 번호는 1부터 시작
        print("--------------------------------")


    # ── load(filename) ────────────────────────────────
    # 지정된 파일에서 라인을 읽어 들임
    # 매개변수: filename(불러올 파일 이름, 기본값 "test.txt")
    # 반환값: 성공이면 True, 파일 없으면 False
    def load(self, filename="test.txt"):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                self.lines = f.read().splitlines()  # 줄바꿈 기준으로 나눠 리스트에 저장
            print(f"'{filename}'에서 {len(self.lines)}개의 라인을 불러왔습니다.")
            return True  # 불러오기 성공

        except FileNotFoundError:
            print(f"오류: '{filename}' 파일을 찾을 수 없습니다.")
            return False  # 파일 없음


    # ── save(filename) ────────────────────────────────
    # 현재 문서를 지정된 파일로 저장
    # 매개변수: filename(저장할 파일 이름, 기본값 "test.txt")
    # 반환값: 없음 (출력 전용 함수)
    def save(self, filename="test.txt"):
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(self.lines))  # 각 라인을 줄바꿈으로 연결해 저장
        print(f"'{filename}'에 {len(self.lines)}개의 라인이 저장되었습니다.")

        
###########           메인 실행부           #############

editor = LineEditor()

print("라인 편집기 시작 (명령어: i, d, r, p, l, s, q)")

while True:
    command = input("\n명령어 입력: ").strip().lower()

    # ── i: 삽입 ──────────────────────────────────────
    if command == "i":
        linenum = int(input("행 번호: "))
        text = input("내용: ")
        if editor.insert(linenum, text):
            print(f"{linenum}번 행에 라인이 삽입되었습니다.")
        else:
            print("오류: 올바르지 않은 행 번호입니다.")

    # ── d: 삭제 ──────────────────────────────────────
    elif command == "d":
        linenum = int(input("행 번호: "))
        removed = editor.delete(linenum)
        if removed is not None:
            print(f"{linenum}번 행 '{removed}'이(가) 삭제되었습니다.")
        else:
            print("오류: 삭제할 수 없습니다.")

    # ── r: 변경 ──────────────────────────────────────
    elif command == "r":
        linenum = int(input("행 번호: "))
        text = input("새 내용: ")
        old = editor.replace(linenum, text)
        if old is not None:
            print(f"{linenum}번 행이 '{old}' → '{text}'로 변경되었습니다.")
        else:
            print("오류: 변경할 수 없습니다.")

    # ── p: 출력 ──────────────────────────────────────
    elif command == "p":
        editor.print_all()

    # ── l: 파일 불러오기 ──────────────────────────────
    elif command == "l":
        editor.load()

    # ── s: 파일 저장 ──────────────────────────────────
    elif command == "s":
        editor.save()

    # ── q: 종료 ───────────────────────────────────────
    elif command == "q":
        print("편집기를 종료합니다.")
        break

    # ── 잘못된 명령어 ─────────────────────────────────
    else:
        print("오류: 올바르지 않은 명령어입니다. (i, d, r, p, l, s, q)")