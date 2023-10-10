from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle


Factory.register('BaseBoxLayout', module="main")


class BaseBoxLayout(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda aDelay: self.OnInit())


    def OnInit(self, *args):
        with self.canvas.before:
            Color(1, 0.13, 0.13, 1)
            Rectangle(pos=self.pos, size=self.size)

class myApp(App):

    def build(self):
        return Builder.load_file("main.kv")


if __name__ == "__main__":
    myApp().run()
