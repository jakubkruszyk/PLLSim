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
        self.fig = fig
        self.fig_agg = draw_figure(plots_canvas, fig)
        self.axes = axes

    def draw(self):
        self.fig_agg.draw()


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
