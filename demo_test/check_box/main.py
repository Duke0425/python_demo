
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.factory import Factory
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

Factory.register("CusGridLayout", module='duke_summary_python.demo_test.check_box.main')

class CusGridLayout(GridLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(lambda aDelay: self.OnInit())
    
    def OnInit(self):
        self.myLabel = label = Button(text="Label", on_release= self.OnCheckBoxActive)
        self.add_widget(label)
        self.checkBox  = checkBox = CheckBox(background_checkbox_down="E:\\duke_summary_python\\resourse_files\\checked.png",
        background_checkbox_normal="E:\\duke_summary_python\\resourse_files\\unchecked.png")
        checkBox.bind(active = self.OnCheckBoxActive2)
        self.add_widget(checkBox)
        
    def OnCheckBoxActive(self, *args):
        self.checkBox.background_checkbox_down = "E:\\duke_summary_python\\resourse_files\\check_all.png"

    def OnCheckBoxActive2(self, *args):
        self.checkBox.background_checkbox_down = "E:\\duke_summary_python\\resourse_files\\checked.png"

class MainApp(App):
    def build(self):
        return CusGridLayout(cols=2)

if __name__ == '__main__':
    MainApp().run()