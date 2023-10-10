import weakref
from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.graphics import Color, Triangle
from kivy.weakproxy import WeakProxy
from kivy.properties import BooleanProperty, NumericProperty
import logging

Factory.register('MouseFloat', module="main")
Factory.register('MouseBox', module="main")

class MouseBox(BoxLayout):
    pass

class MouseFloat(FloatLayout):

    disabled_choose = BooleanProperty(False)
    choose_depth = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.myYList = []
        Window.bind(mouse_pos = self.on_mouse_pos)
        Window.bind(on_touch_down = self.on_touch_down_event)
        self.AddWidgets()
        self.add_triangle()

    def on_touch_down_event(self, window, mouse):
        if self.disabled_choose:
            return

        if self.x <  mouse.pos[0] < self.right and self.y <  mouse.pos[1] < self.top:
            self.displayCurrentYLabelFont()

    def on_mouse_pos(self, window, pos):
        if self.disabled_choose:
            return

        if self.x < pos[0] < self.right and self.y < pos[1] < self.top:
            logging.info(str(pos))

            near = min(self.myYList, key=lambda x:abs(x - pos[1]))
            logging.info(str(near))
            self.box.center_y = near
            self.change_triangle_pos()

    def displayCurrentYLabelFont(self):
        centerY = self.box.center_y
        if not self.choose_depth:
            label = Label(
                    size_hint_y = None,
                    height = 20,
                    text = str(centerY),
                    x = self.x + 50,
                    center_y = centerY,
                    halign = 'left',
                    valign = 'center',
                    color = (0.52,0,1,1)
                )
            self.add_widget(label)
            self.label = WeakProxy(label)
        else:
            self.label.center_y = centerY
            self.label.text = str(centerY)
        self.choose_depth = centerY

    def AddWidgets(self):
        for i in range(1, 10):
            label = Label(
                size_hint_y = None,
                height = 20,
                text = '(' + str(self.x) + ','+ str(self.y + 50 * i)+ ')',
                color = (1,0,0,1),
                x = self.x,
                center_y = self.y + 50 * i,
                halign = 'left',
                valign = 'center',
            )
            self.myYList.append(label.center_y)
            self.add_widget(label)

    def change_triangle_pos(self):
        box = self.box
        box.canvas.clear()
        with box.canvas:
            Color(0.52,0,1,1)
            Triangle(points=[box.x, box.y, box.right, box.center_y, box.x, box.top])

    def add_triangle(self):
        box = BoxLayout(
            size_hint = (None,None),
            size = (20,20),
            x = self.x + 40,
            y = self.y,
            opacity = 1
            )

        self.add_widget(box)
        self.box = WeakProxy(box)

    def OnChooseDisbaledBtnDown(self, *args):
        self.disabled_choose = not self.disabled_choose
        self.remove_widget(self.label)
        self.choose_depth = 0
        self.box.canvas.clear()


class myApp(App):

    def build(self):
        return Builder.load_file('main.kv')


if __name__ == "__main__":
    myApp().run()
