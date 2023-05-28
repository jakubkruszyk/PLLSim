import PySimpleGUI as sg
from src.layout import new_layout
from src.plots import Plots
from src.gui_routines import handle_events
from src.pll import PLL
from src.ocs import OSC
# create app and plots
app = sg.Window("PLLSim", new_layout(), finalize=True)
plots_canvas = app['-plots_canvas-'].TKCanvas
plots = Plots(plots_canvas)

# demo counter
pll = PLL()

while True:
    event, values = app.read(timeout=200)
    if event == sg.WIN_CLOSED:
        break

    if event != sg.TIMEOUT_EVENT:
        handle_events(app, event, values, pll)

    # demo draw
    plots.draw(pll.run())
