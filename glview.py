import flet as ft
from results import gl


def example(page):
    img = ft.Image(
        src=f"oth/{gl[-1]}.jpg",
        width=int(int(page.height) / 1.4),
    )
    try:
        gl.clear()
    except ValueError:
        pass

    return ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    img
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
            )
        ],
    )


def main(page: ft.Page):
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
