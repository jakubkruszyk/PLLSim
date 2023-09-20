from src.globals import *
from src.gui_routines import *


def create_layout(time, data, pll):
    with dpg.font_registry():
        default_font = dpg.add_font("src/LiberationMono-Regular.ttf", 16)
        counter_font = dpg.add_font("src/LiberationMono-Regular.ttf", 24)
    create_controls(time, data, pll)
    create_vertical_plots(time, data)
    dpg.bind_font(default_font)
    dpg.bind_item_font("lead_indicator", counter_font)
    dpg.bind_item_font("lag_indicator", counter_font)


def create_controls(time, data, pll):
    with dpg.window(label="Controls", width=300, height=800, no_close=True):
        with dpg.group(horizontal=True):
            dpg.add_button(label="Reset", tag="btn_reset", height=40, width=100,
                           callback=reset_callback, user_data=(time, data, pll))
            dpg.add_button(label="Stopped", tag="btn_start", height=40, width=100,
                           callback=toggle_sim_run, user_data=False)
        dpg.add_slider_int(label="Simulation speed", tag="slider_speed", width=150, callback=update_speed, user_data=False,
                           min_value=MIN_SPEED, max_value=MAX_SPEED, default_value=DEFAULT_SPEED)
        dpg.add_slider_int(label="Initial phase", tag="slider_phase", width=150, user_data=[pll, DEFAULT_PHASE],
                           min_value=MIN_PHASE, max_value=MAX_PHASE, default_value=DEFAULT_PHASE, callback=update_phase)
        dpg.add_slider_int(label="Correct step", tag="slider_step", width=150, user_data=pll, callback=update_step,
                           min_value=MIN_STEP, max_value=MAX_STEP, default_value=DEFAULT_STEP)
        dpg.add_combo(label="Presets", items=list(PRESETS.keys()), default_value="Lagging", width=150,
                      callback=set_preset, user_data=pll)

        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_text("Counters filter settings")
        dpg.add_slider_int(label="Lead/Lag counter", tag="slider_lead_lag_counter", width=150, user_data=pll,
                           callback=update_counters_callback, min_value=MIN_LAG_COUNTER, max_value=MAX_LAG_COUNTER,
                           default_value=DEFAULT_LAG_COUNTER)
        dpg.add_slider_int(label="Sum counter", tag="slider_sum_counter", width=150, callback=update_counters_callback,
                           min_value=MIN_SUM_COUNTER, max_value=MAX_SUM_COUNTER, default_value=DEFAULT_SUM_COUNTER,
                           user_data=pll)

        dpg.add_spacer(height=10)
        dpg.add_separator()
        dpg.add_text("Generators period settings")
        dpg.add_slider_int(label="Input osc", tag="slider_input_gen", width=150, callback=update_freq_callback,
                           min_value=MIN_INPUT_PERIOD, max_value=MAX_INPUT_PERIOD, default_value=DEFAULT_INPUT_PERIOD,
                           user_data=pll)
        dpg.add_slider_int(label="Local osc", tag="slider_local_gen", width=150, callback=update_freq_callback,
                           min_value=MIN_LOCAL_PERIOD, max_value=MAX_LOCAL_PERIOD, default_value=DEFAULT_LOCAL_PERIOD,
                           user_data=pll)


def create_vertical_plots(time, data):
    with dpg.window(label="Plots", width=1050, height=800, pos=(300, 0), no_close=True):
        with dpg.group(horizontal=True):
            with dpg.group():
                tags = ("input", "local", "lead", "lag")
                labels = ("Input oscillator", "Local oscillator", "Lead detection", "Lag detection")
                for tag, label in zip(tags, labels):
                    with dpg.plot(label=label, height=120, width=500, anti_aliased=True):
                        dpg.add_plot_axis(dpg.mvXAxis, tag=f"{tag}_x_axis", no_tick_marks=True, no_tick_labels=True)
                        dpg.add_plot_axis(dpg.mvYAxis, tag=f"{tag}_y_axis", no_tick_marks=True, no_tick_labels=True)
                        dpg.set_axis_limits(f"{tag}_y_axis", -0.1, 1.1)
                        dpg.set_axis_limits(f"{tag}_x_axis", 0, DATA_POINTS_NUM)
                        dpg.add_line_series(time, data[0], parent=f"{tag}_y_axis", tag=f"{tag}_series")

                with dpg.plot(label="Filter output", height=150, width=500, anti_aliased=True):
                    dpg.add_plot_axis(dpg.mvXAxis, tag="delta_x_axis", label="Time")
                    dpg.add_plot_axis(dpg.mvYAxis, tag="delta_y_axis", no_tick_marks=True, no_tick_labels=True)
                    dpg.set_axis_limits("delta_y_axis", -1.1, 1.1)
                    dpg.set_axis_limits("delta_x_axis", 0, DATA_POINTS_NUM)
                    dpg.add_line_series(time, data[0], parent="delta_y_axis", tag="delta_series")

                with dpg.group(horizontal=True):
                    dpg.add_text("Lead counter: 0", tag="lead_indicator")
                    dpg.add_spacer(width=50)
                    dpg.add_text("Lag counter: 0", tag="lag_indicator")

            with dpg.plot(label="Oscillators phases", height=500, width=500, anti_aliased=True):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, tag="phase_x_axis", label="Time")
                dpg.add_plot_axis(dpg.mvYAxis, tag="phase_y_axis", no_tick_marks=True, no_tick_labels=True,
                                  label="Time/Period")
                dpg.set_axis_limits("phase_x_axis", 0, DATA_POINTS_NUM)
                dpg.set_axis_limits("phase_y_axis", 0, 5)
                dpg.add_line_series(time, data[5], parent="phase_y_axis", tag="phase_input_series", label="Input")
                dpg.add_line_series(time, data[6], parent="phase_y_axis", tag="phase_local_series", label="Local")
