from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.pyplot import subplots


class Plots:
    def __init__(self, plots_canvas):
        fig, axes = subplots(2)
        # add style
        y_labels = ("Input oscillator", "Output signal")
        for ax, label in zip(axes, y_labels):
            ax.set_ylabel(label)
            ax.grid()
        # create figure and axes
        self.fig = fig
        self.fig_agg = draw_figure(plots_canvas, fig)
        self.axes = axes
        self.axes_values = [[0 for _ in range(100)] for _ in axes]
        self.time_value = -100
        # create initial plots
        self.draw([0 for _ in axes])

    def draw(self, new_values):
        self.time_value += 1
        for ax, ax_values, new_value in zip(self.axes, self.axes_values, new_values):
            ax_values.pop(0)
            ax_values.append(new_value)
            ax.plot(range(self.time_value, self.time_value+100), ax_values)

        self.fig_agg.draw()


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
