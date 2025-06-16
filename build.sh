#!/bin/bash

# PDF到Excel转换APP构建脚本

echo "开始构建PDF到Excel转换APP..."

# 检查Python环境
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3，请先安装Python3"
    exit 1
fi

# 检查pip
if ! command -v pip &> /dev/null; then
    echo "错误: 未找到pip，请先安装pip"
    exit 1
fi

# 安装依赖
echo "安装Python依赖..."
pip install -r requirements.txt

# 安装buildozer
echo "安装Buildozer..."
pip install buildozer

# 检查buildozer配置
if [ ! -f "buildozer.spec" ]; then
    echo "错误: 未找到buildozer.spec配置文件"
    exit 1
fi

# 清理之前的构建
echo "清理之前的构建文件..."
buildozer android clean

# 开始构建
echo "开始构建APK文件..."
buildozer android debug

# 检查构建结果
if [ $? -eq 0 ]; then
    echo "构建成功！"
    echo "APK文件位置："
    find . -name "*.apk" -type f
else
    echo "构建失败，请检查错误信息"
    exit 1
fi

echo "构建完成！"
