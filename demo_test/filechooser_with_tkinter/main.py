import tkinter as tk
from tkinter import filedialog

from kivy.app import App
from kivy.base import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

Builder.load_string("""
<rootwi>:
    orientation:'vertical'
    PathButton:
        on_press: label.text = self.get_path()
    Label:
        id: label

""")
class PathButton(Button):
    @staticmethod
    def get_path():
        root = tk.Tk()
        root.withdraw()

        return(filedialog.askdirectory())

class rootwi(BoxLayout):
    pass


class MyApp(App):
    def build(self):
        return rootwi()

if __name__ == '__main__':
    MyApp().run()