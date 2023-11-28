import flet as ft
import combview
from results import cat


def example(page):

    def comb_view1(e):
        cat.append(1)
        comb_view(e)

    def comb_view2(e):
        cat.append(2)
        comb_view(e)

    def comb_view3(e):
        cat.append(3)
        comb_view(e)

    def comb_view4(e):
        cat.append(4)
        comb_view(e)

    def comb_view5(e):
        cat.append(5)
        comb_view(e)

    def comb_view6(e):
        cat.append(6)
        comb_view(e)

    def comb_view7(e):
        cat.append(7)
        comb_view(e)

    def comb_view(e):
        page.views.append(
            ft.View(
                bgcolor="#333333",
                controls=[
                    ft.AppBar(bgcolor="#333333", title=ft.Text("КОМБИНЕЗОНЫ", color=f"#FFFFFF")),
                    combview.example(page),
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
                        height=int(int(page.height) / 5.5),
                        spacing=70,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="comb/1.png"),
                                on_click=comb_view1,
                            ),
                            ft.Container(
                                content=ft.Image(src="comb/2.png"),
                                on_click=comb_view2,
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=int(int(page.height) / 5.5),
                        spacing=70,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="comb/3.png"),
                                on_click=comb_view3,
                            ),
                            ft.Container(
                                content=ft.Image(src="comb/4.png"),
                                on_click=comb_view4,
                            )
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        height=int(int(page.height) / 5.5),
                        spacing=70,
                        controls=[
                            ft.Container(
                                content=ft.Image(src="comb/5.png"),
                                on_click=comb_view5,
                            ),
                            ft.Container(
                                content=ft.Image(src="comb/6.png"),
                                on_click=comb_view6,
                            )
                        ]
                    ),
                    ft.Container(
                        height=int(int(page.height) / 5.5),
                        content=ft.Image(src="comb/7.png"),
                        on_click=comb_view7,
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                scroll=ft.ScrollMode.ALWAYS,
            )
        ],
    )


def main(page: ft.Page):
    page.title = "О КОМПАНИИ"
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
