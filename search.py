import res
import search2

import flet as ft

from data import *
from results import imgres, value


def example(page):

    def textbox_changed(string):
        str_lower = string.control.value.lower()

        list_view.controls = [
            list_items.get(n) for n in all_cas if str_lower in n.lower()
        ] if str_lower else []
        page.update()

    def printer(e):
        cas_res = e.control.text

        value.append(cas_res)

        if cas_res in set1_cas:
            imgres.append("5")

        if cas_res in set2_cas:
            imgres.append("1")
            imgres.append("2")
            imgres.append("6")

        if cas_res in set3_cas:
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
                controls=[ft.AppBar(bgcolor="#333333", title=ft.Text("ПОИСК ПО ВЕЩЕСТВУ")), search2.example(page)],
            )
        )
        page.update()

    list_items = {
        cas: ft.OutlinedButton(
            text=cas,
            on_click=printer,
        )
        for cas in all_cas
    }

    next_btn = ft.ElevatedButton(
        text="НОМЕР НЕИЗВЕСТЕН",
        on_click=next_click,
        width=int(int(page.width) / 4.2),
        bgcolor="#F74F10",
        height=50,
        color="#FFFFFF"
    )
    res_btn = ft.ElevatedButton(
        text="ПЕРЕЙТИ К РЕЗУЛЬТАТУ",
        on_click=res_click,
        width=int(int(page.width) / 4.2),
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
            ft.TextField(label="Введите CAS номер:",
                         on_change=textbox_changed,
                         color="#FFFFFF",
                         bgcolor="#333333"
                         ),
            list_view,

        ]
    )


def main(page: ft.Page):
    page.title = "ПОИСК ПО CAS НОМЕРУ"
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
