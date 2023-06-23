import PySimpleGUI as sg
from src.globals import *


def new_layout() -> list[list]:
    return [[sg.Column(control_layout_row(), element_justification="center"), sg.VerticalSeparator(),
             sg.Column(plots_canvas(), element_justification="center")]]


def control_layout_row() -> list:
    start_button = sg.Button("Stopped", key="-start_btn-", button_color=STOP_BUTTON_COLOR, metadata=False,
                             size=(10, 2))

    filter_control = [[sg.Text("Lead/Lag"), sg.Slider(range=(5, 30), default_value=10, key="-lead_lag_counter_value-",
                                                      orientation='h', enable_events=True)],
                      [sg.Text("Sum"), sg.Push(), sg.Slider(range=(5, 30), default_value=19, key="-sum_counter_value-",
                                                            orientation='h', enable_events=True)]
                      ]

    osc_control = [[sg.Text("Reference:"), sg.Slider(range=(5, 30), default_value=15,
                                                     key="-ref_osc_value-", orientation='h', enable_events=True)],
                   [sg.Text("Local:"), sg.Push(), sg.Slider(range=(5, 30), default_value=15,
                                                            key="-loc_osc_value-", orientation='h', enable_events=True)]
                   ]
    return [[sg.Image("src/Block_diagram.png")],
            [sg.HorizontalSeparator()],
            [start_button],
            [sg.Frame("Oscillators settings", osc_control), sg.Frame("Filter settings", filter_control)]]


def plots_canvas():
    return [[sg.Canvas(key="-plots_canvas-", expand_x=True)],
            [sg.Text("Lead counter:", font=("Arial", 12)), sg.Text("0", key="-lead_display-", font=("Arial", 12)),
             sg.Text("Lag counter:", font=("Arial", 12)), sg.Text("0", key="-lag_display-", font=("Arial", 12))]]

