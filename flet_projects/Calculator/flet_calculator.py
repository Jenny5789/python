import flet as ft

def main(page: ft.Page):
    # --- 색상 테마 ---
    MAIN_BLUE = "#3A608F" 
    
    # --- 창 설정 ---
    page.title = " Num-Picker"
    page.window.width = 480
    page.window.height = 800   # 박스들이 다 들어오도록 높이 넉넉히 조절
    page.window_resizable = False
    page.padding = 35
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE

    # --- [로직] 숫자 추출 함수 ---
    def extract_numbers(input_data):
        numbers = []
        not_numbers = []
        for item in input_data:
            if isinstance(item, (int, float)):
                numbers.append(float(item))
            elif isinstance(item, (list, tuple)):
                for sub_item in item:
                    if isinstance(sub_item, (int, float)):
                        numbers.append(float(sub_item))
                    else:
                        not_numbers.append(sub_item)
            else:
                not_numbers.append(item)
        return numbers, not_numbers

    # --- [이벤트] 초기화 버튼 ---
    def reset_event(e):
        input_field.value = ""
        error_text.value = ""
        result_container.visible = False
        page.update()

    # --- [이벤트] 계산 실행 버튼 ---
    def calculate_event(e):
        if not input_field.value:
            error_text.value = "숫자를 입력해주세요."
            page.update()
            return

        raw_input = input_field.value.replace(',', ' ').split()
        raw_items = []
        for val in raw_input:
            try:
                raw_items.append(float(val))
            except ValueError:
                raw_items.append(val)

        final_numbers, not_numbers = extract_numbers(raw_items)

        if not final_numbers:
            error_text.value = "계산할 숫자가 없습니다."
            result_container.visible = False
            page.update()
            return

        # 사칙연산 로직
        add_result = final_numbers[0]
        sub_result = final_numbers[0]
        mul_result = final_numbers[0]
        div_result = final_numbers[0]
        div_error = False

        for i in range(1, len(final_numbers)):
            num = final_numbers[i]
            add_result += num
            sub_result -= num
            mul_result *= num
            if num != 0:
                div_result /= num
            else:
                div_error = True

        avg = sum(final_numbers) / len(final_numbers)
        
        error_text.value = f"제외됨: {not_numbers}" if not_numbers else "분석 완료"
        error_text.color = MAIN_BLUE
        
        # 결과 항목 업데이트
        res_list.controls = [
            create_result_row("인식된 데이터", f"{len(final_numbers)}개"),
            ft.Divider(height=1, color=ft.Colors.GREY_200),
            create_result_row("더하기 (+)", f"{add_result:,.2f}"),
            create_result_row("빼기 (-)", f"{sub_result:,.2f}"),
            create_result_row("곱하기 (×)", f"{mul_result:,.2f}"),
            create_result_row("나누기 (÷)", f"{div_result:,.2f}" if not div_error else "0 포함 불가"),
            ft.Divider(height=1, color=ft.Colors.GREY_200),
            create_result_row("평균 (AVG)", f"{avg:,.2f}", ft.Colors.BLUE_700),
            create_result_row("최댓값 (MAX)", f"{max(final_numbers):,.2f}", ft.Colors.GREEN_700),
            create_result_row("최솟값 (MIN)", f"{min(final_numbers):,.2f}", ft.Colors.ORANGE_800),
        ]
        result_container.visible = True
        page.update()

    def create_result_row(label, value, color=MAIN_BLUE):
        return ft.Row(
            controls=[
                ft.Text(label, color=ft.Colors.GREY_600, size=12),
                ft.Text(value, weight="bold", color=color, size=13),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

    # --- UI 컴포넌트 ---
    title_text = ft.Text("🧐숫자 추출 계산기🧐", size=28, weight="bold", color=MAIN_BLUE)

    # 1. 입력 박스 (높이 160)
    input_field = ft.TextField(
        label="숫자 입력",
        multiline=True,
        min_lines=6, 
        max_lines=6,
        border_radius=15,
        text_align=ft.TextAlign.CENTER,
        border_color=MAIN_BLUE,
        focused_border_color=MAIN_BLUE,
        label_style=ft.TextStyle(color=MAIN_BLUE),
        width=400,
        height=160,
    )

    # 2. 계산 버튼 박스
    calc_button = ft.FilledButton(
        content=ft.Row(
            [ft.Icon(ft.Icons.ANALYTICS_ROUNDED), ft.Text("분석 및 계산 실행", weight="bold")],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        on_click=calculate_event,
        width=400,
        height=55,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor=MAIN_BLUE,
            color=ft.Colors.WHITE
        )
    )

    # 3. 초기화 버튼 박스 (계산 버튼과 같은 크기/모양의 박스로 제작)
    reset_button = ft.OutlinedButton(
        content=ft.Row(
            [ft.Icon(ft.Icons.REFRESH_ROUNDED), ft.Text("데이터 초기화 (Reset)", weight="bold")],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        on_click=reset_event,
        width=400,
        height=55,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            color=MAIN_BLUE,
            side=ft.BorderSide(2, MAIN_BLUE), 
        )
    )

    error_text = ft.Text("", size=11)
    res_list = ft.Column(spacing=7)
    
    # 4. 결과 박스 
    result_container = ft.Container(
        content=res_list,
        padding=20,
        bgcolor=ft.Colors.GREY_50,
        border=ft.Border.all(1, MAIN_BLUE),
        border_radius=15,
        visible=False,
        width=400,
        height=280,
    )

    # 페이지 배치
    page.add(
        ft.Column(
            [
                ft.Row([title_text], alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=10),
                input_field,
                calc_button,
                reset_button,
                ft.Row([error_text], alignment=ft.MainAxisAlignment.CENTER),
                result_container,
            ],
            spacing=12,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    ft.run(main)