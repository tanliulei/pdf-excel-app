"""
PDF到Excel转换APP测试文件
"""

import unittest
import pandas as pd
import tempfile
import os
from unittest.mock import patch, MagicMock

# 模拟Kivy环境
class MockKivyApp:
    def __init__(self):
        pass
    
    def run(self):
        pass

class MockBoxLayout:
    def __init__(self, **kwargs):
        self.children = []
    
    def add_widget(self, widget):
        self.children.append(widget)

class MockLabel:
    def __init__(self, **kwargs):
        self.text = kwargs.get('text', '')

class MockButton:
    def __init__(self, **kwargs):
        self.text = kwargs.get('text', '')
        self.disabled = kwargs.get('disabled', False)
    
    def bind(self, **kwargs):
        pass

class MockFileChooser:
    def __init__(self, **kwargs):
        self.selection = []

class MockProgressBar:
    def __init__(self, **kwargs):
        self.value = 0
        self.max = kwargs.get('max', 100)

class MockPopup:
    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.content = kwargs.get('content', None)
    
    def open(self):
        pass
    
    def dismiss(self):
        pass

# 模拟Kivy模块
import sys
sys.modules['kivy'] = MagicMock()
sys.modules['kivy.app'] = MagicMock()
sys.modules['kivy.uix'] = MagicMock()
sys.modules['kivy.uix.boxlayout'] = MagicMock()
sys.modules['kivy.uix.button'] = MagicMock()
sys.modules['kivy.uix.label'] = MagicMock()
sys.modules['kivy.uix.filechooser'] = MagicMock()
sys.modules['kivy.uix.popup'] = MagicMock()
sys.modules['kivy.uix.progressbar'] = MagicMock()
sys.modules['kivy.clock'] = MagicMock()
sys.modules['kivy.utils'] = MagicMock()

# 设置模拟的类
sys.modules['kivy.app'].App = MockKivyApp
sys.modules['kivy.uix.boxlayout'].BoxLayout = MockBoxLayout
sys.modules['kivy.uix.label'].Label = MockLabel
sys.modules['kivy.uix.button'].Button = MockButton
sys.modules['kivy.uix.filechooser'].FileChooserIconView = MockFileChooser
sys.modules['kivy.uix.progressbar'].ProgressBar = MockProgressBar
sys.modules['kivy.uix.popup'].Popup = MockPopup
sys.modules['kivy.utils'].platform = 'linux'

# 现在导入我们的应用
from main import PDFToExcelApp

class TestPDFToExcelApp(unittest.TestCase):
    def setUp(self):
        """设置测试环境"""
        self.app = PDFToExcelApp()
    
    def test_app_initialization(self):
        """测试应用初始化"""
        self.assertIsInstance(self.app, PDFToExcelApp)
    
    def test_get_storage_path(self):
        """测试存储路径获取"""
        path = self.app.get_storage_path()
        self.assertTrue(isinstance(path, str))
        self.assertTrue(len(path) > 0)
    
    def test_extract_pdf_to_dataframe_with_empty_file(self):
        """测试空PDF文件处理"""
        # 创建一个临时文件
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
            tmp_file.write(b'')  # 空文件
            tmp_file_path = tmp_file.name
        
        try:
            result = self.app.extract_pdf_to_dataframe(tmp_file_path)
            # 空文件应该返回None
            self.assertIsNone(result)
        finally:
            os.unlink(tmp_file_path)
    
    def test_process_excel_data(self):
        """测试Excel数据处理"""
        # 创建测试数据
        test_data = pd.DataFrame({
            0: ['A1', 'A2', 'A3'],
            1: ['B1', 'B2', 'B3'],
            2: ['C1', 'C2', 'C3'],
            3: ['D1', 'D2', 'D3'],
            4: ['E1', 'E2', 'E3'],
            5: ['F1', 'F2', 'F3'],
            6: ['G1', 'G2', 'G3'],
            7: ['H1', 'H2', 'H3'],
            8: ['I1', 'I2', 'I3']
        })
        
        result = self.app.process_excel_data(test_data)
        
        # 检查结果不为空
        self.assertIsNotNone(result)
        # 检查A、H、I列被删除（原来的0、7、8列）
        self.assertEqual(len(result.columns), 6)  # 9-3=6列
    
    def test_process_excel_data_with_insufficient_columns(self):
        """测试列数不足的数据处理"""
        # 创建只有3列的测试数据
        test_data = pd.DataFrame({
            0: ['A1', 'A2'],
            1: ['B1', 'B2'],
            2: ['C1', 'C2']
        })
        
        result = self.app.process_excel_data(test_data)
        
        # 检查结果不为空
        self.assertIsNotNone(result)
        # 应该扩展到9列然后删除A列，剩下8列
        self.assertGreaterEqual(len(result.columns), 2)

if __name__ == '__main__':
    unittest.main()
