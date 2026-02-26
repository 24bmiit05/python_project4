import unittest
import matplotlib
import time_series_visualizer as ts


class TestTimeSeriesVisualizer(unittest.TestCase):

    def test_line_plot(self):
        fig = ts.draw_line_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_bar_plot(self):
        fig = ts.draw_bar_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_box_plot(self):
        fig = ts.draw_box_plot()
        self.assertIsInstance(fig, matplotlib.figure.Figure)


if __name__ == "__main__":
    unittest.main()