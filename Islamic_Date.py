from bs4 import BeautifulSoup
import requests
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLCDNumber, QLabel
import sys
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, QTime, QTimer


page = requests.get('https://news.dawateislami.net/')
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
data = soup.find(class_='noori')
# print(data)
date = str(data)
mahina = data.find().get_text()

# print(date, type(date))
count = 1
tareekh = date[85]
saal = date[137:143].lstrip().rstrip()
if date[174] == ">":
    saal_title = date[175:179]
else:
    saal_title = date[174:178]
if date[86] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
    tareekh = tareekh + date[86]

# print(tareekh)
# print(mahina)
# print(saal)
# print(saal_title)


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.setGeometry(939, 57, 400, 200)
        self.setWindowTitle("Islamic Date")
        self.setWindowIcon(QIcon("masjid.ico"))
        self.setStyleSheet("background-color:green")

        timer = QTimer()
        timer.timeout.connect(self.lcd_number)

        timer.start(1000)
        self.lcd_number()

    def lcd_number(self):
        global tareekh
        global saal
        global saal_title
        global mahina
        vbox = QVBoxLayout()

        lcd = QLabel("\t" + tareekh)

        vbox.addWidget(lcd)
        label = QLabel("   " + mahina)
        label.setStyleSheet('background-color:pink')
        label.setFont(QFont("Sanserif", 22))

        vbox.addWidget(label)

        hbox = QHBoxLayout()

        label2 = QLabel("      " + saal + "  " + saal_title )
        label2.setStyleSheet('background-color:yellow')
        label2.setFont(QFont("Sanserif", 19))

        hbox.addWidget(label2)
        vbox.addLayout(hbox)
        lcd.setStyleSheet('background-color:white')
        lcd.setFont(QFont("Sanserif", 48))



        self.setLayout(vbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
