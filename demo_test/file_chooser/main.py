from pathlib import Path

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup


Factory.register('FileBoxLayout', module="main")
Factory.register('FileIconChooserBox', module="main")
Factory.register('FileListChooserBox', module="main")

class FileBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def OnChooseFilesListMode(self, *args):
        print("ListFileChooser Popup open")
        fileChooserBox = FileListChooserBox()
        pop = Popup(
            content = fileChooserBox
        )
        pop.open()
        def OnClosePopup(aInstance):
            self.ids.file_name.text = aInstance.file_name if aInstance.file_name else ""
            self.ids.file_content.text = aInstance.file_content_first_line if aInstance.file_content_first_line else ""
            pop.dismiss()

        fileChooserBox.bind(on_cancel = OnClosePopup)

    def OnChooseFilesIconMode(self, *args):
        print("IconFileChooser Popup open")
        fileChooserBox = FileIconChooserBox()
        pop = Popup(
            content = fileChooserBox
        )
        pop.open()
        def OnClosePopup(aInstance):
            self.ids.file_name.text = aInstance.file_name if aInstance.file_name else ""
            self.ids.file_content.text = aInstance.file_content_first_line if aInstance.file_content_first_line else ""
            pop.dismiss()

        fileChooserBox.bind(on_cancel = OnClosePopup)

class FileIconChooserBox(BoxLayout):
    
    __events__ = ("on_cancel", )

    file_content_first_line = StringProperty("")
    file_name = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_cancel(self, *args):
        self.file_content_first_line = ""
        self.file_name = ""
    
    def OnSave(self, aFilePath, aFileName):
        with open(Path(aFileName), 'r', encoding='utf-8') as file:
            content = file.readlines()
        self.file_content_first_line = content[0]
        self.file_name = str(aFileName)
        print("FileChooserBox save file")
        self.dispatch("on_cancel")


class FileListChooserBox(BoxLayout):
    __events__ = ("on_cancel", )

    file_content_first_line = StringProperty("")
    file_name = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_cancel(self, *args):
        self.file_content_first_line = ""
        self.file_name = ""
    
    def OnSave(self, aFilePath, aFileName):
        with open(Path(aFileName), 'r', encoding='utf-8') as file:
            content = file.readlines()
        self.file_content_first_line = content[0]
        self.file_name = str(aFileName)
        print("FileChooserBox save file")
        self.dispatch("on_cancel")


class MainApp(App):
    def build(self):
        pass

if __name__ == '__main__':
    MainApp().run()