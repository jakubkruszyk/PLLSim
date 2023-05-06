import PySimpleGUI as sg
from src.layout import new_layout

app = sg.Window("PLLSim", new_layout())

while True:
    event, values = app.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break
