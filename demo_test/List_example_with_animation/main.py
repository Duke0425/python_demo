from cgitb import text
from datetime import datetime

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.factory import Factory
from kivy.animation import Animation
from kivy.properties import ListProperty, NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.behaviors import ButtonBehavior

Factory.register('CusAnchorLayout', module="main")
Factory.register('CusBackgroudButton', module="main")

class CusBackgroudButton(ButtonBehavior, StackLayout):

    bg_color = ListProperty([0.92, 0.92, 0.92, 1])
    label_text = StringProperty("")
    label_font_color = ListProperty([0, 0, 0, 1])
    temp_container = ListProperty()
    time_label_text = StringProperty("")
    extra_text = StringProperty("")
    extra_text_height= NumericProperty(0)
    extra_text_opacity = NumericProperty(0)

    display_image_source = StringProperty("")
    display_image_opacity = NumericProperty(0)
    display_image_width = NumericProperty(0)

    def on_extra_text(self, aInstance, aText):
        pass

    def on_press(self, *args):
        self.temp_container = self.bg_color
        self.bg_color = [0, 0.65, 0.94, 1]

    def on_release(self):
        self.bg_color = self.temp_container
        if self.height == 50:
            anim = Animation(height = 100, extra_text_height = 50, extra_text_opacity = 1, duration=0.5)
            anim.start(self)
        else: 
            anim = Animation(height = 50,  extra_text_height = 0, extra_text_opacity = 0, duration=0.5)
            anim.start(self)

class CusAnchorLayout(AnchorLayout):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        Clock.schedule_once(self.OnInit)

    def OnInit(self, *args):
        gridLayout = self.ids.grid_layout
        lextra_text = "adfhakjsdhfklahdlfkjhalksdhflkahsdlfkh alskjdhflkjashdfkljhasdf"
        # textLength = len(extra_text)
        # n = textLength // 15
        # for i in range(1, n+1):
        #     extra_text[i]
        for i in range(50):
            cusBox = CusBackgroudButton(
                label_text= str(i),
                size_hint_y = None,
                height = 50,
                time_label_text = str(datetime.now().strftime('%H:%M:%S')),
                extra_text = lextra_text
            )
            gridLayout.add_widget(cusBox)

class MainApp(App):
    def build(self):
        pass

if __name__ == '__main__':
    MainApp().run()