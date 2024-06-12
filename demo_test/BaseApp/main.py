from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Line, Rectangle


Factory.register('BaseBoxLayout', module="main")
Factory.register('CusBoxLayout', module="main")


_mainString = """
BaseBoxLayout:
"""


class BaseBoxLayout(BoxLayout):
    pass


class CusBoxLayout(BoxLayout):
    pass

class LocationGridBox(BoxLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.OnInit)

    def OnInit(self, *args):
        figureFloat = self.ids.figure_float
        label = Label(
            text = "10[sup]-10[/sup]",
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            # x = figureFloat.x,
            # y = figureFloat.y,
            markup=True,
        )
        figureFloat.add_widget(label)

        with label.canvas:
            Color(*(1,0,0,0.1))
            Rectangle(pos=label.pos, size = label.size)


class myApp(App):


    def build(self):
        return Builder.load_file('main.kv')


if __name__ == "__main__":
    myApp().run()
