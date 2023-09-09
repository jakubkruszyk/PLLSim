import dearpygui.dearpygui as dpg


def pll_update(pll, data, time):
    new_data = pll.run()
    # tags = ("input_series", "local_series", "lead_series", "lag_series")
    tags = ("input_series", "local_series")
    time.pop(0)
    time.append(time[-1]+1)
    for old, new, tag in zip(data, new_data, tags):
        old.pop(0)
        old.append(new)
        dpg.set_value(tag, [time, old])
    dpg.set_axis_limits("input_x_axis", time[-1]-200, time[-1])
    dpg.set_axis_limits("local_x_axis", time[-1] - 200, time[-1])
