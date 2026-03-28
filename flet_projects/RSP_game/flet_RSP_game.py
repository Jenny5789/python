import flet as ft
import random

def main(page: ft.Page):
    page.title = "✊✌️✋ Game"
    page.bgcolor = "#F8E8EE"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window.width = 420
    page.window.height = 600

    # ================= 상태 =================
    user_score = 0
    computer_score = 0
    round_count = 0

    choices = ["가위", "바위", "보"]
    emoji = {"가위": "✌️", "바위": "✊", "보": "✋"}

    # ================= 텍스트 =================
    title = ft.Text("🌸 봄날의 가위바위보 🌸",
                    size=32, weight="bold", color="#E75480")

    round_text = ft.Text("🌼 1 / 5 라운드", size=16, color="#6D8299")
    score_text = ft.Text("컴퓨터 0 : 사용자 0",
                         size=20, weight="bold", color="#4A6C6F")

    result_text = ft.Text("🦋 버튼을 눌러 게임을 시작하세요 🦋",
                          size=18, color="#7A5C61",
                          text_align="center")

    # ================= 게임 =================
    def play(user_choice):
        nonlocal user_score, computer_score, round_count

        if round_count >= 5:
            return

        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "무승부!"
        elif (
            (user_choice == "가위" and computer_choice == "보") or
            (user_choice == "바위" and computer_choice == "가위") or
            (user_choice == "보" and computer_choice == "바위")
        ):
            result = "사용자 승!"
            user_score += 1
        else:
            result = "컴퓨터 승!"
            computer_score += 1

        round_count += 1

        result_text.value = (
            f"컴퓨터: {emoji[computer_choice]} {computer_choice}\n"
            f"사용자: {emoji[user_choice]} {user_choice}\n\n👉 {result}"
        )

        score_text.value = f"컴퓨터 {computer_score} : 사용자 {user_score}"
        round_text.value = f"🌼 {round_count} / 5 라운드"

        if user_score == 3 or computer_score == 3 or round_count == 5:
            if user_score > computer_score:
                result_text.value += "\n\n🌸 축하합니다! 승리!"
            elif computer_score > user_score:
                result_text.value += "\n\n🌿 컴퓨터 승리!"
            else:
                result_text.value += "\n\n🌼 무승부!"

        page.update()

    def reset_game(e):
        nonlocal user_score, computer_score, round_count
        user_score = 0
        computer_score = 0
        round_count = 0

        score_text.value = "컴퓨터 0 : 사용자 0"
        round_text.value = "🌼 1 / 5 라운드"
        result_text.value = "🌸 다시 시작합니다!"
        page.update()

    def on_click(e):
        play(e.control.data)

    # ================= 버튼 =================
    def make_button(choice):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(f"{emoji[choice]}\n{choice}",
                                size=18, weight="bold",
                                text_align="center"),
                data=choice,
                on_click=on_click,
                style=ft.ButtonStyle(
                    bgcolor="#F4A7B9",
                    color="white",
                    shape=ft.RoundedRectangleBorder(radius=15),
                    padding=20
                ),
            ),
            expand=True
        )

    # ================= 🌸 정적 배경 =================
    background = ft.Stack(
        [
            *[
                ft.Container(
                    content=ft.Text("🌸", size=15, opacity=0.35),
                    left=random.randint(0, 400),
                    top=random.randint(0, 700),
                )
                for _ in range(20)
            ],
            *[
                ft.Container(
                    content=ft.Text("🦋", size=18, opacity=0.5),
                    left=random.randint(0, 400),
                    top=random.randint(0, 700),
                )
                for _ in range(2)
            ],
        ],
        expand=True
    )

    # ================= 카드 =================
    game_card = ft.Container(
        content=ft.Column(
            [
                round_text,
                score_text,
                ft.Divider(height=10, color="transparent"),
                ft.Row(
                    [
                        make_button("가위"),
                        make_button("바위"),
                        make_button("보"),
                    ],
                    alignment="spaceEvenly"
                ),
                ft.Divider(height=10, color="transparent"),
                result_text,
                ft.Divider(height=10, color="transparent"),
                ft.ElevatedButton(
                    content=ft.Text("🌱 다시하기", weight="bold"),
                    on_click=reset_game,
                    style=ft.ButtonStyle(
                        bgcolor="#A8D5BA",
                        color="white",
                        padding=15,
                        shape=ft.RoundedRectangleBorder(radius=12)
                    )
                )
            ],
            horizontal_alignment="center",
            spacing=10
        ),
        bgcolor="white",
        padding=25,
        border_radius=25,
        shadow=ft.BoxShadow(
            blur_radius=20,
            spread_radius=1,
            color="#E6E6FA"
        ),
        width=400,
        height=480
    )

    # ================= 전체 =================
    page.add(
        ft.Stack(
            [
                background,
                ft.Column(
                    [title, game_card],
                    horizontal_alignment="center"
                )
            ],
            expand=True
        )
    )

ft.app(target=main)