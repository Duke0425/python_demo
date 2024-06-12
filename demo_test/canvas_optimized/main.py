from array import array 
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.clock import Clock 
from kivy.graphics.texture import Texture 
from kivy.graphics import Rectangle 

class MyWidget(Widget): 
    def __init__(self, **kwargs): 
        super(MyWidget, self).__init__(**kwargs) 

        self.texture = Texture.create(size=(512, 512), colorfmt='rgb', bufferfmt='ubyte') 

        # 'rgb' 纹理格式意味着每个像素需要 3 个字节，共有 512 x 512 像素
        # 这用黑白渐变初始化缓冲区
        buf = [int(x * 255 / (512*512*3)) for x in range( 512*512*3)] 
        self.cbuffer = array('B', buf) 
        self.texture.blit_buffer(self.cbuffer) 

    # 使用上面的纹理在画布上下文中创建矩形
        with self.canvas: 
            Rectangle( texture=self.texture, pos=self.pos, size=(512, 512)) 

        # 记录当前刻度以用于定位
        self.tick = 0 
        # 设置时间表以触发更改缓冲区和纹理的回调，然后请求重绘
        # 第二参数是时间间隔，每个时钟周期都会传递给回调（第一个参数）
        Clock.schedule_interval(self.mutate_buffer, 1 / 60.) 

    def mutate_buffer(self, _dt): 
        # 抓取整个缓冲区一行 (512 x 3 RGB 字节）一次。
        pos = (self.tick * 512 *3) % (512 * 512 * 3) 
        # 下次更新tick；产量会更干净，而且效果也同样好。
        self.tick += 1 
        # 反转当前位置的值并分配给灰度的每个通道
        val = 255 - self.cbuffer[pos] 
        for pixel in range(0, 512 * 3, 3): 
            for channel in [0, 1,2]: 
                self.cbuffer[pos + pixel + channel] = val 

        # 更新纹理的缓冲区，然后请求重绘。
        self.texture.blit_buffer(self.cbuffer) 
        self.canvas.ask_update() 

class MyApp(App): 
    def build(self): 
        return MyWidget() 

if __name__ == '__main__': 
    MyApp().run()