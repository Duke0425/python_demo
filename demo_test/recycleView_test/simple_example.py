from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from functools import partial


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{
            'text': str(x),
            "on_release": partial(self.butt, x)
            }
            for x in range(100)
        ]

    def butt(self, *args):
        pass

    def OnSorted(self):
        self.data = self.data[::-1]

kv = Builder.load_string('''
BoxLayout:
    orientation:'vertical'
    Button:
        size_hint_y: None
        height: 50
        text: "sorted"
        on_release: rv.OnSorted()
    RV:
        id: rv
        viewclass: 'Button'
        RecycleBoxLayout:
            default_size: None, dp(56)
            default_size_hint: 1, None
            size_hint_y: None
            height: self.minimum_height
            orientation: 'vertical'
''')



class TestApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    TestApp().run()