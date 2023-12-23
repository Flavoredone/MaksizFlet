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
                        title=ft.Text(f"{e.control.name}", font_family="Teko"),
                        bgcolor="#333333",
                    ),
                    e.control.view,
                ],
            )
        )
        e.control.page.update()


def main(page: ft.Page):

    if str(page.route) == '/privacy_policy':
        page.add(
            ft.Row(
                controls=[
                    ft.Text("""
                                   Политика Конфиденциальности: 

                                   Контактный email: info@maksiz.ru

                                   Дата вступления в силу: 23 декабря 2023 года.
                                   
                                   Приложение «MAKSIZ» является оффлайн-приложением и не 
                                   собирает, не хранит и не передает персональные данные 
                                   пользователя. 
                                   
                                   Приложение не требует доступа к интернету 
                                   или другим функциям устройства пользователя для своей 
                                   работы, кроме функций, необходимых для основного 
                                   функционала (например, просмотр текстов песен). 
                                   
                                   Пользователи могут использовать приложение для просмотра 
                                   текстов песен, без необходимости предоставлять какую-либо 
                                   персональную информацию. 
                                   
                                   В случае вопросов или предложений, связанных с работой
                                   приложения или политикой конфиденциальности, пожалуйста,
                                   свяжитесь с нами по адресу: info@maksiz.ru
                                   """,
                            height=int(page.height),
                            selectable=True)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        )

    else:
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
        # color_scheme_seed='#F74F10',
        color_scheme=ft.ColorScheme(
            # primary='#F74F10',
            primary='#FFFFFF',
            primary_container='#F74F10',
        ),
        font_family="Teko"
    )

    def route_change(e: ft.RouteChangeEvent):
        print(e.route)
        if str(e.route) == "/privacy_policy":
            page.clean()
            page.add(
                ft.Row(
                    controls=[
                        ft.Text("""
                                       Политика Конфиденциальности: 
    
                                       Контактный email: info@maksiz.ru
    
                                       Дата вступления в силу: 23 декабря 2023 года.
    
                                       Приложение «MAKSIZ» является оффлайн-приложением и не 
                                       собирает, не хранит и не передает персональные данные 
                                       пользователя. 
    
                                       Приложение не требует доступа к интернету 
                                       или другим функциям устройства пользователя для своей 
                                       работы, кроме функций, необходимых для основного 
                                       функционала (например, просмотр текстов песен). 
    
                                       Пользователи могут использовать приложение для просмотра 
                                       текстов песен, без необходимости предоставлять какую-либо 
                                       персональную информацию. 
    
                                       В случае вопросов или предложений, связанных с работой
                                       приложения или политикой конфиденциальности, пожалуйста,
                                       свяжитесь с нами по адресу: info@maksiz.ru
                                       """,
                                height=int(page.height),
                                selectable=True)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            )
        else:
            pass

    page.on_route_change = route_change
    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)  # , view=ft.WEB_BROWSER
