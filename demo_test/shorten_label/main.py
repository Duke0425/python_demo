from kivy.app import App
from kivy.lang import Builder

class MainAPP(App):

    def build(self):
        return Builder.load_file('main.kv')

if __name__ == '__main__':
    app = MainAPP().run()