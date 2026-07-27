# Stopwatch program
import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QMainWindow, QLabel, QPushButton)
from PyQt5.QtGui import (QPixmap, QIcon, QFont)
from PyQt5.QtCore import (Qt, QTimer)
import time, datetime

class Stopwatch_program (QMainWindow):
    def __init__(self):
        super().__init__()
        self.Window_sys()
    def Window_sys(self):
        self.setGeometry(750, 350, 600, 600)
        self.prgram_Name = self.setWindowTitle("Stopwatch program")
        self.Icone = self.setWindowIcon(QIcon("timer.png"))
        self.back_ground_lable = QLabel(self)
        self.pixmap = QPixmap("Back_ground.png")
        self.back_ground_lable.setPixmap(self.pixmap)
        self.back_ground_lable.setScaledContents(True)
        self.back_ground_lable.setGeometry(0, 0, self.width(), self.height())
        self.Counter = 0
        self.Click_count = 0
        self.Index1 = 0
        self.Index2 = 1
        self.Index3 = 2
        self.Index4 = 3
        self.Index5 = 4
        self.Counter_Lap = 150
        self.Marks = []
        self.Lap1 = QLabel(self)
        self.Lap1.setStyleSheet("color: #2cc4f2;"
                               "font: 18px;")
        self.Lap2 = QLabel(self)
        self.Lap2.setStyleSheet("color: #2cc4f2;"
                               "font: 18px;")
        self.Lap3 = QLabel(self)
        self.Lap3.setStyleSheet("color: #2cc4f2;"
                               "font: 18px;")
        self.Lap4 = QLabel(self)
        self.Lap4.setStyleSheet("color: #2cc4f2;"
                               "font: 18px;")
        self.Lap5 = QLabel(self)
        self.Lap5.setStyleSheet("color: #2cc4f2;"
                               "font: 18px;")
        self.Start_page()

    def Start_page(self):
        self.program_title = QLabel("-- Stopwatch program --", self)
        self.By_AXR = QLabel("-- By Axirise --", self)
        self.program_title.setGeometry(190, 50, 250, 50)
        self.By_AXR.setGeometry(260, 80, 100, 50)
        self.program_title.setStyleSheet("color: #2cc4f2;"
                                        "font: 20px;")
        self.By_AXR.setStyleSheet("color: #2cc4f2;"
                                        "font: 15px;")
        self.Start = QPushButton("start",self)
        self.Start.setGeometry(260, 500, 100, 50)
        self.Start.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.Start.clicked.connect(self.Secound_page)

    def Secound_page(self):
        self.By_AXR.hide()
        self.Start.hide()
        self.Stopwatch_counter = QLabel("00 : 00 : 00", self)
        self.Stopwatch_counter.setGeometry(220, 100, 250, 50)
        self.Stopwatch_counter.setStyleSheet("color: #2cc4f2;"
                                             "font: 30px;")
        self.Go = QPushButton("Go",self)
        self.Go.setGeometry(260, 500, 100, 50)
        self.Go.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.Go.clicked.connect(self.Go_clicked)
        self.Reset = QPushButton("Reset",self)
        self.Reset.setGeometry(400, 500, 100, 50)
        self.Reset.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.Go.clicked.connect(self.Go_clicked)
        self.Reset.clicked.connect(self.Reset_clicked)
        self.Time_up = QTimer(self)
        self.Time_up.timeout.connect(self.count_up)
        self.Stopwatch_counter.show()
        self.Go.show()

    def Go_clicked(self):
        self.Go.hide()
        self.Stop = QPushButton("Stop",self)
        self.Mark = QPushButton("Mark",self)
        self.Stop.setGeometry(260, 500, 100, 50)
        self.Stop.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.Stop.clicked.connect(self.Stop_clicked)
        self.Mark.setGeometry(100, 500, 100, 50)
        self.Mark.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.Mark.clicked.connect(self.Mark_clicked)
        self.Reset.show()
        self.Stop.show()
        self.Mark.show()
        self.Time_up.start(1000)

    def count_up(self):
        self.Counter += 1
        self.Secounds = self.Counter % 60
        self.Meniuts =  int(self.Counter / 60) % 60
        self.Hours =  int(self.Counter / 3600)
        self.Stopwatch_counter.setText(f"{self.Hours:02} : {self.Meniuts:02} : {self.Secounds:02}")

    def Stop_clicked(self):
        self.Stop.hide()
        self.Time_up.stop()
        self.Ready = QPushButton("Ready", self)
        self.Ready.setGeometry(260, 500, 100, 50)
        self.Ready.setStyleSheet("Background-color: #2cc4f2;"
                                 "font: 20px;"
                                 "border-radius: 25px;")
        self.Ready.clicked.connect(self.Go_clicked)
        self.Ready.show()

    def Mark_clicked(self):
        self.Click_count += 1
        self.Round = self.Click_count % 5 
        self.Marks.append([f"{self.Hours:02}", f"{self.Meniuts:02}", f"{self.Secounds:02}" ])
        if self.Round == 1:
            self.Lap1.setText(f"{self.Marks[self.Index1]}")
            self.Lap1.setGeometry(240, 150 , 150, 50)
            self.Lap1.show()
            self.Lap2.hide()
            self.Lap3.hide()
            self.Lap4.hide()
            self.Lap5.hide()
        elif self.Round == 2:
            self.Lap2.setText(f"{self.Marks[self.Index2]}")
            self.Lap2.setGeometry(240, 170 , 150, 50)
            self.Lap2.show()
        elif self.Round == 3:
            self.Lap3.setText(f"{self.Marks[self.Index3]}")
            self.Lap3.setGeometry(240, 190 , 150, 50)
            self.Lap3.show()
        elif self.Round == 4:
            self.Lap4.setText(f"{self.Marks[self.Index4]}")
            self.Lap4.setGeometry(240, 210 , 150, 50)
            self.Lap4.show()
        elif self.Round == 0:
            self.Lap5.setText(f"{self.Marks[self.Index5]}")
            self.Lap5.setGeometry(240, 230 , 150, 50)
            self.Index1 += 5
            self.Index2 += 5
            self.Index3 += 5
            self.Index4 += 5
            self.Index5 += 5
            self.Lap5.show()

    def Reset_clicked(self):
        self.Counter = 0
        self.Stopwatch_counter.setText("00 : 00 : 00")
        self.Time_up.stop()
        self.Stop.hide()
        self.Marks.clear()
        self.Click_count = 0
        self.Lap1.hide()
        self.Lap2.hide()
        self.Lap3.hide()
        self.Lap4.hide()
        self.Lap5.hide()

def main():
    app = QApplication(sys.argv)
    windwo = Stopwatch_program()
    windwo.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()