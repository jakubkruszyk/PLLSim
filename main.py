import dearpygui.dearpygui as dpg
from src.globals import DATA_POINTS_NUM
from src.pll import PLL
from src.layout import *
from src.timer import RepeatedTimer
from src.gui_routines import pll_update

# Default parameters
ref_freq = 10
dco_freq = 10
lead_cnt_max = 1
lag_cnt_max = 1

# Plots data lists

# input, local, lead, lag -> match PLL run output
data = [[0 for _ in range(DATA_POINTS_NUM)] for _ in range(4)]
time = [i for i in range(-DATA_POINTS_NUM, 0)]

# PLL structure
pll = PLL(ref_freq, dco_freq, lead_cnt_max, lag_cnt_max)


# Event loop timer
timer = RepeatedTimer(0.02, pll_update, pll, data, time)

dpg.create_context()
dpg.create_viewport(title='Custom Title')
create_controls(time, data)
timer.start()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
timer.stop()
