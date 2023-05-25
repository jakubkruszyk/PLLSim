import PySimpleGUI as sg


def new_layout() -> list[list]:
    return [[sg.Image("src/Block_diagram.png")],
            [sg.HorizontalSeparator()],
            control_layout_row(),
            [sg.HorizontalSeparator()],
            plots_layout_row()
            ]


def control_layout_row() -> list:
    filter_control = [[sg.Text("N"), sg.Slider(range=(5, 30), default_value=15,
                                               key="-n_counter_value-", orientation='h', enable_events=True)],
                      [sg.Text("M"), sg.Slider(range=(5, 30), default_value=15,
                                               key="-m_counter_value-", orientation='h', enable_events=True)]
                      ]

    osc_control = [[sg.Text("Reference:"), sg.Slider(range=(5, 30), default_value=15,
                                                     key="-ref_osc_value-", orientation='h', enable_events=True)],
                   [sg.Text("Local:"), sg.Push(), sg.Slider(range=(5, 30), default_value=15,
                                                            key="-loc_osc_value-", orientation='h', enable_events=True)]
                   ]
    return [sg.Frame("Oscillators settings", osc_control), sg.Frame("Filter settings", filter_control)]


def plots_layout_row() -> list:
    return [sg.Canvas(key="-plots_canvas-", expand_x=True)]
