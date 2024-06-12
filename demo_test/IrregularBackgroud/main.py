'''
Mesh test
=========

This demonstrates the use of a mesh mode to distort an image. You should see
a line of buttons across the bottom of a canvas. Pressing them displays
the mesh, a small circle of points, with different mesh.mode settings.
'''

from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Mesh, Color, Line, SmoothLine, Bezier, Quad
from functools import partial
from math import cos, sin, pi
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.effectwidget import EffectWidget
from kivy.uix.effectwidget import (MonochromeEffect,
                                   InvertEffect,
                                   ChannelMixEffect,
                                   ScanlinesEffect,
                                   FXAAEffect,
                                   PixelateEffect,
                                   HorizontalBlurEffect,
                                   VerticalBlurEffect)
from kivy.config import Config
Config.get('graphics', 'multisamples')
Config.set('graphics', 'multisamples', '4')
GRADIENT_DATA_DARKER = (
    b"\x00\x00\x00\x07\x07\x07\x0f\x0f\x0f\x17\x17\x17\x1f\x1f\x1f"
    b"'''///777???GGGOOOWWW___gggooowww\x7f\x7f\x7f\x87\x87\x87"
    b"\x8f\x8f\x8f\x97\x97\x97\x9f\x9f\x9f\xa7\xa7\xa7\xaf\xaf\xaf"
    b"\xb7\xb7\xb7\xbf\xbf\xbf\xc7\xc7\xc7\xcf\xcf\xcf\xd7\xd7\xd7"
    b"\xdf\xdf\xdf\xe7\xe7\xe7\xef\xef\xef\xf7\xf7\xf7\xff\xff\xff"
    b"\xf6\xf6\xf6\xee\xee\xee\xe6\xe6\xe6\xde\xde\xde\xd5\xd5\xd5"
    b"\xcd\xcd\xcd\xc5\xc5\xc5\xbd\xbd\xbd\xb4\xb4\xb4\xac\xac\xac"
    b"\xa4\xa4\xa4\x9c\x9c\x9c\x94\x94\x94\x8b\x8b\x8b\x83\x83\x83"
    b"{{{sssjjjbbbZZZRRRJJJAAA999111)))   \x18\x18\x18\x10\x10\x10"
    b"\x08\x08\x08\x00\x00\x00")

GRADIENT_DATA_BRIGHTER = (
    b"\x00\x00\x00\x07\x07\x07\x0f\x0f\x0f\x17\x17\x17\x1f\x1f\x1f"
    b"'''///777???GGGOOOWWW___gggooowww\x7f\x7f\x7f\x87\x87\x87"
    b"\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xaf\xaf\xaf"
    b"\xff\xff\xff\xbf\xbf\xbf\xc7\xc7\xc7\xcf\xcf\xcf\xff\xff\xff"
    b"\xff\xff\xff\xe7\xe7\xe7\xef\xef\xef\xf7\xf7\xf7\xff\xff\xff"
    b"\xff\xff\xff\xee\xee\xee\xe6\xe6\xe6\xde\xde\xde\xff\xff\xff"
    b"\xff\xff\xff\xc5\xc5\xc5\xbd\xbd\xbd\xb4\xb4\xb4\xff\xff\xff"
    b"\xff\xff\xff\xff\xff\xff\x94\x94\x94\x8b\x8b\x8b\x83\x83\x83"
    b"{{{sssjjjbbbZZZRRRJJJAAA999111)))   \x18\x18\x18\x10\x10\x10"
    b"\x08\x08\x08\x00\x00\x00")


class CusBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.OnInit)
    
    def change_mode(self, mode, *largs):
        self.mesh.mode = mode

    def build_mesh(self, pos_x, pos_y):
        """ returns a Mesh of a rough circle. """
        vertices = []
        indices = []
        step = 100
        istep = (pi * 2) / float(step)
        for i in range(step):
            x = pos_x + cos(istep * i) * 100
            y = pos_y + sin(istep * i) * 100
            vertices.extend([x, y, 0, 0])
            indices.append(i)
            if i == 50:
                break
        return Mesh(vertices=vertices, indices=indices, mode='line_loop')

    def build_irregular_mesh(self, pos_x, pos_y):
        # vertices = [
        #     305, 500, 0 , 0, 
        #     311, 400, 0 , 0, 
        #     318, 200, 0 , 0, 
        #     350, 200, 0 , 0,
        #     311, 400, 0 , 0, 
        #     340, 500, 0 , 0, 
        #     # 280, 270, 0 , 0, 
        #     # 280, 280, 0 , 0, 
        #     # 280, 300, 0 , 0, 

        # ]
        # indices = [0,1,2,3,4,5]
        mesh_list = []
        a1 = [[305, 500],[311, 400], [318, 200]]
        b1 = [[340, 500],[311, 400], [350, 200]]
        vertices = [
            305, 500, 0, 0,
            311, 400, 0, 0,
            340, 500, 0, 0,
        ]
        indices = [0,1,2]
        mesh_list.append(Mesh(vertices=vertices, indices=indices, mode='triangle_fan'))
        vertices = [
            311, 400, 0, 0,
            318, 200, 0, 0,
            350, 200, 0, 0,
        ]
        indices = [0,1,2]
        mesh_list.append(Mesh(vertices=vertices, indices=indices, mode='triangle_fan'))
        return mesh_list

    def to_points(self, pos_x, pos_y):
        vertices = []
        indices = []
        step = 100
        istep = (pi * 2) / float(step)
        for i in range(step):
            x = pos_x + cos(istep * i) * 100
            y = pos_y + sin(istep * i) * 100
            vertices.extend([x, y])
            indices.append(i)
            if i == 50:
                break
        # tex = Texture.create(size=(1, 64), colorfmt='rgb', bufferfmt='ubyte')
        # tex.blit_buffer(GRADIENT_DATA_DARKER, colorfmt='rgb')
        return Line(points=vertices, width=1.0, cap='round', joint='round')

    def OnInit(self, *args):
        imageFloat = self.ids.image_float

        # for i in range(3):
        #     wid = Widget()
        #     with wid.canvas:
        #         Color(0, 0, 0, 1)
        #         self.to_points(300+i*20, 300+i*20)
        #         Color(0.035, 0.3961, 0.0352, 0.3)
        #         self.mesh = self.build_mesh(300+i*20, 300+i*20)
        #     imageFloat.add_widget(wid)

        wid = Widget()
        with wid.canvas:
            Color(0.035, 0.3961, 0.0352, 0.3)
            # vertices = [
            # 311, 400, 0, 0,
            # 318, 200, 0, 0,
            # 318, 200, 0, 0,
            # 350, 200, 0, 0,
            # ]
            # indices = [0,1,2,3]
            # Mesh(vertices=vertices, indices=indices, mode='triangle_fan')
            vertices = [
            1186.8333333333333, 866.65, 0, 0, 
            1186.8333333333333, 850.51, 0, 0, 
            1186.8333333333333, 834.37, 0, 0, 
            1186.8333333333333, 818.23, 0, 0, 
            1186.8333333333333, 802.09, 0, 0, 
            1186.8333333333333, 785.9499999999999, 0, 0, 
            1186.8333333333333, 769.81, 0, 0, 
            1186.8333333333333, 753.6700000000001, 0, 0, 
            1186.8333333333333, 737.53, 0, 0, 
            1186.8333333333333, 721.39, 0, 0, 

            1215.266204438511, 721.39, 0, 0, 
            1242.239966307231, 737.53, 0, 0, 
            1201.2240782985732, 753.6700000000001, 0, 0, 
            1248.4714511113636, 769.81, 0, 0, 
            1246.6666454397318, 785.9499999999999, 0, 0, 
            1245.5943625373102, 802.09, 0, 0, 
            1188.1504655453189, 818.23, 0, 0,
            1222.8759742110701, 834.37, 0, 0, 
            1226.5683949764853, 850.51, 0, 0, 
            1285.5219004985304, 866.65, 0, 0
            ]
            indices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
            # self.mesh = Mesh(vertices=vertices, indices=indices, mode='triangle_fan')
            # points = 
            Quad(points=[1186.8333333333333, 866.65, 1186.8333333333333, 850.51, 
            1226.5683949764853, 850.51,
                1285.5219004985304, 866.65,
                ]
            )
            Color(0.035, 0.3961, 0.0352, 0.3)
            Quad(points=[1186.8333333333333, 850.51,
            1186.8333333333333, 834.37,
            1222.8759742110701, 834.37,
            1226.5683949764853, 850.51,
            ]
            )
    
        imageFloat.add_widget(wid)
        layout = self.ids.button_box

        for mode in ('points', 'line_strip', 'line_loop', 'lines',
                'triangle_strip', 'triangle_fan'):
            button = Button(text=mode)
            button.bind(on_release=partial(self.change_mode, mode))
            layout.add_widget(button)


class MeshTestApp(App):

    def build(self):
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    MeshTestApp().run()