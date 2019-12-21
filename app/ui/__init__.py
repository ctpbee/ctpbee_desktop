## ui
# pyside2-uic signin.ui > ui_signin.py

## resource
# pyrcc5 -o img_rc.py signin.qrc


scroll_bar = """
QScrollBar:vertical {  
    width:10px;   
    background-color:rgba(0,0,0,0%);   
    padding-top:10px;   
    padding-bottom:10px;  
}  
  
QScrollBar:horizontal {  
    height:10px;   
    background-color:rgba(0,0,0,0%);   
    padding-left:10px; padding-right:10px;  
}  
  
QScrollBar::handle:vertical {  
    width:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);   
}  
  
QScrollBar::handle:horizontal {  
    height:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #5CACEE, stop:1 #4F94CD);   
}  
  
QScrollBar::handle:vertical:hover {  
    width:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);   
}  
  
QScrollBar::handle:horizontal:hover {  
    height:10px;  
    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #1B89CA, stop:1 #1077B5);   
}  
  
QScrollBar::add-line:vertical {  
    height:10px;  
    width:10px;  
    subcontrol-position: bottom;   
    subcontrol-origin: margin;  
    border-image:url(:/image/add-line_vertical.png);  
}  
  
QScrollBar::add-line:horizontal {  
    height:10px;  
    width:10px;  
    subcontrol-position: right;  
    subcontrol-origin: margin;  
    border-image:url(:/image/add-line_horizontal.png);  
}  
  
QScrollBar::sub-line:vertical {  
    height:10px;  
    width:10px;  
    subcontrol-position: top;   
    subcontrol-origin: margin;  
    border-image:url(:/image/sub-line_vertical.png);  
}  
  
QScrollBar::sub-line:horizontal {  
    height:10px;  
    width:10px;  
    subcontrol-position: left;  
    subcontrol-origin: margin;  
    border-image:url(:/image/sub-line_horizontal.png);  
}  
  
QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical {  
    width:10px;  
    background: #C0C0C0;  
}  
  
QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal {  
    height:10px;  
    background: #C0C0C0;  
}
"""

qss = """
QMainWindow{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}



QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}


QPushButton,QToolButton{
    background:#1b89ca;
    border-radius:2px;
    padding:5px;
}
QPushButton:disabled{
    background:#2B2B2B;
    color:#b6b6b6;
    border-radius:2px;
}
QPushButton:hover,QToolButton:hover{
    border-bottom:1px solid #ffffff;
}

QLabel#title{
    color:#1b89ca;
    border-radius:5px;
    padding:5px
}



QTableWidget{
    border:none;
    background:#2B2B2B;
    color:#ffffff
}

QTableWidget:disabled{
    background:gray;
}

#QTableCornerButton::section,QHeaderView::section{
color:#00c1c1;
background:#2B2B2B;
}


QCheckBox{
    border-radius:5px;
}

QCheckBox::indicator:checked {
    color:#1b89ca;
 }
 
 
QTextEdit{
background:#2B2B2B;
color:#ffffff;
border-radius: 5px;
}



#line{
background:#1b89ca;
}

QStatusBar,QMenuBar{
color:#ffffff;
}

QLabel{
color:#ffffff;
}

QProgressBar {
    border-radius: 5px;
    text-align: center;
}

QProgressBar::chunk {
    width: 2px;
    margin: 0.5px;
    background-color: #1B89CA;
}


QToolBox::pane{
    border:none;
}

QToolBox::tab {
     border:1px solid #1b89ca;
     border-radius:2px; 
     margin-right:5px;
     min-width: 100px;
     padding: 2px;
 }
QToolBox::tab:selected{
    background:#1b89ca;
}
QToolBox::tab:!selected{
    margin-top:5px;
}

#local_symbol_zn{
color:#00c1c1
}


QTableCornerButton::section,QHeaderView::section{
background:#004687;
color:#ffffff;
}


QComboBox,QLineEdit,QDoubleSpinBox,QSpinBox{
    color:#ffffff;
    border:1px solid #1b89ca;
    border-radius:5px;
    padding:5px
}


#symbol{
color:#1b89ca;
}

QListWidget::item{
margin:10px
}

QListWidget#search_list{
background:#3C3F41;
color:#1b89ca
}

""" + scroll_bar
