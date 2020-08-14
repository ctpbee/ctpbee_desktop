# ctpbee_desktop
ctpbee的桌面端实现

#### 快速使用
```
pip install -r requirement.txt
python ctpbee_desktop.py
```

> 关于打包[ubuntu]
##### ！路径不要有中文
```
pyinstaller ctpbee_desktop.py #生成 ctpbee_desktop.spec  build  dist

```
修改 ctpbee_desktop.spec
```
# ctpbee_desktop.spec

 datas=[("app/static","static"),
        ("venv/lib/python3.7/site-packages/ctpbee-0.31.3-py3.7-linux-x86_64.egg/ctpbee",'ctpbee'),("venv/lib/python3.7/site-packages/PySide2","PySide2")],
 # datas=[("文件或文件夹路径：自行查找","dist下的名称")]
 
 hiddenimports=['PySide2.QtPrintSupport'],
 #可能需要显示导入QtPrintSupport,不过代码中貌似没出现使用的地方
```
再次打包
```
pyinstaller ctpbee_desktop.spec  # 注意后缀  .spec
```
运行
```
cd dist/ctpbee_desktop 
./ctpbee_desktop
```
打包时报错 No module named 'win32com'
```
pip install pypiwin32
```
如k线图不显示（QWebEngineView）

[解决方法](https://blog.csdn.net/weixin_42591308/article/details/100728021)

[64bit](http://download.microsoft.com/download/9/E/1/9E1FA77A-9E95-4F3D-8BE1-4D2D0C947BA2/enu_INREL/vcredistd14x64/vc_redist.x64.exe)

[32bit](http://download.microsoft.com/download/9/E/1/9E1FA77A-9E95-4F3D-8BE1-4D2D0C947BA2/enu_INREL/vcredistd14x86/vc_redist.x86.exe)


** 如果出现不存在dll载入失败 **
```
pip uninstall pyside2 
pip install pyside2
```