from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout


Factory.register('BaseBoxLayout', module="main")
Factory.register('CusBoxLayout', module="main")


_mainString = """
BaseBoxLayout:
"""


class BaseBoxLayout(BoxLayout):
    pass
class CusBoxLayout(BoxLayout):
    pass


class myApp(App):


    def build(self):
        return Builder.load_file('main.kv')

    pass

if __name__ == "__main__":
    myApp().run()
