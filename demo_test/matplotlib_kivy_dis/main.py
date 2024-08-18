from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.clock import Clock

import os
import matplotlib.pyplot as plt
import matplotlib
# Becareful: set 'Agg' before import matplotlib modules
# The default backend is TkAgg, that required use matplotlib in main loop thread
matplotlib.use('Agg')

from matplotlib import cm
# from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib.pyplot as plt
import numpy as np
import json
from types import SimpleNamespace

from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.gridspec import GridSpec

matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
Factory.register('Matty', module="main")

# x = [1,2,3,4,5]
# y = [5,12,6,9,15]
# plt.axis('off')

class Matty(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mySizeInInch = [5.5, 5.0]
        self.myDpi = 100 # image pixel size: size in inch * dpi
        self.myGridspec = dict(width_ratios=[5.1, 0.28], wspace=0.1)
        self.myIsXLogScale = True
        self.myIsYLogScale = True
        self.myFigure = SimpleNamespace()
        Clock.schedule_once(self.load_image_data)


    def load_image_data(self, *args):
        with open('E:\duke_summary_python\demo_test\matplotlib_kivy_dis\\result.json', 'r') as f:
            content = f.read()
        aDict = json.loads(content)
        self.myFigure.coords = aDict['coords']
        self.myFigure.values = aDict['values']
        self.myFigure.x_label = "T2/ms"
        self.myFigure.y_label = 'T1/ms'
        self.myFigure.title = 'T1/T2 Spectrum'

    def dis_figure(self, *args):
        self.__build_plt()
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def dis_2d_image_test(self):
        gs = GridSpec(nrows=3, ncols=4,
                               width_ratios=[2.5, 2.5, 2.5, 0.56], 
                               hspace=0.5, wspace=0.75,
                               left=0.05, right=0.95,
                               bottom=0.1, top=0.95)
        fig = plt.figure(figsize=(8.75, 8))
        top_ax = fig.add_subplot(gs[0, 1:3])
        left_ax = fig.add_subplot(gs[1:3, 0])
        heap_ax = fig.add_subplot(gs[1:3, 1:3])
        color_bar_ax = fig.add_subplot(gs[1:3, 3])

        # Heapmap
        nmin = np.min(self.myFigure.values)
        nmax = np.max(self.myFigure.values)
        self._AddDiagonal(heap_ax)
        levels = 100
        if levels < 0:
            levels = 0
        levels = int(levels)
        mesh = heap_ax.contourf(self.myFigure.coords[0], self.myFigure.coords[1], self.myFigure.values,
                           vmin=nmin, vmax=nmax, cmap=cm.jet, levels=levels)
        heap_ax.set_xscale(self._GetScale(self.myIsXLogScale))
        heap_ax.set_yscale(self._GetScale(self.myIsYLogScale))
        heap_ax.set_xlabel(self.myFigure.x_label)
        heap_ax.set_ylabel(self.myFigure.y_label)
        heap_ax.set_title(self.myFigure.title)
        # colorbar
        fig.colorbar(mesh, cax=color_bar_ax)

        # left_ax
        color = 'tab:blue'
        color_1 = 'tab:red'
        left_ax_t = self.myFigure.coords[1]
        left_ax_data1 = np.sum(self.myFigure.values, axis=0)
        left_ax_data2 = left_ax_data1.cumsum(axis=0)

        left_ax.yaxis.set_ticks_position('right')
        left_ax.set_xlabel("Incremental", color=color)
        left_ax.set_yscale('log')
        left_ax.set_xlim(np.max(left_ax_data1), np.min(left_ax_data1))
        left_ax.set_ylim(np.min(left_ax_t), np.max(left_ax_t))
        left_ax.tick_params(axis='x', labelcolor=color)
        left_ax.ticklabel_format(style='sci', axis='x', scilimits = (0,0))
        left_ax.plot(left_ax_data1, left_ax_t, color=color)

        left_ax_1 = left_ax.twiny()
        left_ax_1.set_xlabel("Cumulative", color=color_1)
        # left_ax_1.set_xlim(np.max(left_ax_data2), np.min(left_ax_data2))
        left_ax_1.set_ylim(np.min(left_ax_t), np.max(left_ax_t))
        left_ax_1.tick_params(axis='x', labelcolor=color_1)
        left_ax_1.set_xlim(np.max(left_ax_data2), np.min(left_ax_data2))
        left_ax_1.ticklabel_format(style='sci', axis='x', scilimits = (0,0))
        left_ax_1.plot(left_ax_data2, left_ax_t, color=color_1)
        
        # top_ax
        top_ax_data_1 = np.sum(self.myFigure.values, axis=1)
        top_ax_data_2 = top_ax_data_1.cumsum(axis=0)
        top_ax_t = self.myFigure.coords[0]

        top_ax.set_ylabel("Incremental", color=color)
        top_ax.tick_params(axis='y', labelcolor=color)
        top_ax.set_xscale("log")
        top_ax.set_xlim(np.min(top_ax_t), np.max(top_ax_t))
        top_ax.ticklabel_format(style='sci', axis='y', scilimits = (0,0))
        top_ax.plot(top_ax_t, top_ax_data_1, color=color)

        top_ax_1 = top_ax.twinx()
        top_ax_1.set_ylabel("Cumulative", color=color_1)
        top_ax_1.plot(top_ax_t, top_ax_data_2, color=color_1)
        top_ax_1.tick_params(axis='y', labelcolor=color_1)
        top_ax_1.ticklabel_format(style='sci', axis='y', scilimits = (0,0))

        # fig.colorbar(mesh, cax=axColorBar)
        canvas = FigureCanvasKivyAgg(fig)
        box = self.ids.box
        box.add_widget(canvas)

        dir = os.getcwd()
        path = os.path.join(dir, 'test.png')
        canvas.print_png(path)

        plt.close(fig)

    def dis_2d_image(self):
        levels = 100
        if levels < 0:
            levels = 0
        levels = int(levels)

        # fig, ax = plt.subplots(1, 1, figsize=self.mySizeInInch, dpi=self.myDpi)
        fig, (ax, axColorBar) = plt.subplots(1, 2, figsize=self.mySizeInInch, dpi=self.myDpi, gridspec_kw=self.myGridspec)

        nmin = np.min(self.myFigure.values)
        nmax = np.max(self.myFigure.values)

        self._AddDiagonal(ax)

        mesh = ax.contourf(self.myFigure.coords[0], self.myFigure.coords[1], self.myFigure.values,
                           vmin=nmin, vmax=nmax, cmap=cm.jet, levels=levels)
        ax.set_xscale(self._GetScale(self.myIsXLogScale))
        ax.set_yscale(self._GetScale(self.myIsYLogScale))
        ax.set_xlabel(self.myFigure.x_label)
        ax.set_ylabel(self.myFigure.y_label)
        ax.set_title(self.myFigure.title)

        # cax = plt.axes
        # divider = make_axes_locatable(ax)
        # ax_hist_color = divider.append_axes("right", 0.2, pad=1)
        self.__add_new_axes(ax)
        self.__add_new_empty_axes(axColorBar)
        fig.colorbar(mesh, cax=axColorBar) # add a new colorbar

        canvas = FigureCanvasKivyAgg(fig)
        box = self.ids.box
        box.add_widget(canvas)



    def __add_color_axes(self, ax):
        divider = make_axes_locatable(ax)
        ax_color = divider.append_axes("right", size="5%", pad=1)
        return ax_color

    def __add_new_empty_axes(self, axColorBar):
        divider = make_axes_locatable(axColorBar)
        # below height and pad are in inches
        cax = divider.append_axes("top", 0.5, pad=1)
        # cax.set_axis_bgcolor('none')
        for axis in ['top','bottom','left','right']:
            cax.spines[axis].set_linewidth(0)
        cax.set_xticks([])
        cax.set_yticks([])

    def dis_top_image(self):
        fig, ax = plt.subplots(1, 1, figsize=[5.1, 3.0], dpi=self.myDpi)
        ax.set_xscale("log")
        ax.set_yscale('linear')
        # ax.set_xlabel
        ax_histx_x = self.myFigure.coords[0]
        ax_histx_y = np.sum(self.myFigure.values, axis=1)
        ax.plot(ax_histx_x, ax_histx_y)
        canvas = FigureCanvasKivyAgg(fig)
        top_box = self.ids.top_box
        top_box.add_widget(canvas)

    def dis_left_image(self):
        pass

    def __add_new_axes(self, ax):
        divider = make_axes_locatable(ax)
        # below height and pad are in inches
        top_ax = divider.append_axes("top", 0.5, pad=1, sharex=ax)
        left_ax = divider.append_axes("left", 0.5, pad=1, sharey=ax)

        top_ax_data_1 = np.sum(self.myFigure.values, axis=1)
        top_ax_data_2 = top_ax_data_1.cumsum(axis=0)
        top_ax_t = self.myFigure.coords[0]

        color = 'tab:blue'
        top_ax.set_ylabel("incremental", color=color)
        top_ax.tick_params(axis='y', labelcolor=color)
        top_ax.plot(top_ax_t, top_ax_data_1, color=color)

        top_ax_1 = top_ax.twinx()
        # top_ax_1 = top_ax

        color_1 = 'tab:red'
        top_ax_1.set_ylabel("Cumulative", color=color_1)
        top_ax_1.plot(top_ax_t, top_ax_data_2, color=color_1)
        top_ax_1.tick_params(axis='y', labelcolor=color_1)

        top_ax_1.set_position([top_ax.get_position().x0, top_ax.get_position().y0, top_ax.get_position().width, top_ax.get_position().height])

        left_ax_t = self.myFigure.coords[1]
        left_ax_data1 = np.sum(self.myFigure.values, axis=0)
        left_ax_data2 = left_ax_data1.cumsum(axis=0)


        left_ax.yaxis.set_ticks_position('right')
        left_ax.set_xlabel("Cumulative", color=color)
        left_ax.set_xlim(np.max(left_ax_data1), np.min(left_ax_data1))
        left_ax.plot(left_ax_data1, left_ax_t, color=color)
    
        # left_ax_1 = left_ax.twiny()
        # left_ax_1.set_xlabel("Cumulative", color=color_1)
        # left_ax_1.set_xlim(np.max(left_ax_t), np.min(left_ax_t))
        # left_ax_1.tick_params(axis='y', labelcolor=color_1)
        # left_ax_1.plot(left_ax_data2, left_ax_t, color=color_1)

        # # make some labels invisible
        # top_ax.xaxis.set_tick_params(labelbottom=False)
        # left_ax.yaxis.set_tick_params(labelleft=False)

    def _AddDiagonal(self, ax):
        y_data_max = np.max(self.myFigure.coords[1])
        y_data_min = np.min(self.myFigure.coords[1])

        # Default x, y => t2, t1 currently
        # T1:T2 = 1:1
        marker_line_1 = np.arange(0, y_data_max + 1)
        # T1:T2 = 10:1
        marker_line_10 = marker_line_1 * 10
        # T1:T2 = 100:1
        marker_line_100 = marker_line_1 * 100
        # T1:T2 = 1000:1
        marker_line_1000 = marker_line_1 * 1000
        kw = {
            'color': '#ffffff',
            'linestyle': '--',
            'linewidth': 1
        }
        ax.set_ylim([y_data_min, y_data_max])
        ax.plot(marker_line_1, **kw)
        ax.plot(marker_line_10, **kw)
        ax.plot(marker_line_100, **kw)
        ax.plot(marker_line_1000, **kw)

    def _GetScale(self, aIsLogScale):
        return 'log' if aIsLogScale else 'linear'

    def __build_plt(self):
        with open('E:\duke_summary_python\demo_test\matplotlib_kivy_dis\\test.json', 'r') as f:
            content = f.read()
        aDict = json.loads(content)
        x = aDict['figures'][0]['x_axis'][0]
        y = aDict['figures'][0]['y_axis'][0]

        plt.plot(x, y, color='red', alpha=0.5)
        plt.xscale('log')
        plt.ylabel("Y Axis")
        plt.xlabel("X Axis")
        plt.xlim((10**-1, 10**4))

    def save_it(self):
        pass

class MyApp(App): 
    def build(self): 
        return Builder.load_file('main.kv')
        

if __name__ == '__main__': 
    MyApp().run()