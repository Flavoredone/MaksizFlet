import flet as ft

import comb
import gloves
import other


class CatalogueObj(ft.Container):
    def __init__(self, name, view, file_name, content):
        super().__init__()
        self.view = view
        self.content = content
        self.title = ft.Text(name)
        self.on_click = self.app_button_clicked
        self.name = name
        self.file_name = file_name
        self.alignment = ft.alignment.center

    @staticmethod
    def app_button_clicked(e):
        e.control.page.views.append(
            ft.View(
                bgcolor="#333333",
                controls=[
                    ft.AppBar(
                        title=ft.Text(f"{e.control.name}"),
                        bgcolor="#333333",
                    ),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def example(page):
    return ft.Column(
        tight=True,
        scroll=ft.ScrollMode.AUTO,
        controls=[
            CatalogueObj(
                name="КОБИНЕЗОНЫ",
                file_name="comb.py",
                view=comb.example(page),
                content=ft.Image(src="assets/с1.png",
                                 height=int(int(page.height) / 3.5),
                                 fit=ft.ImageFit.FIT_HEIGHT
                                 ),
            ),
            CatalogueObj(
                name="ПЕРЧАТКИ",
                file_name="gloves.py",
                view=gloves.example(page),
                content=ft.Image(src="assets/с2.png",
                                 height=int(int(page.height) / 3.5),
                                 fit=ft.ImageFit.FIT_HEIGHT
                                 ),
            ),
            CatalogueObj(
                name="ПРОЧЕЕ",
                file_name="other.py",
                view=other.example(page),
                content=ft.Image(src="assets/с3.png",
                                 height=int(int(page.height) / 3.5),
                                 fit=ft.ImageFit.FIT_HEIGHT
                                 ),
            )
        ],
    )


def main(page: ft.Page):
    page.title = "О КОМПАНИИ"
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
