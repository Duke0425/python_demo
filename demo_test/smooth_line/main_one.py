from kivy.app import App
from kivy.graphics import Line
from kivy.graphics.texture import Texture
from kivy.uix.widget import Widget

   
GRADIENT_DATA = (
    b"\x00\x00\x00\x07\x07\x07\x0f\x0f\x0f\x17\x17\x17\x1f\x1f\x1f"
    b"'''///777???GGGOOOWWW___gggooowww\x7f\x7f\x7f\x87\x87\x87"
    b"\x8f\x8f\x8f\x97\x97\x97\x9f\x9f\x9f\xa7\xa7\xa7\xaf\xaf\xaf"
    b"\xb7\xb7\xb7\xbf\xbf\xbf\xc7\xc7\xc7\xcf\xcf\xcf\xd7\xd7\xd7"
    b"\xdf\xdf\xdf\xe7\xe7\xe7\xef\xef\xef\xf7\xf7\xf7\xff\xff\xff"
    b"\xf6\xf6\xf6\xee\xee\xee\xe6\xe6\xe6\xde\xde\xde\xd5\xd5\xd5"
    b"\xcd\xcd\xcd\xc5\xc5\xc5\xbd\xbd\xbd\xb4\xb4\xb4\xac\xac\xac"
    b"\xa4\xa4\xa4\x9c\x9c\x9c\x94\x94\x94\x8b\x8b\x8b\x83\x83\x83"
    b"{{{sssjjjbbbZZZRRRJJJAAA999111)))   \x18\x18\x18\x10\x10\x10"
    b"\x08\x08\x08\x00\x00\x00")


class TestApp(App):
    def build(self):
        widget = Widget()
        # Create texture
        tex = Texture.create(size=(1, 64), colorfmt='rgb')
        tex.blit_buffer(GRADIENT_DATA, colorfmt='rgb')
        # Draw lines with the texture
        with widget.canvas:
            Line(points=(200,200,150), close=True, width=1.01, texture=tex)
            Line(circle=(300,300,150), close=True, width=1.00, texture=None)
        return widget
       
if __name__ == "__main__":    
    TestApp().run()