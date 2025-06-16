# PDF到Excel转换工具 - 安卓APP

一个基于Kivy框架开发的安卓应用，可以将PDF文件转换为Excel格式。

## 功能特性

- 📱 **安卓原生应用** - 使用Kivy框架开发，完全适配安卓系统
- 📄 **PDF文件处理** - 支持从PDF文件中提取表格和文本数据
- 📊 **Excel输出** - 将提取的数据保存为Excel格式(.xlsx)
- 🎯 **智能数据处理** - 自动删除指定列，格式化时间数据，智能排序
- 📱 **用户友好界面** - 简洁直观的用户界面，支持文件选择和进度显示
- 🔒 **权限管理** - 自动请求必要的存储权限

## 安装和使用

### 方法1: 下载APK文件

1. 从[Releases页面](https://github.com/tanliulei/pdf-excel-app/releases)下载最新的APK文件
2. 在安卓设备上安装APK文件
3. 打开应用，选择PDF文件进行转换

### 方法2: 从源码构建

#### 环境要求

- Python 3.8+
- Buildozer
- Android SDK
- Android NDK

#### 构建步骤

```bash
# 克隆仓库
git clone https://github.com/tanliulei/pdf-excel-app.git
cd pdf-excel-app

# 安装依赖
pip install -r requirements.txt
pip install buildozer

# 构建APK
buildozer android debug
```

## 使用说明

1. **启动应用** - 打开PDF转Excel转换工具
2. **选择文件** - 点击"选择文件"按钮，从文件管理器中选择PDF文件
3. **开始转换** - 点击"开始转换"按钮，应用会自动处理PDF文件
4. **查看结果** - 转换完成后，Excel文件会保存到下载目录

## 数据处理规则

应用会自动执行以下数据处理操作：

- 删除A列、H列、I列的数据
- 按G列和B列进行排序（G列升序，B列降序）
- 格式化B列的时间数据为 `YYYY-MM-DD HH:MM` 格式
- 设置Excel列宽和对齐方式

## 技术架构

- **前端框架**: Kivy 2.1.0
- **数据处理**: Pandas
- **PDF处理**: pdfplumber
- **Excel处理**: openpyxl
- **构建工具**: Buildozer
- **CI/CD**: GitHub Actions

## 开发和测试

### 运行测试

```bash
python test_app.py
```

### 本地开发

```bash
# 安装开发依赖
pip install -r requirements.txt

# 运行应用（桌面版）
python main.py
```

## 权限说明

应用需要以下权限：

- `READ_EXTERNAL_STORAGE` - 读取PDF文件
- `WRITE_EXTERNAL_STORAGE` - 保存Excel文件
- `MANAGE_EXTERNAL_STORAGE` - Android 11+的存储管理权限

## 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 许可证

MIT License