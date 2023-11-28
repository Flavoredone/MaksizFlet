import res

import flet as ft

from results import imgres, value


def example(page):

    def res_click(e):
        if (rg1.value is None) and (rg2.value is None) and (rg3.value is None) and (rg4.value is None):
            pass
        else:
            if rg4.value == "1":
                imgres.append("1")
                imgres.append("2")
            else:
                if rg3.value == "2":
                    imgres.append("6")
                else:
                    if rg3.value == "1":
                        imgres.append("5")
                        imgres.append("7")
                    else:
                        if rg2.value == "2":
                            imgres.append("1")
                            imgres.append("2")
                            imgres.append("6")
                        else:
                            imgres.append("1")
                            imgres.append("2")
                            imgres.append("6")
                            imgres.append("5")
                            imgres.append("7")

        value.append("анкеты")

        page.views.append(
            ft.View(
                bgcolor="#333333",
                controls=[
                    ft.AppBar(bgcolor="#333333", title=ft.Text("РЕЗУЛЬТАТ ПОИСКА", color=f"#FFFFFF")),
                    res.example(page),
                ],
            )
        )
        page.update()

    res_btn = ft.ElevatedButton(
        text="ПЕРЕЙТИ К РЕЗУЛЬТАТУ",
        on_click=res_click,
        bgcolor="#F74F10",
        height=50,
        color="#FFFFFF"
    )

    rg1 = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="1", label="твердое вещество", fill_color=f"#FFFFFF"),
        ft.Radio(value="2", label="жидкость, в том числе аэрозоли", fill_color=f"#FFFFFF"),
        ft.Radio(value="3", label="газ", fill_color=f"#FFFFFF")]))

    rg2 = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="1", label="имеется", fill_color=f"#FFFFFF"),
        ft.Radio(value="2", label="не имеется", fill_color=f"#FFFFFF")]))

    rg3 = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="1", label="умеренный", fill_color=f"#FFFFFF"),
        ft.Radio(value="2", label="тяжелый", fill_color=f"#FFFFFF")]))

    rg4 = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="1", label="да", fill_color=f"#FFFFFF"),
        ft.Radio(value="2", label="нет", fill_color=f"#FFFFFF")]))

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Row(
                [
                    res_btn,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text(height=50),
            ft.Row([
                ft.Column([
                    ft.Text("Каково физическое состояние вашей опасности в момент ее возникновения?", color="#FFFFFF"),
                    rg1,
                    ft.Text(height=10),
                    ft.Text("Наличие или опасность взаимодействия с открытым пламенем:", color="#FFFFFF"),
                    rg2,
                    ft.Text(height=10),
                    ft.Text("Контактный уровень взаимодействия с одеждой:", color="#FFFFFF"),
                    rg3,
                    ft.Text(height=10),
                    ft.Text("Нужна ли дополнительная защита шва путем проклейки?", color="#FFFFFF"),
                    rg4,
                    ft.Text(height=500),
                ],
                    scroll=ft.ScrollMode.HIDDEN,
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
                # scroll=ft.ScrollMode.HIDDEN,
                alignment=ft.MainAxisAlignment.CENTER,
            )
        ],
        scroll=ft.ScrollMode.HIDDEN,
    )


def main(page: ft.Page):
    page.title = "ПОИСК ПО ВЕЩЕСТВУ"
    page.bgcolor = "#333333"
    page.add(example(page))


if __name__ == "__main__":
    ft.app(target=main)
