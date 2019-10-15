from PySide2.QtGui import QFont
import Qsci


class CodeWidget(Qsci.QsciScintilla):

    def __init__(self):
        super().__init__()

        self.setEolMode(self.SC_EOL_LF)  # 以\n换行
        self.setWrapMode(self.WrapWord)  # 自动换行。self.WrapWord是父类QsciScintilla的
        self.setAutoCompletionSource(self.AcsAll)  # 自动补全。对于所有Ascii字符
        self.setAutoCompletionCaseSensitivity(False)  # 自动补全大小写敏感
        self.setAutoCompletionThreshold(1)  # 输入多少个字符才弹出补全提示
        self.setFolding(True)  # 代码可折叠
        self.setFont(QFont('Consolas', 12))  # 设置默认字体
        # self.setMarginType(0, self.NumberMargin)    # 0~4。第0个左边栏显示行号
        # self.setMarginLineNumbers(0, True)  # 我也不知道
        # self.setMarginsBackgroundColor(QtGui.QColor(120, 220, 180))  # 边栏背景颜色
        # self.setMarginWidth(0, 30)  # 边栏宽度
        self.setAutoIndent(True)  # 换行后自动缩进
        self.setUtf8(True)  # 支持中文字符
