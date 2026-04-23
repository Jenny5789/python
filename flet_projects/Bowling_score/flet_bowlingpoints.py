import flet as ft

# 🎨 컬러 팔레트
NEON_ORANGE = "#FF6A00"
HOT_ORANGE = "#FF8C00"
DARK_BG = "#0B0F1A"
CARD_BG = "#1A1F2E"
DISABLED = "#2A2F3F"

class BowlingApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "BOWLING SCORE"
        self.page.window_width = 1100
        self.page.window_height = 750
        self.page.bgcolor = DARK_BG
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 40

        self.rolls = []
        self.frame_scores = []
        self.is_first_roll = True

        # 🎯 UI
        self.total_text = ft.Text(
            value="0",
            size=70,
            weight=ft.FontWeight.W_900,
            italic=True,
            color=NEON_ORANGE,
        )

        self.status_text = ft.Text(
            value="READY TO ROLL!",
            size=14,
            color=HOT_ORANGE,
            weight=ft.FontWeight.BOLD
        )

        self.score_display = ft.Row(
            spacing=12,
            scroll=ft.ScrollMode.AUTO,
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.btn_grid = ft.Row(
            wrap=True,
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.setup_ui()

    def setup_ui(self):
        self.render_scoreboard()
        self.create_buttons()

        header = ft.Container(
            content=ft.Column([
                ft.Text("HIT THE PIN", size=40, weight=ft.FontWeight.W_900, color="white"),
                ft.Container(height=2, width=100, bgcolor=NEON_ORANGE),
            ], spacing=5),
            margin=ft.margin.only(bottom=30)
        )

        score_card = ft.Container(
            content=ft.Column([
                ft.Text("TOTAL SCORE", size=16, color="white70", weight=ft.FontWeight.BOLD),
                self.total_text,
                self.status_text,
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=30,
            bgcolor=CARD_BG,
            border_radius=30,
            border=ft.border.all(1, "white10"),
            shadow=ft.BoxShadow(blur_radius=15, color="#000055"),
            width=350
        )

        self.page.add(
            ft.Column(
                controls=[
                    header,
                    ft.Container(
                        content=self.score_display,
                        padding=20,
                        bgcolor=CARD_BG,
                        border_radius=25,
                        margin=ft.margin.only(bottom=30)
                    ),
                    ft.Row([
                        score_card,
                        ft.Column([
                            ft.Container(
                                content=self.btn_grid,
                                padding=30,
                                bgcolor=CARD_BG,
                                border_radius=30,
                                width=600,
                            ),
                            ft.TextButton(
                                "RESET GAME",
                                icon=ft.Icons.REFRESH_OUTLINED,
                                on_click=self.reset_game,
                                style=ft.ButtonStyle(color=NEON_ORANGE)
                            )
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
                    ], alignment=ft.MainAxisAlignment.CENTER, spacing=40)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    def create_buttons(self, max_pins=10):
        self.btn_grid.controls.clear()
        for i in range(11):
            is_disabled = (i > max_pins)
            self.btn_grid.controls.append(
                ft.Container(
                    content=ft.Text(str(i), weight=ft.FontWeight.BOLD, size=20),
                    alignment=ft.Alignment(0,0),
                    width=70,
                    height=70,
                    bgcolor=NEON_ORANGE if not is_disabled else DISABLED,
                    border_radius=15,
                    on_click=self.on_score_click if not is_disabled else None,
                    data=i,
                    animate=ft.Animation(300, "decelerate"),
                    opacity=1.0 if not is_disabled else 0.3,
                    shadow=ft.BoxShadow(blur_radius=15, color="#FF6A0022") if not is_disabled else None
                )
            )
        self.page.update()

    def on_score_click(self, e):
        score = e.control.data
        was_first = self.is_first_roll

        self.rolls.append(score)

        if self.is_first_roll:
            if score == 10:
                self.is_first_roll = True
                self.create_buttons(10)
            else:
                self.is_first_roll = False
                self.create_buttons(10 - score)
        else:
            self.is_first_roll = True
            self.create_buttons(10)

        total = self.calculate_score()
        self.total_text.value = str(total)

        if score == 10 and was_first:
            self.status_text.value = "🔥 STRIKE!!! 🔥"
            self.status_text.color = NEON_ORANGE
        elif not self.is_first_roll:
            self.status_text.value = "SET IT UP 😎"
            self.status_text.color = HOT_ORANGE
        else:
            self.status_text.value = "ROLL IT 🔥"
            self.status_text.color = "#FFD166"

        self.render_scoreboard()

    def calculate_score(self):
        score = 0
        idx = 0
        self.frame_scores = []

        for frame in range(10):
            if idx >= len(self.rolls):
                break

            # ⭐ 10프레임 처리
            if frame == 9:
                score += sum(self.rolls[idx:idx+3])
                self.frame_scores.append(score)
                break

            if self.rolls[idx] == 10:  # Strike
                bonus = 0
                if idx + 1 < len(self.rolls):
                    bonus += self.rolls[idx + 1]
                if idx + 2 < len(self.rolls):
                    bonus += self.rolls[idx + 2]

                score += 10 + bonus
                idx += 1

            elif idx + 1 < len(self.rolls):
                if self.rolls[idx] + self.rolls[idx + 1] == 10:  # Spare
                    bonus = self.rolls[idx + 2] if idx + 2 < len(self.rolls) else 0
                    score += 10 + bonus
                else:
                    score += self.rolls[idx] + self.rolls[idx + 1]
                idx += 2

            self.frame_scores.append(score)

        return score

    def render_scoreboard(self):
        self.score_display.controls.clear()
        temp = self.rolls[:]
        idx = 0

        for f in range(1, 11):
            r1, r2, r3 = "", "", ""
            total = str(self.frame_scores[f-1]) if f-1 < len(self.frame_scores) else ""

            if idx < len(temp):
                v1 = temp[idx]
                r1 = "X" if v1 == 10 else str(v1)
                idx += 1

                if f < 10:
                    if v1 != 10 and idx < len(temp):
                        v2 = temp[idx]
                        r2 = "/" if v1 + v2 == 10 else str(v2)
                        idx += 1
                else:
                    if idx < len(temp):
                        v2 = temp[idx]
                        r2 = "X" if v2 == 10 else ("/" if v1+v2==10 and v1!=10 else str(v2))
                        idx += 1
                    if idx < len(temp):
                        v3 = temp[idx]
                        r3 = "X" if v3 == 10 else str(v3)
                        idx += 1

            self.score_display.controls.append(
                ft.Container(
                    width=90,
                    height=120,
                    bgcolor=CARD_BG if total else DARK_BG,
                    border_radius=15,
                    padding=10,
                    content=ft.Column([
                        ft.Text(f"{f}F", size=10, color="white54", weight=ft.FontWeight.BOLD),
                        ft.Row([
                            ft.Text(r1, size=16, weight="bold"),
                            ft.Text(r2, size=16, weight="bold"),
                            ft.Text(r3, size=16, weight="bold") if f==10 else ft.Container()
                        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10),
                        ft.Container(height=5),
                        ft.Text(total, size=22, weight="w900", color=NEON_ORANGE)
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=5),
                    animate=ft.Animation(400, "bounceOut")
                )
            )
        self.page.update()

    def reset_game(self, e):
        self.rolls = []
        self.frame_scores = []
        self.is_first_roll = True
        self.total_text.value = "0"
        self.status_text.value = "READY TO ROLL!"
        self.status_text.color = HOT_ORANGE
        self.create_buttons(10)
        self.render_scoreboard()


def main(page: ft.Page):
    BowlingApp(page)


ft.app(target=main)