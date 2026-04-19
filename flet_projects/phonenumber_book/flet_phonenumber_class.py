import flet as ft

class PhoneBookApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "전화번호부"
        self.page.theme_mode = ft.ThemeMode.LIGHT

        self.page.window.width = 450
        self.page.window.height = 800

        self.page.bgcolor = "#FFF8E1"
        self.page.padding = 20
        self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.phone_book = {}

        self.input_style = {"width": 380, "border_radius": 10, "bgcolor": "white"}
        self.name_field = ft.TextField(label="👤 이름", **self.input_style)
        self.phone_field = ft.TextField(label="📞 전화번호", **self.input_style)
        self.email_field = ft.TextField(label="📧 이메일", **self.input_style)
        self.job_field = ft.TextField(label="🏢 직장명", **self.input_style)

        self.list_view = ft.ListView(height=300, spacing=10, width=400)
        self.page.scroll = "auto"

        self.setup_ui()

    def show_message(self, text):
        snack = ft.SnackBar(content=ft.Text(text))
        self.page.overlay.append(snack)
        snack.open = True
        self.page.update()

    def create_menu_button(self, emoji, text, color, on_click):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(emoji, size=26),
                    ft.Text(text, size=12)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=3
            ),
            width=70,
            height=70,
            bgcolor=color,
            border_radius=35,
            on_click=on_click
        )

    def setup_ui(self):
        btn_add = self.create_menu_button(
            "➕", "추가", "#F3E5F5", self.add_contact
        )
        btn_search = self.create_menu_button(
            "🔎", "검색", "#E3F2FD", self.search_contact
        )
        btn_list = self.create_menu_button(
            "📑", "목록", "#E4DCDC", self.refresh_list
        )

        menu_row = ft.Row(
            [btn_add, btn_search, btn_list],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15
        )

        self.page.add(
            ft.Text("전화번호부", size=34, weight="bold", color="#1565C0"),
            menu_row,
            ft.Divider(height=20, color="#90CAF9"),
            self.name_field,
            self.phone_field,
            self.email_field,
            self.job_field,
            ft.Container(height=10),
            self.list_view
        )

    def add_contact(self, e):
        name = self.name_field.value.strip()

        if not name:
            self.show_message("이름을 입력하세요!")
            return

        if name in self.phone_book:
            self.show_message("이미 존재하는 이름입니다.")
            return

        self.phone_book[name] = {
            "전화번호": self.phone_field.value.strip(),
            "이메일": self.email_field.value.strip(),
            "직업": self.job_field.value.strip()
        }

        self.clear_fields()
        self.refresh_list()
        self.show_message("추가되었습니다.")

    def search_contact(self, e):
        name = self.name_field.value.strip()

        if not name:
            self.show_message("검색할 이름을 입력하세요.")
            return

        if name in self.phone_book:
            self.list_view.controls.clear()
            self.list_view.controls.append(
                self.create_card(name, self.phone_book[name])
            )
            self.page.update()
        else:
            self.show_message("찾는 이름이 없습니다.")

    def delete_contact(self, e, name):
        if name in self.phone_book:
            del self.phone_book[name]
            self.refresh_list()
            self.show_message(f"{name} 삭제됨")

    def refresh_list(self, e=None):
        self.list_view.controls.clear()

        for name, info in self.phone_book.items():
            self.list_view.controls.append(self.create_card(name, info))

        self.page.update()

    def create_card(self, name, info):
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text(name, weight="bold", size=18),
                        ft.IconButton(
                            icon=ft.Icons.DELETE,
                            icon_color="red",
                            on_click=lambda e, n=name: self.delete_contact(e, n)
                        )
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Text(f"📞 {info['전화번호']}"),
                    ft.Text(f"📧 {info['이메일']}"),
                    ft.Text(f"🏢 {info['직업']}")
                ]),
                padding=15,
                bgcolor="white",
                border_radius=10
            ),
            width=360
        )

    def clear_fields(self):
        self.name_field.value = ""
        self.phone_field.value = ""
        self.email_field.value = ""
        self.job_field.value = ""
        self.page.update()


def main(page: ft.Page):
    PhoneBookApp(page)


if __name__ == "__main__":
    ft.app(target=main)