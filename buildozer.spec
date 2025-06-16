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
requirements = python3,kivy,pandas,pdfplumber,openpyxl,xlsxwriter

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (landscape, sensorLandscape, portrait, sensorPortrait or all)
orientation = portrait

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

[android]

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 28

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 21.4.7075529

# (str) Android SDK version to use
android.sdk = 28

# (str) Android build tools version
android.build_tools = 28.0.3

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = False
