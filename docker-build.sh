#!/bin/bash

# Docker构建APK脚本

echo "=== 使用Docker构建Android APK ==="
echo "开始时间: $(date)"

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "错误: 未找到Docker，请先安装Docker"
    exit 1
fi

# 构建Docker镜像
echo "构建Docker镜像..."
docker build -f Dockerfile.build -t pdf-excel-builder .

if [ $? -ne 0 ]; then
    echo "Docker镜像构建失败"
    exit 1
fi

# 运行构建
echo "开始构建APK..."
docker run --rm -v $(pwd):/app -w /app pdf-excel-builder

# 检查结果
if [ -f "bin/*.apk" ]; then
    echo "🎉 构建成功！"
    echo "APK文件："
    ls -la bin/*.apk
else
    echo "❌ 构建失败，未找到APK文件"
fi

echo "结束时间: $(date)"
