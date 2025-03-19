import sys
sys.path.insert(0, "E:/emei/client/src/")
sys.path.insert(0, "E:/emei/client/local/resources/")
sys.path.insert(0, "E:\ci_cache\windows_x86_64_msvc16_md\MSPY-0.0.0-3a19426-shared-release\bin")

from kivy.resources import resource_add_path
resource_add_path(str("E:/emei/client/local/resources/"))

from ms_init import versions
from ms_init import args as startupArguments

# 以上是固定调用峨眉客户端组件的开头

from kivy.app import App
from kivy.properties import  ObjectProperty, NumericProperty
from kivy.uix.recycleview import RecycleView 
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.modalview import ModalView

from msc.client.controls.check_section_list_box import CheckListBoxItemButton
from msc.client.controls.button_factory import CusBackgroudButton

KV = """
<RV>: 
    viewclass: 'CustomCheckListBoxItemButton' # defines the viewtype for the data items. 
    orientation: "vertical"
    spacing: 40
    padding:10, 10
    space_x: self.size[0]/3

    RecycleBoxLayout:
        id: rv_box
        color:(0, 0.7, 0.4, 0.8) 
        default_size: None, dp(56) 
        default_size_hint: 0.4, None
        size_hint_y: None
        height: self.minimum_height 
        orientation: 'vertical' # defines the orientation of data items
"""
Builder.load_string(KV)


class CustomCheckListBoxItemButton(RecycleDataViewBehavior, CheckListBoxItemButton):
    index = NumericProperty()
    root_widget = ObjectProperty()

    def on_release(self, **kwargs):
        super().on_release(**kwargs)
        self.root_widget.on_select_item(self)

    def on_press(self, **kwargs):
        super().on_press(**kwargs)
        self.root_widget.on_press_change(self)

    def refresh_view_attrs(self, rv, index, data):
        super(CustomCheckListBoxItemButton, self).refresh_view_attrs(rv, index, data)


class RV(RecycleView):
    n = 1

    right_click_menu_list = ['StartDetection', 'Edit', 'Delete']

    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        self.data = [{'text': str(x), 'root_widget': self, "size_hint_y": None, "height": 15 } for x in range(20)]

    def on_select_item(self, btn):
        self.layout_manager # 获取当前视图的部署管理器(BoxLayout)

        rvBox = self.ids.rv_box
        rvBox.children
        height = 5+self.n
        self.n += 1

        self.data = [{'text': str(x), 'root_widget': self, "size_hint_y": None, "height":  height} for x in range(20)]
        print(btn, btn.text)

    def on_press_change(self, btn):
        if btn.mouse_button == 'right':
            menu_content = BoxLayout(orientation='vertical')
            widgetNums = len(self.right_click_menu_list)
            modal_view = ModalView(size_hint=(None, None), height=widgetNums * 30, pos_hint={'x' : btn.touch_spos[0], 'top' : btn.touch_spos[1]})
            for menu_text in self.right_click_menu_list:
                btn = CusBackgroudButton(label_text = menu_text)
                # btn.bind(on_release = lambda btn: self.on_right_click_menu_btn_down(modal_view, btn, item_data))
                menu_content.add_widget(btn)

            modal_view.add_widget(menu_content)
            modal_view.open()

class SampleApp(App): 
    def build(self):
        return RV() 

SampleApp().run()