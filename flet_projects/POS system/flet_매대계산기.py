import flet as ft
import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(__file__), "mart.db")

# =========================
# DB
# =========================
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
            category TEXT
        )
    """)

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
    return {n: p for n, p, s, c in get_products()}


def get_categories():
    con = db()
    cur = con.cursor()
    cur.execute("SELECT DISTINCT category FROM products")
    cats = [r[0] for r in cur.fetchall()]
    con.close()
    return ["전체"] + sorted(cats)


def get_sales():
    con = db()
    cur = con.cursor()

    today = datetime.now().strftime("%Y-%m-%d")
    week_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")

    cur.execute("SELECT IFNULL(SUM(amount),0) FROM sales WHERE date LIKE ?", (today + "%",))
    today_sales = cur.fetchone()[0]

    cur.execute("SELECT IFNULL(SUM(amount),0) FROM sales WHERE date >= ?",(week_ago,))
    week_sales = cur.fetchone()[0]

    cur.execute("SELECT IFNULL(SUM(amount),0) FROM sales")
    total_sales = cur.fetchone()[0]

    con.close()
    return today_sales, week_sales, total_sales


# =========================
def main(page: ft.Page):

    init_db()

    page.title = "POS SYSTEM"
    page.bgcolor = "#0B0F14"
    page.padding = 10

    mode = "POS"

    cart = {}
    search = ""
    category = "전체"

    editing = None

    # =========================
    def toggle(e):
        nonlocal mode
        mode = "ADMIN" if mode == "POS" else "POS"

        if mode == "ADMIN":
            render_admin_left()

        render()

    # =========================
    # CART
    # =========================
    def add(name):
        cart[name] = cart.get(name, 0) + 1
        render_receipt()

    def update_qty(name, value):
        try:
            qty = int(value)
            if qty <= 0:
                cart.pop(name, None)
            else:
                cart[name] = qty
        except:
            pass
        render_receipt()

    # =========================
    # RECEIPT
    # =========================
    receipt_list = ft.ListView(expand=True, spacing=5)
    total_text = ft.Text("TOTAL 0", size=18, color="#22C55E")

    def render_receipt():
        receipt_list.controls.clear()

        prices = price_map()
        total = 0

        for name, qty in cart.items():
            unit = prices.get(name, 0)
            amount = unit * qty
            total += amount

            receipt_list.controls.append(
                ft.Row([
                    ft.Text(name, width=120, color="white"),
                    ft.TextField(
                        value=str(qty),
                        width=60,
                        text_align=ft.TextAlign.CENTER,
                        on_change=lambda e, n=name: update_qty(n, e.control.value),
                        bgcolor="#111827",
                        color="white"
                    ),
                    ft.Text(f"{unit:,}", width=80, color="#E5E7EB"),
                    ft.Text(f"{amount:,}", width=100, color="#22C55E"),
                ])
            )

        total_text.value = f"TOTAL {total:,}"
        page.update()

    # =========================
    # PRODUCTS
    # =========================
    product_grid = ft.GridView(expand=True, max_extent=170, spacing=10, run_spacing=10)

    def render_products():
        product_grid.controls.clear()

        for n, p, s, c in get_products():

            if search and search not in n.lower():
                continue

            if category != "전체" and category != c:
                continue

            product_grid.controls.append(
                ft.Container(
                    height=70,
                    padding=10,
                    bgcolor="#111827",
                    border_radius=10,

                    content=ft.Column([
                        ft.Text(n, color="white", text_align="center"),
                        ft.Text(f"{p:,}원", color="#94A3B8", text_align="center"),
                        ft.Text(f"재고 {s}", color="#60A5FA", text_align="center"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    on_click=lambda e, n=n: add(n)
                )
            )

        page.update()

    def on_search(e):
        nonlocal search
        search = e.control.value.lower()
        render_products()

    search_box = ft.TextField(
        hint_text="상품 검색",
        on_change=on_search,
        bgcolor="#1F2937",
        color="white"
    )

    def select_cat(c):
        nonlocal category
        category = c
        render_products()

    def category_bar():
        return ft.Container(
            height=50,
            content=ft.Row(
                scroll="auto",
                controls=[
                    ft.Container(
                        padding=8,
                        margin=3,
                        bgcolor="#22C55E" if c == category else "#1F2937",
                        border_radius=6,
                        content=ft.Text(c, color="white"),
                        on_click=lambda e, c=c: select_cat(c)
                    )
                    for c in get_categories()
                ]
            )
        )

    # =========================
    def pay(e):
        con = db()
        cur = con.cursor()

        prices = price_map()
        total = sum(prices[n] * q for n, q in cart.items())

        cur.execute(
            "INSERT INTO sales (amount, date, method) VALUES (?, ?, ?)",
            (total, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "CARD")
        )

        con.commit()
        con.close()

        cart.clear()
        render_receipt()

    # =========================
    # ADMIN
    # =========================
    product_list = ft.ListView(expand=True, spacing=2)

    name = ft.TextField(label="이름", width=500, color="white", filled=True, fill_color="#1F2937")
    price = ft.TextField(label="가격", width=500, color="white", filled=True, fill_color="#1F2937")
    stock = ft.TextField(label="재고", width=500,  color="white", filled=True, fill_color="#1F2937")
    cat = ft.TextField(label="카테고리", width=500,  color="white", filled=True, fill_color="#1F2937")

    def render_admin_left():
        product_list.controls.clear()

        product_list.controls.append(
            ft.Row([
                ft.Text("품명", width=120, color="white", text_align="center"),
                ft.Text("가격", width=120, color="white", text_align="center"),
                ft.Text("재고", width=120, color="white", text_align="center"),
                ft.Text("수정", width=120, color= "white", text_align="center"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        

        product_list.controls.append(ft.Divider())

        for n, p, s, c in get_products():
            product_list.controls.append(
                ft.Row([
                    ft.Text( n, width=120, color="white", text_align="center" ),
                    ft.Text(f"{p:,}", width=120, color="white", text_align="center"),
                    ft.Text(str(s), width=120, color="white",text_align="center" ),
                    ft.Button("수정", width=80, color="darkblue"),
                ],            alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
            )

        page.update()

    def save(e):
        con = db()
        cur = con.cursor()

        cur.execute("""
            UPDATE products
            SET price=?, stock=?, category=?
            WHERE name=?
        """, (int(price.value), int(stock.value), cat.value, name.value))

        con.commit()
        con.close()

        render_admin_left()
        render_products()

    # =========================
    # HEADER
    # =========================
    header = ft.Row([
        ft.Text("POS SYSTEM", size=22, color="white"),
        ft.Button("POS / ADMIN", on_click=toggle)
    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    # =========================
    # POS VIEW (FIXED RECEIPT TOP)
    # =========================
    def pos_view():

        return ft.Row([

            # LEFT
            ft.Container(
                expand=2,
                padding=10,
                border_radius=10,
                content=ft.Column([
                    search_box,
                    category_bar(),
                    product_grid
                ])
            ),

            # RIGHT (RECEIPT)
            ft.Container(
                width=380,
                bgcolor="#0F172A",
                padding=10,
                border_radius=10,
                content=ft.Column([

                    # 🔥 FIXED TOP RECEIPT HEADER
                    ft.Container(
                        content=ft.Column([
                            ft.Text("RECEIPT", size=20, weight="bold", color="white"),
                            ft.Row([
                                ft.Text("상품", width=120, color="white", text_align="left"),
                                ft.Text("수량", width=60, color="white", text_align="center"),
                                ft.Text("단가", width=60, color="white", text_align="center"),
                                ft.Text("합계", width=80, color="white", text_align="center"),
                            ])
                        ])
                    ),

                    # 🔥 SCROLL AREA ONLY
                    ft.Container(
                        expand=True,
                        content=receipt_list
                    ),

                    # TOTAL FIXED
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[total_text]
                    ),

                    ft.Row([
                        ft.Button("CASH", on_click=pay),
                        ft.Button("CARD", on_click=pay),
                    ], alignment=ft.MainAxisAlignment.CENTER)

                ])
            )

        ], expand=True)

    # =========================
    # ADMIN VIEW
    # =========================
    def admin_view():

        return ft.Row([

            # LEFT
            ft.Container(
                expand=2,
                bgcolor="#111827",
                border_radius=10,
                padding=10,
                content=product_list
            ),

            # RIGHT
            ft.Container(
                expand=1,
                padding=20,
                bgcolor="#111827",
                border=ft.border.all(1, "#1F2937"),
                border_radius=12,
                shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=1,
                color="#00000050",
            ),
                content=ft.Column([

                    ft.Text("PRODUCT EDIT", size=18, color="white"),
                    name, price, stock, cat,

                    ft.Row([
                        ft.Button("저장", on_click=save),
                        ft.Button("초기화"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                    ),

                    ft.Divider(),

                    ft.Text("SALES", color="white"),
                    ft.Text(f"오늘 매출: {get_sales()[0]:,}", color="#22C55E"),
                    ft.Text(f"주간 매출: {get_sales()[1]:,}", color="#FACC15"),
                    ft.Text(f"전체 누적 매출: {get_sales()[2]:,}", color="#60A5FA"),

                ])
            )

        ], expand=True)

    # =========================
    def render():
        page.controls.clear()

        page.add(header)

        if mode == "POS":
            page.add(pos_view())
        else:
            page.add(admin_view())

        page.update()

    # =========================
    render_products()
    render_receipt()
    render_admin_left()
    render()


ft.app(target=main)