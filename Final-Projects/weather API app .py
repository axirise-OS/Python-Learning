# Weather API app
import sys, requests, threading
from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QPushButton, QLineEdit)
from PyQt5.QtGui import (QFont, QIcon, QPixmap)
from PyQt5.QtCore import (Qt, QTimer)
import time, datetime

class Mainwindwo(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(750, 350, 600, 600)
        self.setWindowTitle("Weather API app")
        self.setWindowIcon(QIcon("cloudy.png"))
        pixmap = QPixmap("Back_ground.png")
        self.Background_img = QLabel(self)
        self.Background_img.setPixmap(pixmap)
        self.Background_img.setGeometry(0,0,self.width(),self.height())
        self.Background_img.setScaledContents(True)
        self.title = QLabel("-- Weather API app --", self)
        self.By_AXR = QLabel("-- By Axirise --", self)
        self.info1 = QLabel(self)
        self.info2 = QLabel(self)
        self.info3 = QLabel(self)
        self.info4 = QLabel(self)
        self.info5 = QLabel(self)
        self.input_cty = QLineEdit(self)
        self.Start = QPushButton("Start", self)
        self.Search = QPushButton("Search", self)
        self.Start.clicked.connect(self.Start_Clicked)
        self.Search.clicked.connect(self.Search_Clicked)
        self.initUI()
    def initUI(self):
        self.title.setGeometry(200, 50, 250, 50)
        self.By_AXR.setGeometry(250, 80, 100, 50)
        self.input_cty.setGeometry(170, 140, 150, 50)
        self.info1.setGeometry(100, 300, 200, 50)
        self.info2.setGeometry(400, 300, 200, 50)
        self.info3.setGeometry(100, 400, 200, 50)
        self.info4.setGeometry(400, 400, 200, 50)
        self.info5.setGeometry(250, 480, 200, 50)
        self.Search.setGeometry(330, 140, 100, 50)
        self.Start.setGeometry(260, 500, 100, 50)
        self.title.setStyleSheet("color: #2cc4f2;"
                                        "font: 20px;")
        self.info1.setStyleSheet("color: #2cc4f2;"
                                        "font: 18px;")
        self.info2.setStyleSheet("color: #2cc4f2;"
                                        "font: 18px;")
        self.info3.setStyleSheet("color: #2cc4f2;"
                                        "font: 18px;")
        self.info4.setStyleSheet("color: #2cc4f2;"
                                        "font: 18px;")
        self.info5.setStyleSheet("color: #2cc4f2;"
                                        "font: 18px;")
        self.By_AXR.setStyleSheet("color: #2cc4f2;"
                                        "font: 15px;")
        self.input_cty.setStyleSheet("border-radius: 25px;"
                                     "font: 15px;"
                                     "Background-color: #2cc4f2;")
        self.input_cty.setPlaceholderText("Enter Cty name")
        self.Start.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.Search.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.input_cty.hide()
        self.info1.hide()
        self.info2.hide()
        self.info3.hide()
        self.info4.hide()
        self.info5.hide()
        self.Search.hide()
        self.Start.show()

    def Cheack_conect(self, Cty_find):
        self.key ="01a4dfd009f1425c8b0181122262707"
        self.URl = f"https://api.weatherapi.com/v1/current.json?key={self.key}&q={Cty_find}"
        self.response = requests.get(self.URl)
        if self.response.status_code == 200:
            print("Request Accepted")
            self.data = self.response.json()
            return self.data
        else:
            print(self.response.status_code)

    def Start_Clicked(self):
        self.By_AXR.hide()
        self.Start.hide()
        self.input_cty.show()
        self.Search.show()

    def Search_Clicked(self):
        self.Cty_find = self.input_cty.text()
        self.data_info = self.Cheack_conect(self.Cty_find)
        print(self.data_info)
        self.info1.setText(f"Name: {self.data_info['location']['name']}")
        self.info2.setText(f"Country: {self.data_info['location']['country']}")
        self.info3.setText(f"Wind_kph: {self.data_info['current']['wind_kph']}")
        self.info4.setText(f"Temp/c: {self.data_info['current']['temp_c']}")
        self.info5.setText(f"Feelslike: {self.data_info['current']['feelslike_c']}")
        self.info1.show()
        self.info2.show()
        self.info3.show()
        self.info4.show()
        self.info5.show()

def main():
    app = QApplication(sys.argv)
    windwo = Mainwindwo()
    windwo.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()