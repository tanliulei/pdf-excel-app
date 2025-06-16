[app]

# (str) Title of your application
title = PDF转Excel转换工具

# (str) Package name
package.name = pdftoexcel

# (str) Package domain (needed for android packaging)
package.domain = com.pdftools.converter

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy==2.1.0,pandas,pdfplumber,openpyxl,xlsxwriter,plyer

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, sensorLandscape, portrait, sensorPortrait or all)
orientation = portrait

# (str) Description of the application
description = PDF到Excel转换工具 - 轻松将PDF文件转换为Excel格式

# (str) Author of the application
author = PDF Tools Team

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

[android]

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE,INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (str) Android SDK version to use
android.sdk = 31

# (str) Android build tools version
android.build_tools = 31.0.0

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
android.theme = @android:style/Theme.NoTitleBar

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = False
