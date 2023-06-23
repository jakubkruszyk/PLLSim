from src.globals import *


def handle_events(app, event, values, pll):
    if event == "-ref_osc_value-":
        pll.ref_osc.freq = values[event]

    elif event == "-loc_osc_value-":
        pll.dco.freq = values[event]

    elif event == "-lead_lag_counter_value":
        pll.filter.lead_lag_cnt_max = values[event]

    elif event == "-sum_counter_value-":
        pll.filter.lead_lag_cnt_max = values[event]

    elif event == "-start_btn-":
        if app[event].metadata:
            app[event].metadata = False
            app[event].update(text="Stop", button_color=STOP_BUTTON_COLOR)
        else:
            app[event].metadata = True
            app[event].update(text="Start", button_color=START_BUTTON_COLOR)

