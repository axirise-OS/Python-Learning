# day - 13
# PyQt5 GUI intro 
# PyQt5 labels
# PyQt5 images
# PyQt5 latouts
# CSS PyQt5
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QPushButton, QCheckBox, QRadioButton, QButtonGroup, QLineEdit)
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("My first GUI")
    self.setGeometry(700,350,500,500)
    self.setWindowIcon(QIcon("C:\\Users\\Axiri\\Developer\\Python-Learning\\day-13\\Gemini_Generated_Image_c4vbpsc4vbpsc4vb.png"))
    self.button = QPushButton("Click me", self)
    self.QcheckBox = QCheckBox("Do you like pizza?", self)
    lable = QLabel("Hello", self)
    lable.setFont(QFont("Arial", 20))
    lable.setGeometry(0,0,500,100)
    lable.setStyleSheet("background-color: red;"
                        "font-weight: bold;"
                        "font-style: italic;"
                        "text-decoration: underline;")
    lable.setAlignment(Qt.AlignTop) # Vertically Top
    lable.setAlignment(Qt.AlignBottom) # Vertically Bottom
    lable.setAlignment(Qt.AlignVCenter) # Vertically center
    lable.setAlignment(Qt.AlignLeft) # Horizontally Left
    lable.setAlignment(Qt.AlignRight) # Horizontally Right
    lable.setAlignment(Qt.AlignHCenter) # Horizontally center
    lable.setAlignment(Qt.AlignTop | Qt.AlignLeft) # top vertically and left horizontally
    lable.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # center both vertically and horizontally
    lable.setAlignment(Qt.AlignCenter) # center both vertically and horizontally
    pixmap = QPixmap("C:\\Users\\Axiri\\Developer\\Python-Learning\\day-13\\Gemini_Generated_Image_c4vbpsc4vbpsc4vb.png")
    lable2 = QLabel(self)
    lable2.setGeometry(0, 0, 250, 250)
    lable2.setPixmap(pixmap)
    lable2.setScaledContents(True) # scale the image to fit the label size
    lable2.setGeometry((self.width() - lable2.width()) // 2, (self.height() - lable2.height()) // 2, lable2.width(), lable2.height())
    self.RadioButton1 = QRadioButton("Option 1", self)
    self.RadioButton2 = QRadioButton("Option 2", self)
    self.button_group1 = QButtonGroup(self)
    self.button_group1 = QButtonGroup(self)
    self.LineEdit = QLineEdit(self)
    self.QButton = QPushButton("Submit", self)
    self.QLabel1 = QLabel("Enter your name and click Submit", self)
    self.QLabel2 = QLabel(self)
    self.initUI()
  def initUI(self):
    self.QLabel1.setGeometry(5, 10, 300, 30)
    self.QLabel1.setFont(QFont("Arial", 15))
    self.LineEdit.setGeometry(5, 50, 200, 30)
    self.LineEdit.setFont(QFont("Arial", 10))
    self.LineEdit.setPlaceholderText("Enter your name")
    self.QButton.setGeometry(205, 50, 100, 30)
    self.QButton.setFont(QFont("Arial", 10))
    self.QButton.clicked.connect(self.on_submit)
    self.QLabel2.setGeometry(5, 90, 300, 30)
    self.QLabel2.setFont(QFont("Arial", 15))
    center_widget = QWidget()
    self.setCentralWidget(center_widget)
    self.lable1 = QLabel("Label 1", self)
    self.lable3 = QLabel("Label 3", self)
    self.lable1.setStyleSheet("background-color: red;")
    self.lable2.setStyleSheet("background-color: green;")
    self.lable3.setStyleSheet("background-color: blue;")
    self.button.clicked.connect(self.clicked)
    self.QcheckBox.stateChanged.connect(self.CheckBoxstats)
    self.QcheckBox.setChecked(True)
    vox_layout = QVBoxLayout()
    vox_layout.addWidget(self.lable1)
    vox_layout.addWidget(self.lable2)
    vox_layout.addWidget(self.lable3)
    center_widget.setLayout(vox_layout)
    hbox_layout = QHBoxLayout()
    hbox_layout.addWidget(self.lable1)
    hbox_layout.addWidget(self.lable2)
    hbox_layout.addWidget(self.lable3)
    center_widget.setLayout(hbox_layout)
    grid_layout = QGridLayout()
    grid_layout.addWidget(self.lable1, 0, 0)
    grid_layout.addWidget(self.lable2, 0, 1)
    grid_layout.addWidget(self.lable3, 1, 0)
    grid_layout.addWidget(self.button, 0, 0)
    grid_layout.addWidget(self.QcheckBox, 0, 1)
    center_widget.setLayout(grid_layout)
    self.RadioButton1.setGeometry(10, 50, 100, 30)
    self.RadioButton2.setGeometry(10, 100, 100, 30)
    self.button_group1 = QButtonGroup(self)
    self.button_group1 = QButtonGroup(self)
    self.button_group1.addButton(self.RadioButton1)
    self.button_group1.addButton(self.RadioButton2)
    self.RadioButton1.toggled.connect(self.RadioButton_changed)
    self.RadioButton2.toggled.connect(self.RadioButton_changed)
  def RadioButton_changed(self):
    if self.RadioButton1.isChecked():
        print("Option 1 selected")
    elif self.RadioButton2.isChecked():
        print("Option 2 selected")
  def clicked(self):
    print("Button clicked")
    self.button.setText("Clicked")
    self.button.setDisabled(True)
    self.lable1.setText("Button clicked")
    self.lable2.setText("welcome to my GUI")
    self.lable3.setText("I like pizza")
  def CheckBoxstats(self):
    if self.QcheckBox.isChecked():
        print("You like pizza")
    else:
        print("You don't like pizza")
  def on_submit(self):
    name = self.LineEdit.text()
    if name:
         self.QLabel2.setText(f"Happy birthday, {name}!")
    else:
         self.QLabel2.setText("Please enter your name.")
def main():
   app = QApplication(sys.argv)
   window = MainWindow()
   window.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
   main()