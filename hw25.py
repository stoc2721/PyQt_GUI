from PyQt5.QtCore import QDate, QTime, QDateTime, Qt,QTimeZone

# Date and Time Stuff

now=QDate.currentDate()
print(now)
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
print('')


# Following is the one to remember, can slice, see below
dateTime=QDateTime.currentDateTime()
print(dateTime.toString())


time=QTime.currentTime()
print(time.toString(Qt.DefaultLocaleLongDate))

print('Print the month:')
getTimeStr=dateTime.toString()
print(getTimeStr[4:7])
print('')


# days in month and year
d=QDate(1945,5,7)
print("Days in month: %s" % d.daysInMonth())
print("Days in year: %s" % d.daysInYear())

# difference in days
xmas = QDate(2018,12,24)
daysPassed=xmas.daysTo(now)
print('%s days passed since xmas' % daysPassed)


# datetime arithmetic
now = QDateTime.currentDateTime()
print('Today: %s' % now.toString(Qt.ISODate))
print('Adding 100 days: %s' % now.addDays(100).toString(Qt.ISODate))
print('Subtracting 100 days: %s' % now.addDays(-100).toString(Qt.ISODate))
print('Adding 13 seconds: %s' % now.addSecs(13).toString(Qt.ISODate))
print('Adding 12 months: %s' % now.addMonths(12).toString(Qt.ISODate))
print('Adding the sands of time: %s' % now.addYears(1000).toString(Qt.ISODate))

# daylight saving time
print('Time Zone: %s' % now.timeZoneAbbreviation())
if now.isDaylightTime():
    print('It is currently DST')
else:
    print('It is not DST')
    
'''
WINDOWS AND WIDGETS
'''

##a simple window
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QDesktopWidget)
from PyQt5.QtGui import (QIcon, QFont)

app = QApplication(sys.argv)
w=QWidget()
w.resize(350,150)
w.move(300,300)
w.setWindowTitle('Simple')
w.show()

sys.exit(app.exec_())


#application icon
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        
        self.show()
        
app=QApplication(sys.argv)
ex=Example()
sys.exit(app.exec_())

#Push button
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn=QPushButton('Button',self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        self.setGeometry(300,300,300,220)
        self.setWindowTitle('ToolTips')
        self.show()
        
app=QApplication(sys.argv)
ex=Example()
sys.exit(app.exec_())

# closing a window
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        qbtn=QPushButton('Quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)
        self.setGeometry(300,300,450,150)
        self.setWindowTitle('Quit button')
        self.show()
app=QApplication(sys.argv)
ex=Example()
sys.exit(app.exec_())

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,450,150)
        self.setWindowTitle('Message box')
        self.show()
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',"Are ya sure?",QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply==QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
app=QApplication(sys.argv)
ex=Example()
sys.exit(app.exec_())

## centering a window on a screen
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.resize(450,150)
        self.center()
        self.setWindowTitle('Center')
        self.show()
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
app=QApplication(sys.argv)
ex=Example()
sys.exit(app.exec_())
        
