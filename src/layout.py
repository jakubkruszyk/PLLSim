import PySimpleGUI as sg


def new_layout() -> list[list]:
    return [[sg.Image("src/Block_diagram.png")],
            [sg.HorizontalSeparator()],
            control_layout_row(),
            [sg.HorizontalSeparator()],
            plots_layout_row()
            ]


def control_layout_row() -> list:
    filter_control = [[sg.Text("N"), sg.Input("10", key="-N_counter_set-", size=6)],
                      [sg.Text("M"), sg.Input("10", key="-M_counter_set-", size=6)]
                      ]
    return [sg.Frame("Filter settings", filter_control)]


def plots_layout_row() -> list:
    return [sg.Canvas(size=(640, 480), key="-plots_canvas-")]
