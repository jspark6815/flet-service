import flet as ft
print("Flet Web Server is starting...")
def main(page: ft.Page):
    page.add(ft.Text(value="Containerized Flet app!"))

ft.app(target=main, view=None, port=8080)