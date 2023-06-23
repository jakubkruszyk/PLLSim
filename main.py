import PySimpleGUI as sg
from src.layout import new_layout
from src.plots import Plots
from src.gui_routines import handle_events
from src.pll import PLL
from random import randint

# create app and plots
app = sg.Window("PLLSim", new_layout(), finalize=True)
plots_canvas = app['-plots_canvas-'].TKCanvas
plots = Plots(plots_canvas)

# Default parameters
ref_freq = app['-ref_osc_value-'].DefaultValue
dco_freq = app['-loc_osc_value-'].DefaultValue
lead_lag_cnt_max = app['-lead_lag_counter_value-'].DefaultValue
sum_cnt_max = app['-sum_counter_value-'].DefaultValue

# PLL structure
pll = PLL(ref_freq, dco_freq, lead_lag_cnt_max, sum_cnt_max)

# Random DCO starting phase
phase = randint(-5, 5)
print(phase)
pll.dco.tics = phase

while True:
    event, values = app.read(timeout=50)
    if event == sg.WIN_CLOSED:
        break

    if event != sg.TIMEOUT_EVENT:
        handle_events(app, event, values, pll)

    if app["-start_btn-"].metadata:
        plots.draw(pll.run())
        app["-lead_display-"].update(pll.filter.lead_cnt)
        app["-lag_display-"].update(pll.filter.lag_cnt)
        app["-loc_osc_value-"].update(value=pll.dco.freq)
