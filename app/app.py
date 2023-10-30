import flet as ft
print("Flet Web Server is starting...")
def main(page: ft.Page):
    page.add(ft.Text(value="Containerized Flet app!"))
    page.add(ft.Text(value="feat. js.park"))

ft.app(target=main, view=None, port=8080)