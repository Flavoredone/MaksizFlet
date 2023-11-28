from flet_core import Theme

import where
import catalogue
import company
import certif
import search

import flet as ft


class AppTile(ft.Container):
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
                        title=ft.Text(f"{e.control.name}", font_family="Teko", color=f"#FFFFFF"),
                        bgcolor="#333333",
                    ),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):
    page.add(
        ft.Column(
            tight=True,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Text(height=1),
                AppTile(
                    name="О КОМПАНИИ",
                    file_name="company.py",
                    view=company.example(page),
                    content=ft.Image(src="1.png",
                                     # width=250,
                                     height=int(int(page.height) / 5.5),
                                     fit=ft.ImageFit.FIT_HEIGHT
                                     ),
                ),
                AppTile(
                    name="ПОИСК ПО НОМЕРУ CAS",
                    file_name="search.py",
                    view=search.example(page),
                    content=ft.Image(src="2.png",
                                     # width=250,
                                     height=int(int(page.height) / 5.5),
                                     fit=ft.ImageFit.FIT_HEIGHT
                                     ),
                ),
                AppTile(
                    name="КАТАЛОГ",
                    file_name="catalogue.py",
                    view=catalogue.example(page),
                    content=ft.Image(src="3.png",
                                     # width=250,
                                     height=int(int(page.height) / 5.5),
                                     fit=ft.ImageFit.FIT_HEIGHT
                                     ),
                ),
                AppTile(
                    name="ДОКУМЕНТАЦИЯ",
                    file_name="certif.py",
                    view=certif.example(page),
                    content=ft.Image(src="4.png",
                                     # width=250,
                                     height=int(int(page.height) / 5.5),
                                     fit=ft.ImageFit.FIT_HEIGHT
                                     ),
                ),
                AppTile(
                    name="ГДЕ КУПИТЬ",
                    file_name="where.py",
                    view=where.example(page),
                    content=ft.Image(src="5.png",
                                     # width=250,
                                     height=int(int(page.height) / 5.5),
                                     fit=ft.ImageFit.FIT_HEIGHT
                                     ),
                ),
            ],
        )
    )

    def view_pop(view):
        page.views.pop()
        top_view = page.views[0]
        page.go(top_view.route)

    page.on_view_pop = view_pop
    page.bgcolor = "#333333"

    page.fonts = {
        "Teko": "/fonts/Teko-Regular.ttf"
    }

    page.theme = Theme(
        color_scheme_seed='#FFFFFF',
        color_scheme=ft.ColorScheme(
            primary='#FFFFFF',
            tertiary='#FFFFFF',
            secondary='#FFFFFF',
        ),
        font_family="Teko"
    )

    page.update()


ft.app(target=main, view=ft.WEB_BROWSER) #, view=ft.WEB_BROWSER
