import flet as ft
from results import cert
import certview


def example(page):
    def view1(e):
        cert.append(1)
        view(e)

    def view2(e):
        cert.append(2)
        view(e)

    def view3(e):
        cert.append(3)
        view(e)

    def view4(e):
        cert.append(4)
        view(e)

    def view5(e):
        cert.append(5)
        view(e)

    def view6(e):
        cert.append(6)
        view(e)

    def view7(e):
        cert.append(7)
        view(e)

    def view8(e):
        cert.append(8)
        view(e)

    def view9(e):
        cert.append(9)
        view(e)

    def view(e):
        page.views.append(
            ft.View(
                bgcolor="#333333",
                controls=[
                    ft.AppBar(bgcolor="#333333", title=ft.Text("ДОКУМЕНТАЦИЯ", color=f"#FFFFFF")),
                    certview.example(page),
                ],
            )
        )
        page.update()

    return ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=int(int(page.height) / 3.5),
                        spacing=70,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="cert/1.jpg"),
                                on_click=view1,
                            ),
                            ft.Container(
                                content=ft.Image(src="cert/2.jpg"),
                                on_click=view2,
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=int(int(page.height) / 3.5),
                        spacing=70,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="cert/3.jpg"),
                                on_click=view3,
                            ),
                            ft.Container(
                                content=ft.Image(src="cert/4.jpg"),
                                on_click=view4,
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=int(int(page.height) / 3.5),
                        spacing=70,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="cert/5.jpg"),
                                on_click=view5,
                            ),
                            ft.Container(
                                content=ft.Image(src="cert/6.jpg"),
                                on_click=view6,
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=int(int(page.height) / 3.5),
                        spacing=70,
                        controls=[

                            ft.Container(
                                content=ft.Image(src="cert/7.jpg"),
                                on_click=view7,
                            ),
                            ft.Container(
                                content=ft.Image(src="cert/8.jpg"),
                                on_click=view8,
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=int(int(page.height) / 3.5),
                        spacing=70,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="cert/9.jpg"),
                                on_click=view9,
                            ),
                        ]
                    ),
                ],
                scroll=ft.ScrollMode.HIDDEN,
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
