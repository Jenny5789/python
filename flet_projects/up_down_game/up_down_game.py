import flet as ft
import random
def main(page: ft.Page):
    page.title = "UP&DOWN GAME"
    page.window.width = 300
    page.window.height = 180

    answer = random.randint(1,100)
    input_num = ft.TextField()
    msg = ft.Text()
    def check(e):
        n = int(input_num.value)

        if n > answer:
            msg.value = "DOWN"
        elif n < answer:
            msg.value = "UP"
        else:
            msg.value = "CORRECT"
        page.update()

    page.add(
        ft.Text("Enter a number between 1 and 100 : "),
    input_num,
    ft.ElevatedButton("확인", on_click=check),
    msg
)

ft.app(main)
