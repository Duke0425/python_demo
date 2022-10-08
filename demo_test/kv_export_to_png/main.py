
import os

import kivy
import logging
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label


class MainApp(App):
    def build(self):
        Clock.schedule_once(self.consume, 0)
        return Builder.load_file("main.kv")

    def consume(self, *args):
        gridLayout = self.root.ids.target
        for _ in range(30):
            gridLayout.add_widget(Label(
                text = str(_) + "label",
                size_hint = (1, None),
                height = 100
            ))

    def screenshot_button(self, aLabel):

        imageRootPath = os.getcwd()
        logging.info(f"MainAPP: current path {imageRootPath}")
        imageName = "image_222.bmp"

        imagePath = '/'.join([imageRootPath, imageName])
        aLabel.export_to_png(imagePath)
        logging.info(f"MainAPP: export widget to image success {imagePath}")
        with open(imagePath, mode= 'rb') as file:
            content = file.read()

        logging.info(f"MainAPP: read image data success {imagePath}") 
        # with open('rewirte.jpg', mode="wb") as file:
        #     file.write(content)

if __name__ == '__main__':
    MainApp().run()