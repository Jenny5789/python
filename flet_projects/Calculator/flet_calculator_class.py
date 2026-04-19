import flet as ft
import re


class CalculatorApp(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            padding=20,
            expand=True,
            bgcolor="white"
        )

        self._page = page
        self.raw_data = []

        # =========================
        # 입력창
        # =========================
        self.input_field = ft.TextField(
            label="데이터 입력",
            expand=True,
            on_submit=self.add_item
        )

        # =========================
        # 리스트
        # =========================
        self.list_view = ft.ListView(
            expand=True,
            spacing=8
        )

        self.list_container = ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text("📋 입력된 데이터", weight="bold", color="#424242"),
                    ft.Icon(ft.Icons.SWAP_VERT, color="grey", size=16)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),

                ft.Container(
                    content=self.list_view,
                    height=300
                )
            ]),
            padding=10,
            border_radius=12,
            border=ft.border.all(1, "#DEE2E6"),
            bgcolor="#FFFFFF"
        )

        # =========================
        # 결과
        # =========================
        self.result_container = ft.Column(
            spacing=10,
            scroll=ft.ScrollMode.AUTO
        )

        # =========================
        # UI
        # =========================
        self.content = ft.Row(
            expand=True,
            spacing=20,
            controls=[

                # LEFT
                ft.Container(
                    width=360,
                    content=ft.Column([
                        ft.Text(
                            "🔢 Number Data Handler",
                            size=24,
                            weight="bold",
                            color="#263238"
                        ),

                        ft.Row([
                            self.input_field,
                            ft.ElevatedButton(
                                content=ft.Icon(ft.Icons.ADD),
                                bgcolor="#2196F3",
                                color="white",
                                on_click=self.add_item
                            )
                        ]),

                        ft.Divider(),

                        self.list_container,

                        ft.Row(
                            [
                                ft.OutlinedButton(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.CALCULATE),
                                        ft.Text("계산하기")
                                    ]),
                                    style=ft.ButtonStyle(
                                        side=ft.BorderSide(1, "#90A4AE"),
                                        color="#1E88E5"
                                    ),
                                    on_click=self.calculate
                                ),

                                ft.OutlinedButton(
                                    content=ft.Row([
                                        ft.Icon(ft.Icons.REFRESH),
                                        ft.Text("초기화")
                                    ]),
                                    style=ft.ButtonStyle(
                                        side=ft.BorderSide(1, "#90A4AE")
                                    ),
                                    on_click=self.clear_all
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        )
                    ], spacing=12)
                ),

                # RIGHT
                ft.Container(
                    width=350,
                    padding=15,
                    border_radius=12,
                    bgcolor="#F8F9FA",
                    content=self.result_container
                )
            ]
        )

    # =========================
    # 숫자 추출
    # =========================
    def _extract_numbers(self):
        numbers = []
        non_numbers = []
        pattern = r"[-+]?\d*\.\d+|\d+"

        for item in self.raw_data:
            matches = re.findall(pattern, item)
            if matches:
                numbers.extend(map(float, matches))
            else:
                non_numbers.append(item)

        return numbers, non_numbers

    def _format_value(self, value):
        v = round(value, 2)
        return str(int(v)) if v == int(v) else f"{v:.2f}"

    # =========================
    # 카드 UI
    # =========================
    def make_card(self, label, value, color):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Text(label, weight="bold"),
                    ft.Text(value, weight="bold")
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=12,
            border_radius=10,
            bgcolor=color
        )

    # =========================
    # 리스트 아이템 (삭제 버튼 작게)
    # =========================
    def make_item_card(self, value):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Text(value, expand=True),

                    ft.IconButton(
                        icon=ft.Icons.DELETE,
                        icon_size=16,   # ⭐ 작게
                        icon_color="#E53935",
                        tooltip="삭제",
                        on_click=lambda e, v=value: self.remove_item(v)
                    )
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=10,
            border_radius=10,
            bgcolor="#E3F2FD"
        )

    # =========================
    # 추가
    # =========================
    def add_item(self, e):
        val = self.input_field.value.strip()
        if not val:
            return

        self.raw_data.append(val)
        self.list_view.controls.append(self.make_item_card(val))

        self.input_field.value = ""
        self.input_field.focus()
        self._page.update()

    # =========================
    # 삭제
    # =========================
    def remove_item(self, value):
        if value in self.raw_data:
            self.raw_data.remove(value)

        self.list_view.controls = [
            c for c in self.list_view.controls
            if value not in c.content.controls[0].value
        ]

        self._page.update()

    # =========================
    # 초기화
    # =========================
    def clear_all(self, e):
        self.raw_data.clear()
        self.list_view.controls.clear()
        self.result_container.controls.clear()
        self._page.update()

    # =========================
    # 계산 (완전 복구 버전)
    # =========================
    def calculate(self, e):
        nums, non_nums = self._extract_numbers()
        self.result_container.controls.clear()

        if not nums:
            self.result_container.controls.append(
                ft.Text("계산할 숫자가 없습니다.", color="red")
            )
        else:
            add_res = sum(nums)
            sub_res = nums[0] - sum(nums[1:]) if len(nums) > 1 else nums[0]

            mul_res = 1
            for n in nums:
                mul_res *= n

            div_res = nums[0]
            div_error = False
            for n in nums[1:]:
                if n != 0:
                    div_res /= n
                else:
                    div_error = True

            self.result_container.controls.append(
                ft.Column([
                    self.make_card("➕ 합계", self._format_value(add_res), "#E3F2FD"),
                    self.make_card("➖ 차이", self._format_value(sub_res), "#FFF3E0"),
                    self.make_card("✖ 곱", self._format_value(mul_res), "#F3E5F5"),
                    self.make_card(
                        "➗ 나눗셈",
                        "계산불가" if div_error else self._format_value(div_res),
                        "#E8F5E9"
                    ),
                    self.make_card("📊 평균", self._format_value(sum(nums)/len(nums)), "#F5F5F5"),
                    self.make_card("🔺 최대", self._format_value(max(nums)), "#FFEBEE"),
                    self.make_card("🔻 최소", self._format_value(min(nums)), "#E3F2FD"),
                ], spacing=8)
            )

        if non_nums:
            self.result_container.controls.append(
                ft.Container(
                    content=ft.Column([
                        ft.Text("⚠ 숫자가 아닌 데이터", weight="bold"),
                        ft.Divider(),
                        ft.Column([
                            ft.Text(f"• {n}") for n in non_nums
                        ])
                    ]),
                    padding=15,
                    border_radius=12,
                    bgcolor="#FFF8E1"
                )
            )

        self._page.update()


# =========================
# 실행
# =========================
def main(page: ft.Page):
    page.title = "Number Data Handler"
    page.bgcolor = "#F1F3F5"
    page.scroll = ft.ScrollMode.AUTO
    page.add(CalculatorApp(page))


ft.run(main)