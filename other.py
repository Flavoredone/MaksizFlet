import flet as ft


def example(page):
    img = ft.Image(
        src=f"oth/4.jpg",
        width=int(int(page.width) / 2),
    )

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
