import numpy as _Numeric
import wx
from wx.lib.plot import PlotCanvas, PlotGraphics, PolyLine, PolyMarker


def drawSinCosWaves():
    data1 = 2. * _Numeric.pi * _Numeric.arange(200) / 200.
    data1.shape = (100, 2)
    data1[:, 1] = _Numeric.sin(data1[:, 0])
    markers1 = PolyMarker(data1, legend='Green Markers', colour='green', marker='circle', size=1)

    data1 = 2. * _Numeric.pi * _Numeric.arange(100) / 100.
    data1.shape = (50, 2)
    data1[:, 1] = _Numeric.cos(data1[:, 0])
    lines = PolyLine(data1, legend='Red Line', colour='red')

    pi = _Numeric.pi
    markers2 = PolyMarker([(0., 0.), (pi / 4., 1.), (pi / 2, 0.),
                           (3. * pi / 4., -1)], legend='Cross Legend', colour='blue',
                          marker='cross')

    return PlotGraphics([markers1, lines, markers2], "Graph Title", "X Axis", "Y Axis")


class MainWindow(wx.Frame):
    a = 1
    def __init__(self):
        super().__init__(parent=None, title='Snake')

        panel = wx.Panel(self, wx.ID_ANY)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        checkSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.canvas = PlotCanvas(panel)
        self.canvas.Draw(drawSinCosWaves())
        toggleGrid = wx.CheckBox(panel, label="Show Grid")
        toggleGrid.Bind(wx.EVT_CHECKBOX, self.onToggleGrid)
        toggleLegend = wx.CheckBox(panel, label="Show Legend")
        toggleLegend.Bind(wx.EVT_CHECKBOX, self.onToggleLegend)
        self.text_ctrl = wx.TextCtrl(panel, pos=(5, 5))
        my_btn = wx.Button(panel, label='Set speed snake', pos=(5, 35))

        mainSizer.Add(self.canvas, 1, wx.EXPAND)
        mainSizer.Add(self.text_ctrl)
        mainSizer.Add(my_btn,0,wx.Center)
        checkSizer.Add(toggleGrid, 0, wx.ALL, 15)
        checkSizer.Add(toggleLegend, 0, wx.ALL, 15)
        mainSizer.Add(checkSizer)
        panel.SetSizer(mainSizer)



        self.Show()
    def onToggleGrid(self, event):
        """"""
        self.canvas.SetEnableGrid(event.IsChecked())


    def onToggleLegend(self, event):
        """"""
        self.canvas.SetEnableLegend(event.IsChecked())

if __name__ == '__main__':
    app = wx.App()
    frame = MainWindow()
    frame.Show()
    app.MainLoop()