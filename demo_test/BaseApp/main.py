from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout


Factory.register('BaseBoxLayout', module="main")


_mainString = """
BaseBoxLayout:
"""


class BaseBoxLayout(BoxLayout):
    pass


class myApp(App):

    def build(self):
        return Builder.load_string(_mainString)


if __name__ == "__main__":
    myApp().run()
