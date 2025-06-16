from kivy.app import App
from kivy.uix.label import Label

class PDFToExcelApp(App):
    def build(self):
        return Label(text='PDF到Excel转换工具\n\n构建测试成功！')
if __name__ == '__main__':
    PDFToExcelApp().run()
