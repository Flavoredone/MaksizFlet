import flet as ft

from results import imgres, value


def example(page):
    if not imgres:
        value.append("пустого запроса")
        res = []
        pass
    else:
        res = [
            ft.Image(
                src=f"kivy/search/results/{img}.jpg",
                width=400,
            )
            for img in imgres
        ]

        imgres.clear()
        try:
            value.remove("пустого запроса")
        except ValueError:
            pass

    return ft.Row(
        expand=True,
        # auto_scroll=True,
        # scroll=ft.ScrollMode.ALWAYS,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                controls=[
                    ft.Text(f'Результат для "{value[-1]}":'),
                    ft.Column(controls=res)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
            )
        ],
    )


def main(page: ft.Page):
    page.title = "RES"
    page.window_width = 390
    page.window_height = 844
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
