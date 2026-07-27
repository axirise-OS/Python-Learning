# Digital Clock program
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLayout, QPushButton, QLineEdit )
from PyQt5.QtGui import (QPixmap, QIcon, QFont)
from PyQt5.QtCore import (Qt, QTimer)
import time, datetime

class Digital_Clock_program(QMainWindow):
    icon_program = "Digital-clock.png"
    def __init__(self):
        super().__init__()
        self.Title = self.setWindowTitle("Digital Clock program")
        self.Icon =self.setWindowIcon(QIcon(self.icon_program))
        self.count = 0
        self.pixmap = QPixmap("Back_ground.png")
        self.Background = QLabel(self)
        self.program_Title = QLabel("-- Digital Clock program ⏱ --",self)
        self.By_AXR = QLabel("-- By Axirise --",self)
        self.Hours = QLabel("Hours",self)
        self.mint = QLabel("Menuets",self)
        self.Background.setPixmap(self.pixmap)
        self.Clock = QLabel(self)
        self.Alarm_seted = QLabel(self)
        self.timer = QTimer(self)
        self.timer2 = QTimer(self)
        self.Start = QPushButton("start", self)
        self.Start2 = QPushButton("start", self)
        self.Alarm = QPushButton("Alarm", self)
        self.theam = QPushButton("", self)
        self.Stop = QPushButton("Stop", self)
        self.Timer = QPushButton("Timer", self)
        self.Set_time = QPushButton("set time", self)
        self.Add_hor = QLineEdit(self)
        self.Add_mim = QLineEdit(self)
        self.Hor = 0
        self.Min = 0
        self.Counter = 0
        self.initUI()
    def initUI(self):
        self.setGeometry(700, 350, 500, 500)
        self.program_Title.setGeometry(120, 50, 300, 100)
        self.By_AXR.setGeometry(200, 100, 100, 50)
        self.Background.setGeometry(0,0, self.width(), self.height())
        self.Background.setScaledContents(True)
        self.timer.timeout.connect(self.Time_update)
        self.timer2.timeout.connect(self.Time_update2)
        self.Start.setGeometry(200, 400, 100, 50)
        self.Start2.setGeometry(200, 400, 100, 50)
        self.Start.setStyleSheet("background-color: #58eded;"
                                 "border-radius: 25px")
        self.Alarm.setStyleSheet("background-color: #58eded;"
                                 "border-radius: 25px")
        self.theam.setStyleSheet("background-color: red;"
                                 "border-radius: 25px")
        self.Stop.setStyleSheet("background-color: #58eded;"
                                 "border-radius: 25px")
        self.Start2.setStyleSheet("background-color: #58eded;"
                                 "border-radius: 25px")
        self.Set_time.setStyleSheet("background-color: #58eded;"
                                 "border-radius: 25px")
        self.Timer.setStyleSheet("background-color: #58eded;"
                                 "border-radius: 25px")
        self.Add_hor.setStyleSheet("background-color: #58eded;"
                                   "color: black;"
                                 "border-radius: 25px")
        self.Add_mim.setStyleSheet("background-color: #58eded;"
                                   "color: black;"
                                 "border-radius: 25px")
        self.Alarm_seted.setStyleSheet("color: #5bf0c3;")
        self.Clock.setStyleSheet("color: #58eded;")
        self.program_Title.setStyleSheet("color: #58eded;" "font: 20px")
        self.By_AXR.setStyleSheet("color: #58eded;" "font: 15px")
        self.Hours.setStyleSheet("color: #58eded;")
        self.mint.setStyleSheet("color: #58eded;")
        self.Start.clicked.connect(self.Start_Clicked)
        self.Stop.clicked.connect(self.Timer_stoped)
        self.Start2.clicked.connect(self.Start2_Clicked)
        self.theam.clicked.connect(self.theam_Clicked)
        self.Alarm.clicked.connect(self.Alarm_Clicked)
        self.Set_time.clicked.connect(self.Alarm_set)
        self.Timer.clicked.connect(self.Timer_Clicked)
        self.Alarm.setGeometry(200, 400, 100, 50)
        self.theam.setGeometry(400, 400, 50, 50)
        self.Stop.setGeometry(200, 400, 100, 50)
        self.Alarm_seted.setGeometry(180, 120, 300, 50)
        self.Set_time.setGeometry(200, 400, 100, 50)
        self.Timer.setGeometry(60, 400, 100, 50)
        self.Alarm.hide()
        self.theam.hide()
        self.Stop.hide()
        self.Start2.hide()
        self.Alarm_seted.hide()
        self.Timer.hide()
        self.Add_hor.hide()
        self.Add_mim.hide()
        self.Set_time.hide()
        self.mint.hide()
        self.Hours.hide()
    def Time_update(self):
        self.now = datetime.datetime.now()
        self.now = self.now.strftime("%H : %M : %S")
        self.Clock.setText(self.now)        
        print(self.now)
        if self.now[0:2] == self.Hor and self.now[5:7] == self.Min  :
            self.Alarm_seted.setText("       Wake up")
            print("wake up")
        elif int(self.now[0:2]) == int(self.Hor) and  int(self.now[5:7]) < int(self.Min) :
            self.Alarm_seted.setText(F"Alarm set at: {self.Hor} : {self.Min}")
        elif int(self.now[0:2]) == int(self.Hor) and int(self.now[5:7]) > int(self.Min) :
            self.Alarm_seted.setText("")
    def Time_update2(self):  
         self.Counter += 1 
         Secound = self.Counter % 60
         minutes = int(self.Counter / 60) % 60
         hours = int(self.Counter / 3600)
         self.Clock.setText(f"{hours:02} : {minutes:02} : {Secound:02}")
    def Start_Clicked(self):
        self.Start.hide()
        self.program_Title.hide()
        self.By_AXR.hide()
        self.Stop.hide()
        self.Start2.hide()
        self.timer2.stop()
        self.theam.show()
        self.Alarm.show()
        self.Alarm_seted.show()
        self.Timer.show()
        self.Clock.setGeometry(170, 80, 300, 50)
        self.Clock.setFont(QFont("Arial", 20))
        self.Counter = 0
        self.timer.start(1000)

    def Alarm_Clicked(self):
        self.timer.stop()
        self.Clock.hide()
        self.Alarm.hide()
        self.theam.hide()
        self.Alarm_seted.hide()
        self.Timer.hide()
        self.Set_time.show()
        self.Hours.show()
        self.mint.show()
        self.Add_hor.setGeometry(180, 100, 50, 50)
        self.Hours.setGeometry(180, 50, 60, 50)
        self.Add_hor.setText(self.now[0:2])
        self.Add_mim.setGeometry(280, 100, 50, 50)
        self.mint.setGeometry(280, 50, 60, 50)
        self.Add_mim.setText(self.now[5:7])
        self.Add_hor.show()
        self.Add_mim.show()

    def theam_Clicked(self):
        print(f"Theam: {(self.count % 3) + 1}")
        if self.count % 3 == 0:
            self.Start.setStyleSheet("background-color: red;"
                                    "border-radius: 25px")
            self.Alarm.setStyleSheet("background-color: red;"
                                    "border-radius: 25px")
            self.theam.setStyleSheet("background-color: gray;"
                                    "border-radius: 25px")
            self.Stop.setStyleSheet("background-color: red;"
                                    "border-radius: 25px")
            self.Start2.setStyleSheet("background-color: red;"
                                    "border-radius: 25px")
            self.Set_time.setStyleSheet("background-color: red;"
                                    "border-radius: 25px")
            self.Timer.setStyleSheet("background-color: red;"
                                    "border-radius: 25px")
            self.Add_hor.setStyleSheet("background-color: red;"
                                    "color: black;"
                                    "border-radius: 25px")
            self.Add_mim.setStyleSheet("background-color: red;"
                                    "color: black;"
                                    "border-radius: 25px")
            self.Clock.setStyleSheet("color: red;")
            self.Alarm_seted.setStyleSheet("color: red;")
            self.Hours.setStyleSheet("color: red;")
            self.mint.setStyleSheet("color: red;")
            self.count += 1
        elif self.count % 3 == 1:
            self.Start.setStyleSheet("background-color: gray;"
                                    "border-radius: 25px")
            self.Alarm.setStyleSheet("background-color: gray;"
                                    "border-radius: 25px")
            self.theam.setStyleSheet("background-color: #58eded;"
                                    "border-radius: 25px")
            self.Stop.setStyleSheet("background-color: gray;"
                                    "border-radius: 25px")
            self.Start2.setStyleSheet("background-color: gray;"
                                    "border-radius: 25px")
            self.Set_time.setStyleSheet("background-color: gray;"
                                    "border-radius: 25px")
            self.Timer.setStyleSheet("background-color: gray;"
                                    "border-radius: 25px")
            self.Add_hor.setStyleSheet("background-color: gray;"
                                    "color: black;"
                                    "border-radius: 25px")
            self.Add_mim.setStyleSheet("background-color: gray;"
                                    "color: black;"
                                    "border-radius: 25px")
            self.Clock.setStyleSheet("color: gray;")
            self.Alarm_seted.setStyleSheet("color: gray;")
            self.Hours.setStyleSheet("color: gray;")
            self.mint.setStyleSheet("color: gray;")
            self.count += 1
        elif self.count % 3 == 2:
            self.Start.setStyleSheet("background-color: #58eded;"
                                    "border-radius: 25px")
            self.Alarm.setStyleSheet("background-color: #58eded;"
                                    "border-radius: 25px")
            self.theam.setStyleSheet("background-color: red;"
                                    "border-radius: 25px")
            self.Stop.setStyleSheet("background-color: #58eded;"
                                    "border-radius: 25px")
            self.Start2.setStyleSheet("background-color: #58eded;"
                                    "border-radius: 25px")
            self.Set_time.setStyleSheet("background-color: #58eded;"
                                    "border-radius: 25px")
            self.Timer.setStyleSheet("background-color: #58eded;"
                                    "border-radius: 25px")
            self.Add_hor.setStyleSheet("background-color: #58eded;"
                                    "color: black;"
                                    "border-radius: 25px")
            self.Add_mim.setStyleSheet("background-color: #58eded;"
                                    "color: black;"
                                    "border-radius: 25px")
            self.Clock.setStyleSheet("color: #58eded;")
            self.Alarm_seted.setStyleSheet("color: #58eded;")
            self.Hours.setStyleSheet("color: #58eded;")
            self.mint.setStyleSheet("color: #58eded;")
            self.count = 0
    def Alarm_set(self):
        self.Hor = self.Add_hor.text()
        self.Min = self.Add_mim.text()
        self.Alarm_seted.setFont(QFont("Arial", 10))
        self.Alarm_seted.setText(F"Alarm set at: {self.Hor} : {self.Min}")
        self.Alarm_seted.show()
        self.Add_hor.hide()
        self.mint.hide()
        self.Hours.hide()
        self.Add_mim.hide()
        self.Set_time.hide()
        self.timer.start(1000)
        self.Clock.show()
        self.theam.show()
        self.Alarm.show()
        self.Timer.show()
    def Timer_Clicked(self):
        self.timer.stop()
        self.Alarm.hide()
        self.Alarm_seted.hide()
        self.theam.hide()
        self.Timer.hide()
        self.Hours.hide()
        self.mint.hide()
        self.Stop.show()
        self.Clock.setText("00 : 00 : 00")
        self.Start.show()
        self.Start.setText("back")
        self.Start.setGeometry(60, 400, 100, 50)
        self.timer2.start(1000)
    def Start2_Clicked(self):
        self.timer.stop()
        self.Alarm.hide()
        self.Alarm_seted.hide()
        self.theam.hide()
        self.Timer.hide()
        self.Stop.show()
        self.Start.show()
        self.Start.setText("back")
        self.Start.setGeometry(60, 400, 100, 50)
        self.timer2.start(1000)
    def Timer_stoped(self):
        self.timer2.stop()
        self.Stop.hide()
        self.Alarm_seted.hide()
        self.Start.show()
        self.Start.setText("back")
        self.Start.setGeometry(60, 400, 100, 50)
        self.Start2.show()  
def Main():
    app = QApplication(sys.argv)
    Mainwindow = Digital_Clock_program()
    Mainwindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    Main()
