import PySimpleGUI as sg
from src.layout import new_layout
from src.plots import Plots

# create app and plots
app = sg.Window("PLLSim", new_layout(), finalize=True)
plots_canvas = app['-plots_canvas-'].TKCanvas
plots = Plots(plots_canvas)

while True:
    event, values = app.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break
