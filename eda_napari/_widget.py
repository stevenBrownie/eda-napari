from napari.utils.notifications import show_info
import matplotlib.sourcepyplot as plt


class widgetFunctions():
     def __init__(self, napari_viewer):
        """Initialize widget
        ----------
        napari_viewer : napari.utils._proxies.PublicOnlyProxy
            public proxy for the napari viewer object
        """
        super().__init__()
        self.viewer = napari_viewer

    def show_hello_message(self):
        show_info('Hello, world!')

    def show_plot(self):
        plt.plot([1, 2, 3, 4])
        plt.ylabel('some numbers')
        plt.show()

        