import flet as ft
import re

class CalculatorApp(ft.Container):
    def __init__(self, page):
        super().__init__(padding=20)
        self.page_ref = page  # 충돌을 피하기 위해 이름을 page_ref로 변경
        self.raw_data = []

        self.input_field = ft.TextField(
            label="데이터 입력 ", 
            width=300,
            on_submit=self.add_item,
            autofocus=True
        )
        self.list_view = ft.ListView(height=150, spacing=5)
        self.result_container = ft.Column()

        self.content = ft.Column(
            width=400,
            horizontal_alignment="center",
            spacing=10,
            controls=[
                ft.Text("🔢 Number Data Handler", size=25, weight="bold"),
                ft.Row([self.input_field, ft.ElevatedButton("추가", on_click=self.add_item)], alignment="center"),
                ft.Divider(),
                ft.Text("입력된 데이터:"),
                ft.Container(self.list_view, border=ft.border.all(1, "grey"), height=150, padding=10),
                ft.Row([
                    ft.ElevatedButton("계산하기", on_click=self.calculate),
                    ft.OutlinedButton("초기화", on_click=self.clear_all)
                ], alignment="center"),
                ft.Divider(),
                self.result_container
            ]
        )

        # 숫자 추출 로직
    def _extract_numbers(self):
        numbers = []
        non_numbers = []
        
        for item in self.raw_data:
            if isinstance(item, str):
                match = re.search(r"[-+]?\d*\.\d+|\d+", item)
                if match:
                    numbers.append(float(match.group()))
                else:
                    non_numbers.append(item)
            elif isinstance(item, (int, float)):
                numbers.append(float(item))
            else:
                non_numbers.append(item)
        return numbers, non_numbers

    # 포맷팅 도우미
    def _format_value(self, value):
        rounded_val = round(value, 2)
        if rounded_val == int(rounded_val):
            return str(int(rounded_val))
        return f"{rounded_val:.2f}"

    # 이벤트 처리: 항목 추가
    def add_item(self, e):
        val = self.input_field.value.strip()
        if not val:
            return
        
        self.raw_data.append(val)
        self.list_view.controls.append(ft.Text(f"- {val}"))
        self.input_field.value = ""
        self.update()

    # 이벤트 처리: 초기화
    def clear_all(self, e):
        self.raw_data = []
        self.list_view.controls.clear()
        self.result_container.controls.clear()
        self.update()

    # 이벤트 처리: 계산
    def calculate(self, e):
        nums, non_nums = self._extract_numbers()
        self.result_container.controls.clear()
        
        if not nums:
            self.result_container.controls.append(ft.Text("계산할 숫자가 없습니다.", color="red"))
        else:
            add_res = sum(nums)
            sub_res = nums[0] - sum(nums[1:]) if len(nums) > 1 else nums[0]
            mul_res = 1
            for n in nums: mul_res *= n
            
            div_res = nums[0]
            div_error = False
            for n in nums[1:]:
                if n != 0: div_res /= n
                else: div_error = True
            
            results = [
                f"합계: {self._format_value(add_res)}",
                f"차이: {self._format_value(sub_res)}",
                f"곱: {self._format_value(mul_res)}",
                f"나눗셈: {'0 포함 계산불가' if div_error else self._format_value(div_res)}",
                f"평균: {self._format_value(sum(nums)/len(nums))}",
                f"최대/최소: {self._format_value(max(nums))} / {self._format_value(min(nums))}"
            ]
            
            for res in results:
                self.result_container.controls.append(ft.Text(res, size=16))
            
            if non_nums:
                self.result_container.controls.append(ft.Text(f"숫자 아님: {non_nums}", color="gray", italic=True))

        self.update()
def main(page: ft.Page):
    page.title = "Number Data Handler"
    page.window_width = 420
    page.window_height = 600
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    
    # 클래스 생성 시 page를 전달
    app = CalculatorApp(page)
    page.add(app)

if __name__ == "__main__":
    ft.app(target=main)