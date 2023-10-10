from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.properties import ListProperty, NumericProperty
from kivy.clock import Clock
from kivy.uix.image import Image
import datetime

Factory.register('CusBoxLayout', module="main")

class CusBoxLayout(BoxLayout):

    bg_color = ListProperty([1,0,0,0.5])
    bg_box_size = ListProperty([0,100])
    step_width = NumericProperty(100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.myStartedTime = None
        Clock.schedule_once(self.OnInit, 2)

    def on_complete(self, *args):
        completedTime = datetime.datetime.now()
        loadingTime = (completedTime - self.myStartedTime).seconds
        print(loadingTime)
        self.sparking_anim()

    def on_start(self, *args):
        self.myStartedTime = datetime.datetime.now()
        print(self.myStartedTime)

    def OnInit(self, *args):
        anim = Animation(bg_color=[0,0,1,0.5], bg_box_size = [0, 100], duration=1)
        for widthValue in range(self.step_width, 1000, self.step_width):
            anim += Animation(bg_color=[0,0,1,0.5], bg_box_size = [widthValue, 100], duration=1)
        anim.bind(on_complete=self.on_complete)
        anim.bind(on_start=self.on_start)
        anim.start(self)

    def sparking_anim(self):
        anim = Animation(bg_color=[0,0,1,0.5]) + Animation(bg_color=[0,0.5,1,1])
        anim.repeat = True
        anim.start(self)


class TestApp(App):
    def build(self):
        return Builder.load_file('main.kv')

TestApp().run()