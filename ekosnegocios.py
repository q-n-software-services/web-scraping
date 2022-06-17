import pandas as pd

import json
import requests
import csv




from bs4 import BeautifulSoup

from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QToolButton, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel,QLineEdit
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtDesigner import QDesignerFormEditorInterface
from PyQt5 import QtCore
from PyQt5.QtGui import QFont

def make_request(url):
    res = requests.get(url)
    json_response = json.loads(page_response, strict=False)
    return json_response

def extract_data(data):
    rankings = data['result']['ranking']
    return rankings

def save_data(rankings, name):
    csvFile = open(name, 'w')
    try:
        writer = csv.writer(csvFile)
        #columns names
        writer.writerow(('Sr','Ranking','Business', 'Total Revenue','Gross Profit' , 'Tax Caused' , 'Utility/Income'))
        for i in range(0,len(rankings)):
            print(i+1 ,rankings[i]['position'] ,rankings[i]['empresa'],rankings[i]['ventas'],rankings[i]['utilidad'],rankings[i]['impuestos'],rankings[i]['percent'])
            writer.writerow((i+1 ,rankings[i]['position'] ,rankings[i]['empresa'],rankings[i]['ventas'],rankings[i]['utilidad'],rankings[i]['impuestos'],rankings[i]['percent']))

    except Exception as e:
        print(e)

    finally:
        csvFile.close()



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
        # self.lineEdit = QLineEdit(form)
        # self.lineEdit.setObjectName("lineEdit")
        self.label2 = QLabel(form)
        self.lineEdit2 = QLineEdit(form)
        self.lineEdit2.setObjectName("lineEdit2")
        # self.horizontalLayout.addWidget(self.lineEdit)
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
        form.setWindowTitle(_translate("Form", "Q N S S"))
        form.setStyleSheet("background-color:Cyan")
        self.LabelName.setText(_translate("Form", "     \t \tWeb Scraper"))
        self.LabelName.setFont(QFont("Sanserif", 48))
        self.label2.setText(_translate("Form", "Name of CSV file"))
        self.label2.setFont(QFont("Sanserif", 18))
        # self.lineEdit.setStyleSheet("background-color:White")
        self.lineEdit2.setStyleSheet("background-color:White")
        self.pushButton.setText(_translate("Form", "PROCEED"))
        self.pushButton.setGeometry(172, 100, 66, 36)
        self.pushButton.setStyleSheet("background-color:magenta")
        self.pushButton.setFont(QFont("Sanserif", 18))
        self.labelResult.setText(_translate("Form", "TextLabel"))




    def click_btn(self):
        global url

        name = self.lineEdit2.text().lstrip().rstrip()
        self.labelResult.setText(name)
        name = name + ".csv"
        # name = input(" Enter a name for the csv file CATION:  donot add .csv word extension in the name we will add it for you")

        json_response = make_request('https://www.ekosnegocios.com/ranking-empresarial')
        rankings = extract_data(json_response)
        save_data(rankings, name)



if __name__ == "__main__":
    import sys
    myapp = QApplication(sys.argv)
    faram = QWidget()
    ui = ui_form()
    ui.setupUi(faram)
    faram.show()
    sys.exit(myapp.exec_())
