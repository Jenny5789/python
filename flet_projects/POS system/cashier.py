import flet as ft
import sqlite3
import os


# =========================
# DB PATH (고정)
# =========================
DB_PATH = os.path.join(os.path.dirname(__file__), "mart.db")


def db():
    return sqlite3.connect(DB_PATH)


def init_db():
    con = db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            name TEXT PRIMARY KEY,
            price INTEGER,
            stock INTEGER,
            category TEXT,
            sold INTEGER DEFAULT 0
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    con.commit()
    con.close()


# =========================
def main(page: ft.Page):

    init_db()

    page.title = "FINAL POS"
    page.bgcolor = "#0B0F14"
    page.window_width = 1200
    page.window_height = 800

    cart = {}
    selected_category = "전체"

    categories = ["전체", "생활", "식품", "조미료", "간식", "주류", "신선"]

    # =========================
    def load_products():
        con = db()
        cur = con.cursor()

        if selected_category == "전체":
            cur.execute("SELECT name, price, stock, category FROM products")
        else:
            cur.execute(
                "SELECT name, price, stock, category FROM products WHERE category=?",
                (selected_category,)
            )

        data = cur.fetchall()
        con.close()
        return data

    # =========================
    def add(name):
        cart[name] = cart.get(name, 0) + 1
        render_cart()

    def remove(name):
        if name in cart:
            cart[name] -= 1
            if cart[name] <= 0:
                del cart[name]
        render_cart()

    # =========================
    def render_cart():

        cart_view.controls.clear()

        subtotal = 0

        for name, qty in cart.items():

            con = db()
            cur = con.cursor()
            cur.execute("SELECT price FROM products WHERE name=?", (name,))
            price = cur.fetchone()[0]
            con.close()

            item_total = price * qty
            vat = int(item_total * 0.1)
            total = item_total + vat

            subtotal += item_total

            cart_view.controls.append(
                ft.Container(
                    padding=6,
                    bgcolor="#111827",
                    border_radius=6,
                    content=ft.Row(
                        controls=[
                            ft.Text(name, expand=2, color="white"),
                            ft.Text(str(qty), width=40, color="white"),
                            ft.Text(f"{price:,}", width=60, color="#94A3B8"),
                            ft.Text(f"{item_total:,}", width=70, color="white"),
                            ft.Text(f"{vat:,}", width=60, color="#F59E0B"),
                            ft.Text(f"{total:,}", width=70, color="white"),

                            ft.TextButton(
                                "X",
                                on_click=lambda e, n=name: remove(n),
                                style=ft.ButtonStyle(color="#EF4444")
                            )
                        ]
                    )
                )
            )

        subtotal_text.value = f"합계: {subtotal:,}원"
        vat_text.value = f"부가세: {int(subtotal*0.1):,}원"
        total_text.value = f"총액: {int(subtotal*1.1):,}원"

        page.update()

    # =========================
    def pay(e):

        con = db()
        cur = con.cursor()

        total = 0

        for name, qty in cart.items():
            cur.execute("SELECT price FROM products WHERE name=?", (name,))
            price = cur.fetchone()[0]

            total += price * qty

            cur.execute("""
                UPDATE products
                SET stock = stock - ?, sold = sold + ?
                WHERE name=?
            """, (qty, qty, name))

        cur.execute("INSERT INTO sales (amount) VALUES (?)", (int(total * 1.1),))

        con.commit()
        con.close()

        cart.clear()
        render_cart()

    # =========================
    def set_category(cat):
        nonlocal selected_category
        selected_category = cat
        render_products()

    def search(e):
        render_products(e.control.value.lower())

    # =========================
    grid = ft.GridView(
        expand=True,
        max_extent=160,
        spacing=8,
        run_spacing=8
    )

    cart_view = ft.ListView(expand=True, spacing=5)

    subtotal_text = ft.Text("", size=14, color="white")
    vat_text = ft.Text("", size=14, color="#F59E0B")
    total_text = ft.Text("", size=26, color="#22C55E", weight="bold")

    search_field = ft.TextField(
        hint_text="상품 검색",
        bgcolor="#1F2937",
        color="white",
        on_change=search
    )

    # =========================
    def render_products(keyword=""):

        grid.controls.clear()

        for name, price, stock, cat in load_products():

            if keyword and keyword not in name.lower():
                continue

            grid.controls.append(
                ft.Container(
                    width=160,
                    padding=8,
                    bgcolor="#0F172A",
                    border_radius=10,
                    border=ft.Border.all(2, "#1F2937"),

                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(name, size=13, color="white"),
                            ft.Text(f"{price:,}원", size=10, color="#94A3B8"),

                            ft.Container(height=5),

                            ft.ElevatedButton(
                                "ADD",
                                bgcolor="#22C55E",
                                color="black",
                                on_click=lambda e, n=name: add(n)
                            )
                        ]
                    )
                )
            )

        page.update()

    # =========================
    render_products()

    # =========================
    page.add(

        ft.Text("FINAL POS SYSTEM", size=28, color="white"),

        search_field,

        ft.Row(
            controls=[
                ft.ElevatedButton(
                    c,
                    on_click=lambda e, x=c: set_category(x)
                )
                for c in categories
            ]
        ),

        ft.Row(
            expand=True,
            controls=[

                ft.Container(expand=3, content=grid),

                ft.Container(
                    width=500,
                    bgcolor="#111827",
                    padding=12,
                    border_radius=10,

                    content=ft.Column(
                        controls=[

                            ft.Text("RECEIPT", size=24, color="white", weight="bold"),
                            ft.Divider(),

                            # HEADER
                            ft.Row([
                                ft.Text("품목", expand=2, color="#94A3B8"),
                                ft.Text("수량", width=40, color="#94A3B8"),
                                ft.Text("단가", width=60, color="#94A3B8"),
                                ft.Text("금액", width=70, color="#94A3B8"),
                                ft.Text("VAT", width=60, color="#94A3B8"),
                                ft.Text("합계", width=70, color="#94A3B8"),
                                ft.Text("", width=30),
                            ]),

                            ft.Divider(),

                            cart_view,

                            ft.Divider(),

                            # RIGHT ALIGNED TOTALS (alignment 안 씀)
                            ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.END,
                                controls=[
                                    subtotal_text,
                                    vat_text,
                                    total_text
                                ]
                            ),

                            ft.Container(height=10),

                            ft.Row(
                                alignment=ft.MainAxisAlignment.CENTER,
                                controls=[
                                    ft.ElevatedButton(
                                        "CASH",
                                        bgcolor="#F59E0B",
                                        color="black",
                                        on_click=pay
                                    ),
                                    ft.ElevatedButton(
                                        "CARD",
                                        bgcolor="#22C55E",
                                        color="black",
                                        on_click=pay
                                    )
                                ]
                            )
                        ]
                    )
                )
            ]
        )
    )


ft.app(target=main)