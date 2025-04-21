import flet as ft

def main(page: ft.Page):
    page.title = "Control Remoto"
    page.theme_mode = ft.ThemeMode.LIGHT

    def btn_click(e):
        page.snack_bar = ft.SnackBar(ft.Text(f"{e.control.text} presionado"))
        page.snack_bar.open = True
        page.update()

    def create_button(text="", icon=None):
        return ft.ElevatedButton(
            text=text if not icon else None,
            icon=icon,
            width=60,
            height=60,
            shape=ft.CircleBorder(),
            on_click=btn_click
        )

    page.add(
        ft.Column([
            ft.Row([create_button(icon=ft.icons.POWER_SETTINGS_NEW), create_button(icon=ft.icons.HOME)], alignment="center"),
            ft.Row([create_button(icon=ft.icons.ARROW_BACK), create_button(icon=ft.icons.CAST), create_button(icon=ft.icons.EXIT_TO_APP)], alignment="center"),
            ft.Row([create_button("+"), create_button(icon=ft.icons.VOLUME_DOWN), create_button(icon=ft.icons.VOLUME_OFF)], alignment="center"),
            ft.Row([create_button("TV"), create_button("CC"), create_button(icon=ft.icons.KEYBOARD)], alignment="center"),
            ft.Row([ft.Container(content=ft.Text("D-pad"), width=120, height=120, alignment=ft.alignment.center, bgcolor=ft.colors.GREY_300, shape=ft.BoxShape.CIRCLE)], alignment="center")
        ])
    )

ft.app(target=main)
