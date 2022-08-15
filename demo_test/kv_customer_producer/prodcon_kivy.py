from kivy.app import App
from kivy.clock import Clock, _default_time as time  # ok, no better way to use the same clock as kivy, hmm
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import ListProperty

MAX_TIME = 1/60.

kv = '''
BoxLayout:
    ScrollView:
        GridLayout:
            cols: 1
            id: target
            size_hint: 1, None
            height: self.minimum_height
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'add 10'
            on_press: app.consommables.extend(range(10))
        Button:
            text: 'add 100'
            on_press: app.consommables.extend(range(100))
        Button:
            text: 'add 1000'
            on_press: app.consommables.extend(range(1000))
        Button:
            text: 'clear'
            on_press: target.clear_widgets()
<MyLabel@Label>:
    size_hint_y: None
    height: self.texture_size[1]
'''


class ProdConApp(App):
    consommables = ListProperty([])

    def build(self):
        Clock.schedule_interval(self.consume, 0)
        return Builder.load_string(kv)

    def consume(self, *args):
        while self.consommables and time() < (Clock.get_time() + MAX_TIME):
            item = self.consommables.pop(0)  # i want the first one
            label = Factory.MyLabel(
                text='%s : %s : %s' % (item, Clock.get_time(), time()))
            self.root.ids.target.add_widget(label)


if __name__ == '__main__':
    ProdConApp().run()
