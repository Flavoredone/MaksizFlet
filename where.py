import flet as ft


def example(page):

    def show_view(e):
        cur = e.control.text[17:]
        if str(page.platform) == "macos" or "linux" or "windows":
            page.launch_url(cur)
        else:
            page.views.append(
                ft.AppBar(bgcolor="#333333", title=ft.Text("САЙТ ПАРТНЕРА", color=f"#FFFFFF")),
                ft.WebView(
                    cur,
                    bgcolor="#333333",
                )
            )
            page.update()

    def copy(e):
        e.page.set_clipboard(e.control.text)
        e.page.add(ft.SnackBar(ft.Text(f"Скопировано: {e.control.text[17:]}"), open=True))

    st1 = ft.Column(
        [
            ft.Image(
                src=f"where/1.png",
                width=350,
                height=int(int(page.height) / 7.7),
            ),
            ft.TextButton("     Компания:   АО «ФПГ ЭНЕРГОКОНТРАКТ»", on_click=copy),
            ft.TextButton("     Телефон:    +7 (495) 645-00-11", on_click=copy),
            ft.TextButton("     Почта:      fpg@energocontract.ru", on_click=copy),
            ft.TextButton("     Сайт:       https://energocontract.ru/", on_click=show_view),
        ],
    )

    st2 = ft.Column(
        [
            ft.Image(
                width=350,
                src=f"where/2.png",
                height=int(int(page.height) / 7.7),
            ),
            ft.TextButton("     Компания:   «Техноавиа»", on_click=copy),
            ft.TextButton("     Телефон:    +7 (495) 787-90-30", on_click=copy),
            ft.TextButton("     Почта:      zakaz@technoavia.ru", on_click=copy),
            ft.TextButton("     Сайт:       https://www.technoavia.ru/", on_click=show_view),
        ],
    )

    st3 = ft.Column(
        [
            ft.Image(
                width=350,
                src=f"where/3.png",
                height=int(int(page.height) / 7.7),
            ),
            ft.TextButton("     Компания:   «ВОСТОК-СЕРВИС»", on_click=copy),
            ft.TextButton("     Телефон:    +7 (495) 665-0-665", on_click=copy),
            ft.TextButton("     Почта:      magazin@vostok.ru", on_click=copy),
            ft.TextButton("     Сайт:       https://vostok.ru/", on_click=show_view),
        ],
    )

    return ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    st3,
                    st2,
                    st1
                ],
                scroll=ft.ScrollMode.HIDDEN,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
    )


def main(page: ft.Page):
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
