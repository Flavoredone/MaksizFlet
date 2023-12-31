import flet as ft


def example(page):

    img = ft.Image(
        src="kivy/company/comp_menu.jpg",
        height=int(int(page.height) / 1.2),
        width=int(int(page.height) / 2.37),
    )

    def history(e):
        img.src = str("kivy/company/comp_1.jpg")
        e.control.page.update()

    def mission(e):
        img.src = str("kivy/company/comp_2.jpg")
        e.control.page.update()

    def uses(e):
        img.src = str("kivy/company/comp_3.jpg")
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
                            ft.ElevatedButton(
                                            content=ft.Column([ft.Text("   ИСТОРИЯ   ", size=14, color="#ffffff")]),
                                            on_click=history,
                                            bgcolor="#F74F10",
                                            # width=int(int(img.width)/3.3),
                                            ),
                            ft.ElevatedButton(
                                            content=ft.Column(
                                                [
                                                    ft.Text("  МИССИЯ   ", size=14, color="#ffffff")
                                                ]
                                            ),
                                            on_click=mission,
                                            bgcolor="#F74F10",
                                            # width=int(int(img.width)/3.3),
                                            ),
                            ft.ElevatedButton(
                                            content=ft.Column(
                                                [
                                                    ft.Text("   ЦЕННОСТИ   ", size=14, color="#ffffff")
                                                ]
                                            ),
                                            on_click=uses,
                                            bgcolor="#F74F10",
                                            # width=int(int(img.width)/3.3),
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
