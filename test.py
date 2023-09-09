import dearpygui.dearpygui as dpg
import numpy as np
from threading import Timer

dpg.create_context()
dpg.create_viewport(title='Custom Title')

x_space = np.linspace(0, 4*np.pi, 100)
y_space = np.sin(x_space)
scale = 1


def timer_callback():
    global y_space, scale
    if scale >= 10:
        scale = 1
    else:
        scale += 0.1
    y_space = np.sin(scale*x_space)
    dpg.set_value('series_tag', [x_space, y_space])


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False


tim = RepeatedTimer(0.02, timer_callback)
tim.start()


def change_text(sender, app_data, user_data):
    # dpg.set_value("text item", f"Mouse Button ID: {app_data}")
    print(f"sender: {sender}, app_data: {app_data}, user_data: {user_data}")
    if sender == "btn2":
        dpg.set_value("txt", "Update from btn2")
    else:
        dpg.set_value("txt", "Update from btn1")


def show_config(sender, app_data):
    print(dpg.get_item_configuration("btn2"))
    print(dpg.get_item_configuration("sld1"))
    print(dpg.get_value("sld1"))


def update_plot(sender, app_data):
    global y_space
    if sender == "plot2x":
        y_space = np.sin(2*x_space)
    else:
        y_space = np.sin(x_space)
    dpg.set_value('series_tag', [x_space, y_space])


with dpg.item_handler_registry(tag="widget handler") as handler:
    dpg.add_item_clicked_handler(callback=change_text)


def add_2_col():
    with dpg.group(label="2 group"):
        with dpg.plot(label="Test plot", height=300, width=500):
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
            dpg.add_line_series(x_space, y_space, label="sin(x)", parent="y_axis", tag="series_tag")


with dpg.window(label="Example Window"):
    dpg.add_text("Hello, world")
    with dpg.group(label="Top", horizontal=True):
        with dpg.group(label="Group test", width=200):
            dpg.add_text("Some text", tag="txt")
            dpg.add_slider_int(label="Input", min_value=10, max_value=30, default_value=15, tag="sld1")
            dpg.add_slider_int(label="Local", min_value=10, max_value=30, default_value=15, tag="sld2")
            dpg.add_button(label="Test button1", tag="btn1", user_data="abc")
            dpg.add_button(label="Test button2", tag="btn2", callback=change_text)
            dpg.add_button(label="Test button3", tag="btn3", callback=show_config)
            dpg.add_button(label="Update plot 2x", tag="plot2x", callback=update_plot)
            dpg.add_button(label="Update plot 1x", tag="plot1x", callback=update_plot)
        add_2_col()


dpg.bind_item_handler_registry("btn1", "widget handler")
# dpg.bind_item_handler_registry("btn2", "widget handler")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
tim.stop()
