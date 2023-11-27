import flet as ft
import glview
from results import gl

def example(page):

    def view1(e):
        gl.append(1)
        view(e)

    def view2(e):
        gl.append(2)
        view(e)

    def view3(e):
        gl.append(3)
        view(e)

    def view(e):
        page.views.append(
            ft.View(
                bgcolor="#333333",
                controls=[
                    ft.AppBar(bgcolor="#333333", title=ft.Text("ПЕРЧАТКИ")),
                    glview.example(page),
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
                    ft.FilledButton(
                        on_click=view1,
                        width=int(int(page.width) / 1.5),
                        text="HOUSEHOLD GLOVES"
                    ),
                    ft.FilledButton(
                        on_click=view2,
                        width=int(int(page.width) / 1.5),
                        text="PHYSICAL PROTECTIVE GLOVES"
                    ),
                    ft.FilledButton(
                        on_click=view3,
                        width=int(int(page.width) / 1.5),
                        text="REAGENT PROTECTIVE GLOVES"
                    )
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