name: 编译PDF转Excel安卓APP

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-20.04
    timeout-minutes: 120
    
    steps:
    - name: 检出代码
      uses: actions/checkout@v4
    
    - name: 设置Python环境
      uses: actions/setup-python@v4
      with:
        python-version: '3.8'
    
    - name: 设置Java环境
      uses: actions/setup-java@v4
      with:
        distribution: 'adopt'
        java-version: '8'
    
    - name: 安装Android SDK
      run: |
        sudo apt-get update
        sudo apt-get install -y wget unzip openjdk-8-jdk
        
        # 下载并安装Android SDK
        wget -q https://dl.google.com/android/repository/commandlinetools-linux-6858069_latest.zip
        unzip -q commandlinetools-linux-*_latest.zip
        mkdir -p $HOME/android-sdk/cmdline-tools
        mv cmdline-tools $HOME/android-sdk/cmdline-tools/latest
        
        # 设置环境变量
        export ANDROID_HOME=$HOME/android-sdk
        export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
        echo "ANDROID_HOME=$HOME/android-sdk" >> $GITHUB_ENV
        echo "JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> $GITHUB_ENV
        echo "$HOME/android-sdk/cmdline-tools/latest/bin" >> $GITHUB_PATH
        echo "$HOME/android-sdk/platform-tools" >> $GITHUB_PATH
        
        # 安装SDK组件
        yes | $HOME/android-sdk/cmdline-tools/latest/bin/sdkmanager --licenses
        $HOME/android-sdk/cmdline-tools/latest/bin/sdkmanager "platforms;android-28" "build-tools;28.0.3" "platform-tools" "ndk;21.4.7075529"
    
    - name: 安装系统依赖
      run: |
        sudo apt-get update
        sudo apt-get install -y autoconf libtool pkg-config \
          zlib1g-dev libncurses5-dev libncursesw5-dev libncurses-dev cmake \
          libffi-dev libssl-dev build-essential python3-dev git
    
    - name: 安装Python依赖
      run: |
        python -m pip install --upgrade pip setuptools wheel
        pip install buildozer==1.4.0 cython==0.29.32
        pip install kivy==2.0.0
        pip install pandas pdfplumber openpyxl xlsxwriter
    
    - name: 缓存buildozer依赖
      uses: actions/cache@v4
      with:
        path: |
          ~/.buildozer
        key: buildozer-cache-${{ runner.os }}-${{ hashFiles('buildozer.spec') }}
        restore-keys: |
          buildozer-cache-${{ runner.os }}-
    
    - name: 编译APK
      run: |
        echo "开始编译Android APK..."
        buildozer android debug --verbose
        echo "编译完成"
    
    - name: 验证编译结果
      run: |
        if [ -f bin/*.apk ]; then
          echo "APK编译成功！"
          ls -la bin/
          echo "文件大小: $(du -h bin/*.apk)"
        else
          echo "APK编译失败"
          ls -la
          exit 1
        fi
    
    - name: 重命名APK文件
      run: |
        cd bin
        mv *.apk pdf-excel-converter.apk
        echo "APK文件已重命名"
    
    - name: 上传APK文件
      uses: actions/upload-artifact@v4
      with:
        name: pdf-excel-android-app
        path: bin/pdf-excel-converter.apk
        retention-days: 90
