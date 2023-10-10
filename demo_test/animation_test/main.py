from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.uix.image import Image

Builder.load_string('''                               
<Loading>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: root.angle
            axis: 0, 0, 1
            origin: root.center
    canvas.after:
        PopMatrix
    source: 'E:/duke_summary_python/resourse_files/load_3.png'
    size_hint: None, None
    size: 100, 100
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
''')

class Loading(Image):
    angle = NumericProperty(0)
    def __init__(self, **kwargs):
        super(Loading, self).__init__(**kwargs)
        anim = Animation(angle = 360, duration=3) 
        anim += Animation(angle = 360, duration=3)
        anim.repeat = True
        anim.start(self)
        Clock.schedule_once(lambda aDelay:  self.OnStopAnimation(anim), 10)

    def on_angle(self, item, angle):
        if angle == 360:
            item.angle = 0

    def OnStopAnimation(self, aAnimation):
        aAnimation.stop(self)

class TestApp(App):
    def build(self):
        return Loading()

TestApp().run()