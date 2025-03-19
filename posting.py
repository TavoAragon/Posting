

import flet as ft

def main(page: ft.Page):
    page.title = "Tablero de Notas Adhesivas"
    page.padding = 20
    page.theme_mode = "light"
    page.bgcolor = ft.colors.LIGHT_BLUE_800

    def add_note(e):
        new_note = create_note("Nueva Nota")
        grid.controls.append(new_note)
        page.update()

    def delete_note(note):
        grid.controls.remove(note)
        page.update()

    def create_note(text):
        note_content = ft.TextField(
            value=text,
            multiline=True,
            bgcolor=ft.colors.BLUE_GREY_50,
        )
        note = ft.Container(
            content=ft.Column(
                [
                    note_content,
                    ft.IconButton(
                        icon=ft.icons.DELETE, on_click=lambda _: delete_note(note)
                    ),
                ]
            ),
            width=200,
            height=200,
            bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=10,
            padding=10,
        )
        return note

    grid = ft.GridView(   #Cuadricula
        expand=True,
        max_extent=220,
        child_aspect_ratio=1,
        run_spacing=10,
        spacing=10,
    )

    drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(height=12),
            ft.NavigationDrawerDestination(
                label="Doctor",
                icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                selected_icon=ft.Icon(ft.Icons.DOOR_BACK_DOOR),
            ),
            ft.Divider(thickness=2),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.PERM_CONTACT_CALENDAR_OUTLINED),
                label="Pacientes",
                selected_icon=ft.Icons.PERM_CONTACT_CALENDAR,
            ),
            ft.NavigationDrawerDestination(
                icon=ft.Icon(ft.Icons.CALENDAR_MONTH_OUTLINED),
                label="Calendario",
                selected_icon=ft.Icons.CALENDAR_MONTH,
            ),
        ],
    )

    notes = [
        "Paciente: Alberto cita a las 10 am",
        "Paciente: Jesus Corona cita a las 12 pm",
        "Paciente: Daniel Ochoa cita a las 3 pm",
    ]

    for note in notes:
        grid.controls.append(create_note(note))

    # Modificar la fila para incluir ambos botones
    page.add(
        ft.Row(
            [
                ft.Text(
                    "Mis notas Adhesivas (Consultorio Dental)",
                    size=24,
                    weight="bold",
                    color=ft.colors.WHITE,
                ),
                ft.IconButton(
                    icon=ft.icons.ADD,
                    on_click=add_note,
                    icon_color=ft.colors.WHITE,
                ),
                ft.ElevatedButton(
                    "Desplegar Menú", on_click=lambda e: page.open(drawer)
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
        ),
        grid,
    )


ft.app(target=main)
