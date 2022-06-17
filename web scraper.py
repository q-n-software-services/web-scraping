
import pandas as pd


import requests


from bs4 import BeautifulSoup

from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QToolButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtDesigner import QDesignerFormEditorInterface
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

url = " "
name = " "
class ui_form(object):

    def setupUi(self, form):
        form.setObjectName("Form")
        form.resize(2160, 700)
        form.move(1, 1)

        self.verticalLaoyut = QVBoxLayout(form)
        self.verticalLaoyut.setObjectName("VerticalLayout")
        self.horizontalLayout = QVBoxLayout(form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LabelName = QLabel(form)
        self.LabelName.setObjectName("labelName")
        self.horizontalLayout.addWidget(self.LabelName)
        self.lineEdit = QLineEdit(form)
        self.lineEdit.setObjectName("lineEdit")
        self.label2 = QLabel(form)
        self.lineEdit2 = QLineEdit(form)
        self.lineEdit2.setObjectName("lineEdit2")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.label2)
        self.horizontalLayout.addWidget(self.lineEdit2)
        self.verticalLaoyut.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QVBoxLayout()
        self.horizontalLayout_2.setObjectName("HorizontalLayout_2")
        self.labelResult = QLabel(form)
        self.labelResult.setObjectName("labelResult")
        self.labelResult.setFont(QFont("Sanserif", 48))
        self.horizontalLayout_2.addWidget(self.labelResult)
        self.pushButton = QPushButton(form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click_btn)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLaoyut.addLayout(self.horizontalLayout_2)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Q N Software Services +923471066089"))
        form.setStyleSheet("background-color:Yellow")
        self.LabelName.setText(_translate("Form", "URL / Link:"))
        self.LabelName.setFont(QFont("Sanserif", 18))
        self.label2.setText(_translate("Form", "Name of CSV file"))
        self.label2.setFont(QFont("Sanserif", 18))
        self.lineEdit.setStyleSheet("background-color:White")
        self.lineEdit2.setStyleSheet("background-color:White")
        self.pushButton.setText(_translate("Form", "PROCEED"))
        self.pushButton.setGeometry(172, 100, 66, 36)
        self.pushButton.setStyleSheet("background-color:Red")
        self.pushButton.setFont(QFont("Sanserif", 18))
        self.labelResult.setText(_translate("Form", "TextLabel"))




    def click_btn(self):
        global url
        global name

        url = self.lineEdit.text()
        name = self.lineEdit2.text()
        self.labelResult.setText(name)
        # name = input(" Enter a name for the csv file CATION:  donot add .csv word extension in the name we will add it for you")
        name = name + ".csv"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        week = soup.find(id='seven-day-forecast-body')
        # print(week)
        items = week.findAll(class_='tombstone-container')
        # print(items)
        # print(items[0].find(class_='period-name').get_text())
        # print(items[0].find(class_='short-desc').get_text())
        # print(items[0].find(class_='temp').get_text())
        period_names = [item.find(class_='period-name').get_text() for item in items]
        short_desc = [item.find(class_='short-desc').get_text() for item in items]
        temperatures = [item.find(class_='temp').get_text() for item in items]
        # print(period_names)
        # print(short_desc)
        # print(temperatures)
        weather_stuff = pd.DataFrame({
            'period': period_names,
            'short_description': short_desc,
            'temperature': temperatures,
        })
        print(weather_stuff)
        weather_stuff.to_csv(name)


if __name__ == "__main__":
    import sys
    myapp = QApplication(sys.argv)
    faram = QWidget()
    ui = ui_form()
    ui.setupUi(faram)
    faram.show()
    sys.exit(myapp.exec_())

    '''global dall
    dall = self.lineEdit.text()
    #   self.pushButton.setGeometry(100, 100, 66, 36)
    # self.verticalLaoyut.addLayout(self.horizontalLayout_2)'''


# url = input("Enter the URL of the webpage for weather forecasting")


