import dearpygui.dearpygui as dpg
from src.globals import DATA_POINTS_NUM


def create_controls(time, data):
    with dpg.window(label="Controls", width=300, height=300):
        with dpg.group(horizontal=True):
            dpg.add_spacer(width=75)
            dpg.add_button(label="Stopped", tag="btn_start", height=40, width=100)
        dpg.add_slider_int(label="Speed", tag="slider_tempo", width=150,
                           min_value=10, max_value=30, default_value=20)

        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_text("Counters filter settings")
        dpg.add_slider_int(label="Lead/Lag counter", tag="slider_lead_lag_counter", width=150,
                           min_value=10, max_value=30, default_value=20)
        dpg.add_slider_int(label="Sum counter", tag="slider_sum_counter", width=150,
                           min_value=10, max_value=30, default_value=20)

        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_text("Generators settings")
        dpg.add_slider_int(label="Input", tag="slider_input_gen", width=150,
                           min_value=10, max_value=30, default_value=20)
        dpg.add_slider_int(label="Local", tag="slider_local_gen", width=150,
                           min_value=10, max_value=30, default_value=20)

    with dpg.window(label="Plots", width=550, height=350, pos=(300, 0)):
        with dpg.plot(label="Input oscillator", height=120, width=500):
            dpg.add_plot_axis(dpg.mvXAxis, tag="input_x_axis", no_tick_marks=True, no_tick_labels=True)
            dpg.add_plot_axis(dpg.mvYAxis, tag="input_y_axis", no_tick_marks=True, no_tick_labels=True)
            dpg.set_axis_limits("input_y_axis", -0.1, 1.1)
            dpg.set_axis_limits("input_x_axis", 0, DATA_POINTS_NUM)
            dpg.add_line_series(time, data[0], parent="input_y_axis", tag="input_series")

        with dpg.plot(label="Local oscillator", height=150, width=500):
            dpg.add_plot_axis(dpg.mvXAxis, tag="local_x_axis", label="Time")
            dpg.add_plot_axis(dpg.mvYAxis, tag="local_y_axis", no_tick_marks=True, no_tick_labels=True)
            dpg.set_axis_limits("local_y_axis", -0.1, 1.1)
            dpg.set_axis_limits("local_x_axis", 0, DATA_POINTS_NUM)
            dpg.add_line_series(time, data[1], parent="local_y_axis", tag="local_series")
