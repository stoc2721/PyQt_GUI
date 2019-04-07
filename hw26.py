# Status Bar
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusBar().showMessage('Ready')
        self.setGeometry(300,300,450,150)
        self.setWindowTitle('Status Bar')
        self.show()
#app = QApplication(sys.argv)
#ex=Example()
#sys.exit(app.exec_())


# Simple Menu
from PyQt5.QtWidgets import QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        exitAct=QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Cntrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        
        self.statusBar()
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Simple menu')
        self.show()
#app=QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())

# SubMenu        
        
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('File')
        
        impMenu=QMenu('Import',self)
        impAct=QAction('Import mail',self)
        impMenu.addAction(impAct)
        
        newAct=QAction('New',self)
        
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Submenu')
        self.show()
#app=QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())
        
        
# Check Menu
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.statusbar=self.statusBar()
        self.statusbar.showMessage('Ready')
        menubar=self.menuBar()
        viewMenu=menubar.addMenu('View')
        
        
        viewStatAct=QAction('View statusbar',self,checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        
        viewMenu.addAction(viewStatAct)
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Check menu')
        self.show()
        
    def toggleMenu(self,state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
#app=QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())          
        
        
# ContextMenu
            
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,400,200)
        self.setWindowTitle('Context Menu')
        self.show()
        
    def contextMenuEvent(self,event):
        cmenu=QMenu(self)
        newAct=cmenu.addAction("New")
        opnAct=cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        
        if action == quitAct:
            qApp.quit()
#app=QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())
    
# Toolbar        
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self): 
        exitAct=QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Cntrl+Q')
        exit.triggered.connect(qApp.quit)
        
        self.toolbar=self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(300,300,400,200)
        self.setWindowTitle('Toolbar')
        self.show()

#app=QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())        
            
        
        
        
class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self): 
        textEdit=QTextEdit()
        self.setCentralWidget(textEdit)
        
        exitAct=QAction(QIcon('exit.png'),'Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        
        self.statusBar()
        
        menubar=self.menuBar()
        fileMenu=menubar.addMenu('File')
        fileMenu.addAction(exitAct)
        
        toolbar=self.addToolBar('Exit')
        toolbar.addAction(exitAct)
        
        self.setGeometry(300,300,400,250)
        self.setWindowTitle('Main Window')
        self.show()
#app=QApplication(sys.argv)
#ex = Example()
#sys.exit(app.exec_())

