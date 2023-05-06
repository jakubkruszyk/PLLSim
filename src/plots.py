from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.pyplot import subplots


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def create_plots():
    fig, axes = subplots(2)
    # add style
    y_labels = ("Input oscillator", "Output signal")
    for ax, label in zip(axes, y_labels):
        ax.set_ylabel(label)
        ax.grid()

    return fig, axes
