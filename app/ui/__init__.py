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

sign_in_qss = """
QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}

QTabWidget::pane{
    border:1px solid #1b89ca;
}

QToolButton:hover{
background:#1b89ca;
}

QTabBar::tab {
     border:1px solid #1b89ca;
     border-radius:2px;
     min-width: 60px;
     padding: 2px;
 }
QTabBar::tab:selected{
    background:#1b89ca;
}
QTabBar::tab:!selected{
    margin-top:5px;
}
QComboBox,QLineEdit{
    color:#ffffff;
    border:1px solid #1b89ca;
    border-radius:5px;
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
}"""

market_qss = """
QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}

QTableWidget{
    border:none;
    background:#2B2B2B;
    color:#ffffff
}

QTableWidget:disabled{
    background:gray;
}

QTableCornerButton::section,QHeaderView::section{
color:#00c1c1;
background:#2B2B2B;
}

QComboBox{
    color:#ffffff;
    border:1px solid #1b89ca;
    border-radius:5px;
}


QPushButton{
background:#2B2B2B;
color:#ffffff;
padding:5px

}

QPushButton:hover{
    background:#1b89ca;
    color:#2B2B2B
}


""" + scroll_bar

config_qss = """QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}

QComboBox,QLineEdit,QDoubleSpinBox,QSpinBox{
    color:#ffffff;
    border:1px solid #1b89ca;
    border-radius:5px;
}

QPushButton{
background:#2B2B2B;
color:#ffffff;
padding:10px;
border-radius:5px;
border:1px solid #1b89ca;

}

QPushButton:hover{
    background:#1b89ca;
    color:#ffffff;
}

QTabWidget::pane{
    border:none;
}


QTabBar::tab {
     border:1px solid #1b89ca;
     border-radius:2px; 
     min-width: 60px;
     padding: 2px;
 }
QTabBar::tab:selected{
    background:#1b89ca;
}
QTabBar::tab:!selected{
    margin-top:5px;
}

QCheckBox{
    border-radius:5px;
}

QCheckBox::indicator:checked {
    color:#1b89ca;
 }"""

home_qss = """
QWidget,QTextEdit{
background:#2B2B2B;
color:#ffffff;
border-radius: 5px;


}
QPushButton{
    padding:10px;
    background: #2B2B2B;
    color:#ffffff;
    border-radius:5px;
    border:1px solid #1b89ca;
}

QPushButton:hover{
    background:#1b89ca;
    color:#ffffff
}

""" + scroll_bar

main_qss = """
QMainWindow{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}

#line{
background:#1b89ca;
}

QStatusBar,QMenuBar{
background:#1b89ca;
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

QToolButton{
    background:#1b89ca;
    border-radius:2px;
    padding:5px;
}

QToolButton:hover{
background:#1b8900;
}

QPushButton{
    padding:10px;
    background: #2B2B2B;
    color:#ffffff;
    border-radius:5px;
    border:1px solid #1b89ca;

    
}
QPushButton:hover{
    background:#1b89ca;
    color:#ffffff
}""" + scroll_bar

order_qss = """
QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}


QTableWidget,QTabWidget::pane{
    border:none;
}

QTableCornerButton::section,QHeaderView::section{
background:#004687;
color:#ffffff;
}

QPushButton:disabled{
    background:gray;
    color:#b6b6b6;
    border-radius:2px;
}
QComboBox,QLineEdit,QDoubleSpinBox,QSpinBox{
    color:#ffffff;
    border:1px solid #1b89ca;
    border-radius:5px;
}

QTabBar::tab {
     border:1px solid #1b89ca;
     border-radius:2px; 
     min-width: 60px;
     padding: 2px;
 }
QTabBar::tab:selected{
    background:#1b89ca;
}
QTabBar::tab:!selected{
    margin-top:5px;
}

#local_symbol_zn{
color:#00c1c1
}


QPushButton{
background:#2B2B2B;
color:#ffffff;
border:1px solid #1b89ca;
     border-radius:5px; 

}

QPushButton:hover{
    background:#1b89ca;
    color:#ffffff
}
""" + scroll_bar

kline_qss = """
QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}


QTableWidget,QTabWidget::pane{
    border:none;
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

QPushButton{
background:#2B2B2B;
color:#ffffff;
border:1px solid #1b89ca;
border-radius:5px; 

}

QPushButton:hover{
    background:#1b89ca;
    color:#ffffff
}

#symbol{
color:#1b89ca;
}
"""

strategy_qss = """
QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}

QTableCornerButton::section,QHeaderView::section{
background:#004687;
color:#ffffff;
}

QPushButton{
    padding:10px
}
QPushButton:hover{
background:#1b89ca;
}


#add_strategy_btn,#gen_strategy{
background:#2B2B2B;
color:#ffffff;
}


#add_strategy_btn:hover,#gen_strategy:hover{
background:#1b89ca;
color:#ffffff;
}
"""

log_qss = """
QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}

QListWidget::item{
margin:10px
}

QListWidget#search_list{
background:#3C3F41;
color:#1b89ca
}

""" + scroll_bar

backtrack_qss = """
QWidget{
background:#2B2B2B;
color:#ffffff;
margin:0px;
}

QPushButton{
    padding:5px
}
QPushButton:hover{
background:#1b89ca;
}

QTableCornerButton::section,QHeaderView::section{
background:#004687;
color:#ffffff;
}

QComboBox,QLineEdit,QDoubleSpinBox,QSpinBox{
    color:#ffffff;
    background:#2B2B2B;
    padding:3px;
    border:1px solid #1b89ca;
    border-radius:5px;
}

""" + scroll_bar
