from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.vkeyboard import VKeyboard
from kivy.base import runTouchApp


class myApp(App):

    def build(self):
        return Builder.load_file("my.kv")

if __name__ == "__main__":
    myApp().run()