import PySimpleGUI as sg
from src.layout import new_layout
from src.plots import Plots

# create app and plots
app = sg.Window("PLLSim", new_layout(), finalize=True)
plots_canvas = app['-plots_canvas-'].TKCanvas
plots = Plots(plots_canvas)

# demo counter
i = 0
a = [1, 1]

while True:
    event, values = app.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break

    # demo draw
    plots.draw(a)
    i += 1
    if 40 > i > 20:
        a = [0, 0]
    elif i > 40:
        i = 0
        a = [1, 1]
