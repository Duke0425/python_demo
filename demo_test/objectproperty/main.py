from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


Factory.register('CusBoxLayout', module="main")


class CusBoxLayout(BoxLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def change_content_box_obj(self, *args):
        for children in self.ids.content_box.children:
            Clock.schedule_once(children.get_prara)


class LocationGridBox(BoxLayout):

    dict_content = ObjectProperty({})

    def get_prara(self, *args):
        self.dict_content.clear()
        self.dict_content = {
            'x': 1,
            'w': 2
        }


class myApp(App):
    def build(self):
        return Builder.load_file('main.kv')


if __name__ == "__main__":
    myApp().run()
