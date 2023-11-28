import res
import search4

import flet as ft

from data import *
from results import imgres, value


def example(page):

    def printer(e):
        sub_res = e.control.text

        value.append(sub_res)

        varbs = [l701, l702, l703, l705, l706, l707]
        for var in varbs:
            if sub_res in var:
                imgres.append(var[0])

    def res_click(e):
        page.views.append(
            ft.View(
                bgcolor="#333333",
                controls=[
                    ft.AppBar(bgcolor="#333333", title=ft.Text("РЕЗУЛЬТАТ ПОИСКА")),
                    res.example(page),
                ],
            )
        )
        page.update()

    def next_click(e):
        page.views.append(
            ft.View(
                bgcolor="#333333",
                controls=[ft.AppBar(bgcolor="#333333", title=ft.Text("АНКЕТА")), search4.example(page)],
            )
        )
        page.update()

    list_items = {
        sub: ft.OutlinedButton(
            text=sub,
            on_click=printer,
        )
        for sub in ddn_otrasl
    }

    next_btn = ft.ElevatedButton(
        text="ДЕЯТЕЛЬНОСТЬ НЕИЗВЕСТНА",
        on_click=next_click,
        # width=int(int(page.width) / 2.2),
        bgcolor="#F74F10",
        height=50,
        color="#FFFFFF"
    )
    res_btn = ft.ElevatedButton(
        text="ПЕРЕЙТИ К РЕЗУЛЬТАТУ",
        on_click=res_click,
        # width=int(int(page.width) / 2.2),
        bgcolor="#F74F10",
        height=50,
        color="#FFFFFF"
    )

    list_view = ft.ListView(expand=1, spacing=10, padding=20)
    list_view.controls = [list_items.get(n) for n in ddn_otrasl]

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Row(
                [
                    next_btn,
                    res_btn,
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text(height=10),
            # ft.TextField(label="Введите вещество:"),
            list_view,

        ]
    )


def main(page: ft.Page):
    page.title = "ПОИСК ПО ВЕЩЕСТВУ"
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
