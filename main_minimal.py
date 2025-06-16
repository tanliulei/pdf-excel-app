"""
PDF到Excel转换 - 安卓APP最小化版本
专为稳定构建设计
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.utils import platform
import os

class PDFToExcelApp(App):
    def build(self):
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 标题
        title_label = Label(
            text='PDF到Excel转换工具',
            size_hint=(1, 0.2),
            font_size='20sp'
        )
        main_layout.add_widget(title_label)
        
        # 状态标签
        self.status_label = Label(
            text='欢迎使用PDF到Excel转换工具！\n\n这是一个测试版本，用于验证APK构建。\n\n完整功能将在后续版本中提供。',
            size_hint=(1, 0.5),
            text_size=(None, None),
            halign='center',
            valign='middle'
        )
        main_layout.add_widget(self.status_label)
        
        # 按钮布局
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2), spacing=10)
        
        # 测试按钮
        test_btn = Button(text='测试功能')
        test_btn.bind(on_press=self.test_function)
        button_layout.add_widget(test_btn)
        
        # 关于按钮
        about_btn = Button(text='关于')
        about_btn.bind(on_press=self.show_about)
        button_layout.add_widget(about_btn)
        
        main_layout.add_widget(button_layout)
        
        # 平台信息
        platform_label = Label(
            text=f'运行平台: {platform}\n构建版本: v1.0-minimal',
            size_hint=(1, 0.1),
            font_size='12sp'
        )
        main_layout.add_widget(platform_label)
        
        return main_layout
    
    def test_function(self, instance):
        """测试功能"""
        self.status_label.text = '✅ 测试功能已执行！\n\n应用运行正常。\n\n安卓APK构建成功！\n\n完整的PDF处理功能将在下个版本中提供。'
    
    def show_about(self, instance):
        """显示关于信息"""
        about_text = """PDF到Excel转换工具 v1.0

这是一个基于Kivy框架开发的安卓应用。

当前版本特性：
• 基础UI框架 ✅
• 安卓平台适配 ✅
• APK构建支持 ✅

即将推出：
• PDF文件处理
• Excel格式输出
• 数据转换功能

开发者：PDF Tools Team
技术栈：Python + Kivy"""
        
        self.show_popup('关于应用', about_text)
    
    def show_popup(self, title, message):
        """显示弹窗"""
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # 消息标签
        message_label = Label(
            text=message, 
            text_size=(300, None),
            halign='center',
            valign='middle'
        )
        popup_layout.add_widget(message_label)
        
        # 关闭按钮
        close_btn = Button(text='确定', size_hint=(1, 0.3))
        popup_layout.add_widget(close_btn)
        
        popup = Popup(
            title=title,
            content=popup_layout,
            size_hint=(0.9, 0.6),
            auto_dismiss=False
        )
        
        close_btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    PDFToExcelApp().run()
