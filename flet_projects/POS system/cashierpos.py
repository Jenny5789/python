import flet as ft
import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "mart.db")


# =========================
def db():
    return sqlite3.connect(DB_PATH)


def init_db():
    con = db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            date TEXT,
            method TEXT
        )
    """)

    con.commit()
    con.close()


def get_products():
    con = db()
    cur = con.cursor()
    cur.execute("SELECT name, price, stock, category FROM products")
    rows = cur.fetchall()
    con.close()
    return rows


def price_map():
    return {p[0]: p[1] for p in get_products()}


def get_categories():
    con = db()
    cur = con.cursor()
    cur.execute("SELECT DISTINCT category FROM products")
    cats = [r[0] for r in cur.fetchall()]
    con.close()
    return ["전체"] + sorted(cats)


# =========================
def main(page: ft.Page):

    init_db()

    page.title = "JS POS"
    page.bgcolor = "#0B0F14"
    page.padding = 10

    cart = {}
    search = ""
    category = "전체"

    # =========================
    def add(name):
        cart[name] = cart.get(name, 0) + 1
        render_receipt()

    def update_qty(name, value):
        try:
            if value == "":
                return
            qty = int(value)
            if qty <= 0:
                cart.pop(name, None)
            else:
                cart[name] = qty
        except:
            pass
        render_receipt()

    # =========================
    receipt_list = ft.ListView(expand=True, spacing=5)
    total_text = ft.Text("TOTAL 0원", size=18, color="#22C55E")

    def render_receipt():
        receipt_list.controls.clear()

        prices = price_map()
        total = 0

        for name, qty in cart.items():
            unit = prices.get(name, 0)
            amount = unit * qty
            total += amount

            receipt_list.controls.append(
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,  # 🔥 중앙정렬
                    controls=[
                        ft.Text(name, width=140, color="white"),
                        ft.TextField(
                            value=str(qty),
                            width=60,
                            text_align=ft.TextAlign.CENTER,
                            on_change=lambda e, n=name: update_qty(n, e.control.value),
                            bgcolor="#111827",
                            color="white",
                        ),
                        ft.Text(f"{unit:,}", width=80, color="#E5E7EB"),
                        ft.Text(f"{amount:,}", width=100, color="#22C55E"),
                    ]
                )
            )

        total_text.value = f"TOTAL {total:,}"
        page.update()

    # =========================
    # CATEGORY (색 유지)
    # =========================
    def select_category(c):
        nonlocal category
        category = c
        render_products()

    def category_bar():
        return ft.Container(
            height=55,
            content=ft.Row(
                scroll="auto",
                controls=[
                    ft.Container(
                        padding=10,
                        margin=3,
                        bgcolor="#22C55E" if c == category else "#1F2937",
                        border_radius=8,
                        content=ft.Text(
                            c,
                            size=15,
                            color="black" if c == category else "white"
                        ),
                        on_click=lambda e, c=c: select_category(c)
                    )
                    for c in get_categories()
                ]
            )
        )

    # =========================
    product_grid = ft.GridView(
        expand=True,
        max_extent=180,
        spacing=10
    )

    def render_products():
        product_grid.controls.clear()

        for name, price, stock, cat in get_products():

            if search and search not in name.lower():
                continue

            if category != "전체" and category != cat:
                continue

            product_grid.controls.append(
                ft.Container(
                    padding=12,
                    bgcolor="#111827",
                    border_radius=10,
                    content=ft.Column(
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(name, size=16, color="white", text_align=ft.TextAlign.CENTER),
                            ft.Text(f"{price:,}원", size=14, color="#94A3B8"),
                            ft.Text(cat, size=13, color="#60A5FA"),
                        ]
                    ),
                    on_click=lambda e, n=name: add(n)
                )
            )

        page.update()

    # =========================
    def on_search(e):
        nonlocal search
        search = e.control.value.lower()
        render_products()

    search_box = ft.TextField(
        hint_text="상품 검색",
        on_change=on_search,
        color="white",
        bgcolor="#1F2937",
        hint_style=ft.TextStyle(color="#9CA3AF"),
    )

    # =========================
    def pay(method):
        con = db()
        cur = con.cursor()

        prices = price_map()
        total = sum(prices[n] * q for n, q in cart.items())

        cur.execute(
            "INSERT INTO sales (amount, date, method) VALUES (?, ?, ?)",
            (total, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), method)
        )

        con.commit()
        con.close()

        cart.clear()
        render_receipt()

    # =========================
    # HEADER (POS/ADMIN 유지)
    # =========================
    header = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Text("JS POS", size=22, color="white"),
            ft.Button("POS / ADMIN"),
        ]
    )

    # =========================
    left_panel = ft.Column(
        expand=True,
        spacing=8,
        controls=[
            header,
            search_box,
            category_bar(),
            product_grid
        ]
    )

    # =========================
    # RECEIPT PANEL
    # =========================
    right_panel = ft.Container(
        width=420,
        bgcolor="#0F172A",
        padding=10,
        content=ft.Column(
            controls=[

                # 🔥 RECEIPT 중앙정렬
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Text("RECEIPT", size=20, color="white")
                    ]
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,  # 🔥 중앙정렬
                    controls=[
                        ft.Text("품목", width=140, color="#E5E7EB"),
                        ft.Text("수량", width=60, color="#E5E7EB"),
                        ft.Text("단가", width=80, color="#E5E7EB"),
                        ft.Text("합계", width=100, color="#E5E7EB"),
                    ]
                ),

                ft.Container(expand=True, content=receipt_list),

                # 🔥 TOTAL 오른쪽 정렬
                ft.Row(
                    alignment=ft.MainAxisAlignment.END,
                    controls=[total_text]
                ),

                # 🔥 CASH / CARD 중앙
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Button("CASH", on_click=lambda e: pay("CASH")),
                        ft.Button("CARD", on_click=lambda e: pay("CARD")),
                    ]
                )
            ]
        )
    )

    # =========================
    page.add(
        ft.Row(
            expand=True,
            controls=[
                ft.Container(expand=2, content=left_panel),
                right_panel
            ]
        )
    )

    render_products()
    render_receipt()


ft.run(main)