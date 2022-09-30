from kivy.app import App
from kivy.lang import Builder
from kivy.core.image import Image as CoreImage
from kivy.properties import ListProperty, ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
from math import sin, cos, pi


kv = '''
Widget:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Mesh:
            vertices: app.mesh_points
            indices: range(int(len(app.mesh_points) / 4))
            texture: app.mesh_texture
            mode: 'triangle_fan'
'''


class MeshBallApp(App):
    mesh_points = ListProperty([])
    mesh_texture = ObjectProperty(None)

    def build(self):
        self.mesh_texture = CoreImage('data/logo/kivy-icon-512.png').texture
        Clock.schedule_interval(self.update_points, 0)
        return Builder.load_string(kv)

    def update_points(self, *args):
        points = [Window.width / 2, Window.height / 2, .5, .5]
        i = 0
        while i < 2 * pi:
            i += 0.01 * pi
            points.extend([
                Window.width / 2 + cos(i) * 100,
                Window.height / 2 + sin(i) * 100,
                .5 + cos(i),
                .5 + sin(i)])

        self.mesh_points = points

if __name__ == '__main__':
    MeshBallApp().run()
