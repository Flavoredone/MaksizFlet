import flet as ft


def example(page):

    st1 = ft.Column(
        [
            ft.Image(
                src=f"assets/where/1.png",
                height=int(int(page.height) / 7.7),
            ),
            ft.Text("Компания: АО «ФПГ ЭНЕРГОКОНТРАКТ»"),
            ft.Text("Телефон:  +7 (495) 645-00-11"),
            ft.Text("Почта:    fpg@energocontract.ru"),
            ft.Text("Сайт:     https://energocontract.ru/"),
        ],
    )

    st2 = ft.Column(
        [
            ft.Image(
                src=f"assets/where/2.png",
                height=int(int(page.height) / 7.7),
            ),
            ft.Text("Компания: «Техноавиа»"),
            ft.Text("Телефон:  +7 (495) 787-90-30"),
            ft.Text("Почта:    zakaz@technoavia.ru"),
            ft.Text("Сайт:     https://www.technoavia.ru/"),
        ],
    )

    st3 = ft.Column(
        [
            ft.Image(
                src=f"assets/where/3.png",
                height=int(int(page.height) / 7.7),
            ),
            ft.Text("Компания: «ВОСТОК-СЕРВИС»"),
            ft.Text("Телефон:  +7 (495) 665-0-665"),
            ft.Text("Почта:    magazin@vostok.ru"),
            ft.Text("Сайт:     https://vostok.ru/"),
        ],
    )

    return ft.Row(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Column(
                [
                    st1,
                    st2,
                    st3
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
    )


def main(page: ft.Page):
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)