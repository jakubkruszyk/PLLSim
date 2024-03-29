import dearpygui.dearpygui as dpg
from src.globals import DATA_POINTS_NUM, PRESETS


def pll_update(pll, data, time):
    new_data = pll.run()
    tags = ("input", "local", "lead", "lag", "delta", "phase_input", "phase_local")
    time.pop(0)
    time.append(time[-1]+1)
    for old, new, tag in zip(data, new_data, tags):
        old.pop(0)
        old.append(new)
        dpg.set_value(f"{tag}_series", [time, old])
    for tag in tags[0:5]:
        dpg.set_axis_limits(f"{tag}_x_axis", time[-1]-DATA_POINTS_NUM, time[-1])
    dpg.set_axis_limits("phase_x_axis", time[-1] - DATA_POINTS_NUM, time[-1])
    dpg.set_axis_limits("phase_y_axis", min(data[5][0], data[6][0]), max(data[5][-1], data[6][-1]))

    dpg.set_value("lead_indicator", f"Lead counter: {pll.filter.lead}")
    dpg.set_value("lag_indicator", f"Lag counter: {pll.filter.lag}")
    dpg.set_value("sum_indicator", f"Sum counter: {pll.filter.lag + pll.filter.lead}")


def toggle_sim_run(sender, app_data):
    running = dpg.get_item_user_data(sender)
    if running:
        dpg.set_item_label(sender, "Stopped")
    else:
        dpg.set_item_label(sender, "Running")
    dpg.set_item_user_data(sender, not running)


def reset_callback(sender, app_data):
    time, data, pll = dpg.get_item_user_data(sender)
    data[:] = [[0 for _ in range(DATA_POINTS_NUM)] for _ in range(7)]
    time[:] = [i for i in range(-DATA_POINTS_NUM, 0)]
    pll.reset()
    pll.local_osc.tics = dpg.get_value("slider_phase")  # restore phase shift
    tags = ("input", "local", "lead", "lag", "delta")
    for x, tag in zip(data, tags):
        dpg.set_value(f"{tag}_series", [time, x])
        dpg.set_axis_limits(f"{tag}_x_axis", time[-1] - DATA_POINTS_NUM, time[-1])
    dpg.set_value("phase_input_series", [time, data[5]])
    dpg.set_value("phase_local_series", [time, data[6]])
    dpg.set_axis_limits("phase_x_axis", time[-1] - DATA_POINTS_NUM, time[-1])


def update_freq_callback(sender, app_data):
    pll = dpg.get_item_user_data(sender)
    if sender == "slider_input_gen":
        pll.input_osc.period = app_data
    else:
        pll.local_osc.period = app_data


def update_counters_callback(sender, app_data):
    pll = dpg.get_item_user_data(sender)
    if sender == "slider_sum_counter":
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


def set_preset(sender, app_data):
    preset = PRESETS[app_data]
    # Update PLL
    pll = dpg.get_item_user_data(sender)
    pll.set_preset(preset)
    update_phase("slider_phase", dpg.get_value("slider_phase"))
    # Update gui
    dpg.set_value("slider_step", preset["step"])
    dpg.set_value("slider_phase", preset["phase"])
    dpg.set_value("slider_lead_lag_counter", preset["lag_counter"])
    dpg.set_value("slider_sum_counter", preset["sum_counter"])
    dpg.set_value("slider_input_gen", preset["input_period"])
    dpg.set_value("slider_local_gen", preset["local_period"])
