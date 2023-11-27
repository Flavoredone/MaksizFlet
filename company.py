import flet as ft


def example(page):

    img = ft.Image(
        src="assets/kivy/company/comp_menu.jpg",
        height=int(int(page.height) / 1.2),
        width=int(int(page.height) / 2.37),
    )

    def history(e):
        img.src = str("assets/kivy/company/comp_1.jpg")
        e.control.page.update()

    def mission(e):
        img.src = str("assets/kivy/company/comp_2.jpg")
        e.control.page.update()

    def uses(e):
        img.src = str("assets/kivy/company/comp_3.jpg")
        e.control.page.update()

    return ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            ft.FilledButton(
                                            content=ft.Column([ft.Text("ИСТОРИЯ", size=10)]),
                                            on_click=history,
                                            width=int(int(img.width)/3),
                                            ),
                            ft.FilledButton(
                                            content=ft.Column(
                                                [
                                                    ft.Text("МИССИЯ", size=10)
                                                ]
                                            ),
                                            on_click=mission,
                                            width=int(int(img.width)/3),
                                            ),
                            ft.FilledButton(
                                            content=ft.Column(
                                                [
                                                    ft.Text("ЦЕННОСТИ", size=10)
                                                ]
                                            ),
                                            on_click=uses,
                                            width=int(int(img.width)/3),
                                            ),
                        ]
                    ),
                    img
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
    )


def main(page: ft.Page):
    page.title = "О КОМПАНИИ"
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)