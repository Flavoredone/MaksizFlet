import res
import search3

import flet as ft

from data import *
from results import imgres, value


def example(page):

    def textbox_changed(string):
        str_lower = string.control.value.lower()

        list_view.controls = [
            list_items.get(n) for n in all_substance if str_lower in n.lower()
        ] if str_lower else []
        page.update()

    def printer(e):
        sub_res = e.control.text

        value.append(sub_res)

        if sub_res in set1_sub:
            imgres.append("5")

        if sub_res in set2_sub:
            imgres.append("1")
            imgres.append("2")
            imgres.append("6")

        if sub_res in set3_sub:
            imgres.append("7")

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
                controls=[ft.AppBar(bgcolor="#333333", title=ft.Text("ПОИСК ПО ДЕЯТЕЛЬНОСТИ")), search3.example(page)],
            )
        )
        page.update()

    list_items = {
        sub: ft.OutlinedButton(
            text=sub,
            on_click=printer,
        )
        for sub in all_substance
    }

    next_btn = ft.ElevatedButton(
        text="ВЕЩЕСТВО НЕИЗВЕСТНО",
        on_click=next_click,
        width=int(int(page.width) / 2.2),
        bgcolor="#F74F10",
        height=50,
        color="#FFFFFF"
    )
    res_btn = ft.ElevatedButton(
        text="ПЕРЕЙТИ К РЕЗУЛЬТАТУ",
        on_click=res_click,
        width=int(int(page.width) / 2.2),
        bgcolor="#F74F10",
        height=50,
        color="#FFFFFF"
    )

    list_view = ft.ListView(expand=1, spacing=10, padding=20)

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Row(
                [
                    next_btn,
                    res_btn,
                ],
                spacing=100,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text(height=10),
            ft.TextField(label="Введите вещество:", on_change=textbox_changed),
            list_view,

        ]
    )


def main(page: ft.Page):
    page.title = "ПОИСК ПО ВЕЩЕСТВУ"
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
