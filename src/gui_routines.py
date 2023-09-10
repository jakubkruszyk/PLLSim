import dearpygui.dearpygui as dpg
from src.globals import DATA_POINTS_NUM


def pll_update(pll, data, time):
    new_data = pll.run()
    tags = ("input", "local", "lead", "lag", "delta")
    time.pop(0)
    time.append(time[-1]+1)
    for old, new, tag in zip(data, new_data, tags):
        old.pop(0)
        old.append(new)
        dpg.set_value(f"{tag}_series", [time, old])
        dpg.set_axis_limits(f"{tag}_x_axis", time[-1]-DATA_POINTS_NUM, time[-1])
    dpg.set_value("lead_indicator", f"Lead counter: {pll.filter.lead}")
    dpg.set_value("lag_indicator", f"Lag counter: {pll.filter.lag}")


def toggle_sim_run(sender, app_data):
    running = dpg.get_item_user_data(sender)
    if running:
        dpg.set_item_label(sender, "Stopped")
    else:
        dpg.set_item_label(sender, "Running")
    dpg.set_item_user_data(sender, not running)


def reset_callback(sender, app_data):
    time, data, pll = dpg.get_item_user_data(sender)
    data[:] = [[0 for _ in range(DATA_POINTS_NUM)] for _ in range(5)]
    time[:] = [i for i in range(-DATA_POINTS_NUM, 0)]
    pll.input_osc.reset()
    pll.local_osc.reset()
    pll.local_osc.tics = dpg.get_value("slider_phase")  # restore phase shift
    pll.filter.reset()
    tags = ("input", "local", "lead", "lag", "delta")
    for x, tag in zip(data, tags):
        dpg.set_value(f"{tag}_series", [time, x])
        dpg.set_axis_limits(f"{tag}_x_axis", time[-1] - DATA_POINTS_NUM, time[-1])


def update_freq_callback(sender, app_data):
    pll = dpg.get_item_user_data(sender)
    if sender == "slider_input_gen":
        pll.input_osc.period = app_data
    else:
        pll.local_osc.period = app_data


def update_counters_callback(sender, app_data):
    pll = dpg.get_item_user_data(sender)
    if sender == "slider_sum_gen":
        pll.filter.sum_cnt_max = app_data
    else:
        pll.filter.lead_lag_cnt_max = app_data


def update_step(sender, app_data):
    pll = dpg.get_item_user_data(sender)
    pll.step = app_data


def update_speed(sender, app_data):
    dpg.set_item_user_data(sender, True)


def update_phase(sender, app_data):
    pll, last = dpg.get_item_user_data(sender)
    pll.local_osc.tics += (app_data - last)
    dpg.set_item_user_data(sender, [pll, app_data])

