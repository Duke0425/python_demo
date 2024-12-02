import encodings
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.animation import Animation
from kivy.clock import Clock


class CusGridLayout(GridLayout):

    def TriggerAnimation(self):
        widget = self.ids.middle_text
        self.text  = text = widget.text
        self.textGen = self.GetGenOfText(text)
        Clock.schedule_interval(self.update_label, 0.3)
        # anim = Animation(color=(0, 0, 0, 1), duration=1) + Animation(color=(1, 1, 1, 1), duration=1)
        # anim.repeat = True
        # anim.start(widget)
        # anim.repeat = True

    def GetGenOfText(self, text):
        context = text
        while len(context) >= 20:
            yield context[0:20]
            context = context[1:]


    def update_label(self, dt):
        try:
            widget = self.ids.middle_text
            text = next(self.textGen)
            widget.text = text
        except StopIteration:
            Clock.unschedule(self.update_label)
            self.textGen = self.GetGenOfText(self.text)
            Clock.schedule_interval(self.update_label, 0.3)


    def StopAnimation(self):
        Clock.unschedule(self.update_label)
        widget = self.ids.middle_text
        widget.text = self.text



class SomeApp(App):
    def build(self):
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    SomeApp().run()