import PySimpleGUI as sg
from src.layout import new_layout
from src.plots import create_plots, draw_figure

# create app and plots
app = sg.Window("PLLSim", new_layout(), finalize=True)
fig, (input_osc_ax, output_signal) = create_plots()
plots_canvas = app['-plots_canvas-'].TKCanvas
fig_agg = draw_figure(plots_canvas, fig)
fig_agg.draw()

while True:
    event, values = app.read(timeout=100)
    if event == sg.WIN_CLOSED:
        break
