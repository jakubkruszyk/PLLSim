from src.pll import PLL
from src.layout import *
from src.timer import RepeatedTimer
from src.gui_routines import pll_update


# Plots data lists
# input, local, lead, lag, delta -> match PLL run output
data = [[0 for _ in range(DATA_POINTS_NUM)] for _ in range(7)]
time = [i for i in range(-DATA_POINTS_NUM, 0)]

# PLL structure
pll = PLL(DEFAULT_INPUT_PERIOD, DEFAULT_LOCAL_PERIOD, DEFAULT_LAG_COUNTER, DEFAULT_SUM_COUNTER)

last_run = False

# Event loop timer
timer = RepeatedTimer(REFRESH_RATE, pll_update, pll, data, time)

dpg.create_context()
dpg.create_viewport(title='PLLSim', width=1350)
create_layout(time, data, pll)
dpg.setup_dearpygui()
dpg.show_viewport()

while dpg.is_dearpygui_running():
    running = dpg.get_item_user_data("btn_start")
    speed_update = dpg.get_item_user_data("slider_speed")
    if running != last_run:
        if running:
            timer.start()
        else:
            timer.stop()
        last_run = running

    if speed_update:
        timer.interval = 1 / dpg.get_value("slider_speed")
        dpg.set_item_user_data("slider_speed", False)

    dpg.render_dearpygui_frame()

dpg.destroy_context()
timer.stop()
