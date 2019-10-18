# ctpbee_desktop
ctpbee的桌面端实现

#### 快速使用
```
pip install -r requirement.txt
python run.py
```

> 关于打包[ubuntu]

> 因为本人对Pyinstaller不熟悉，查阅各种资料，最后才得以这种不太优雅的方式进行打包，如果我的打包姿势不对或者有更好的打包方式
欢迎指出和提出。
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