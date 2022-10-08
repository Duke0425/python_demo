
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup


class ConfigScreenManager(ScreenManager):
    pass


class LoginScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class ConfigureScreen(Screen):
    pass


class ConfigPopup(BoxLayout):

    def OnChangeScreen(self, aButton):
        self.ids.config_screen_manager.current = aButton.text


class MainApp(App):
    def build(self):
        return Builder.load_file("screen_manager_test.kv")

    def OnOpenPopup(self, aButton):
        pop = Popup(
            title = 'About',
            title_align = 'center',
            content = ConfigPopup(),
            auto_dismiss = False
        )
        pop.open()

if __name__ == '__main__':
    MainApp().run()