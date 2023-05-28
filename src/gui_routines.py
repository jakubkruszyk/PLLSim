def handle_events(app, event, values, pll):
    if event == "-ref_osc_value-":
        pll.ref_osc.freq = values[event]

    elif event == "-loc_osc_value-":
        pll.dco.freq = values[event]
