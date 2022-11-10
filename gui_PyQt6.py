import numpy as np
from gui_ml_model_function import predict_y
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QTextEdit, QLineEdit
from PyQt6.QtGui import QDoubleValidator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.inputsArray = []

        # CENTER LAYOUT
        centerLayout = QVBoxLayout()
        self.setLayout(centerLayout)

        # WINDOW SETTINGS
        self.setWindowTitle("AI Program")
        # self.setFixedSize(QSize(350,800))

        # LAYOUTS
        HLayout = QHBoxLayout()
        HLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        col1 = QVBoxLayout()
        col1.setAlignment(Qt.AlignmentFlag.AlignTop)
        col2 = QVBoxLayout()
        col2.setAlignment(Qt.AlignmentFlag.AlignTop)

        # TITLE
        title = QLabel("PARKINSON PROJECT")
        font = title.font()
        font.setPointSize(25)
        font.setBold(True)
        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        centerLayout.addWidget(title)

        # LABELS AND TEXT EDITS
        label1 = QLabel("MDVP:Fo(Hz):")
        self.edittext1 = QLineEdit()
        self.edittext1.setValidator(QDoubleValidator())
        self.edittext1.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext1)
        col1.addWidget(label1)
        col1.addWidget(self.edittext1)

        label2 = QLabel("MDVP:Fhi(Hz):")
        self.edittext2 = QLineEdit()
        self.edittext2.setValidator(QDoubleValidator())
        self.edittext2.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext2)
        col1.addWidget(label2)
        col1.addWidget(self.edittext2)

        label3 = QLabel("MDVP:Flo(Hz):")
        self.edittext3 = QLineEdit()
        self.edittext3.setValidator(QDoubleValidator())
        self.edittext3.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext3)
        col1.addWidget(label3)
        col1.addWidget(self.edittext3)

        label4 = QLabel("MDVP:Jitter(%):")
        self.edittext4 = QLineEdit()
        self.edittext4.setValidator(QDoubleValidator())
        self.edittext4.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext4)
        col1.addWidget(label4)
        col1.addWidget(self.edittext4)

        label5 = QLabel("MDVP:Jitter(Abs):")
        self.edittext5 = QLineEdit()
        self.edittext5.setValidator(QDoubleValidator())
        self.edittext5.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext5)
        col1.addWidget(label5)
        col1.addWidget(self.edittext5)

        label6 = QLabel("MDVP:RAP:")
        self.edittext6 = QLineEdit()
        self.edittext6.setValidator(QDoubleValidator())
        self.edittext6.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext6)
        col1.addWidget(label6)
        col1.addWidget(self.edittext6)

        label7 = QLabel("MDVP:PPQ:")
        self.edittext7 = QLineEdit()
        self.edittext7.setValidator(QDoubleValidator())
        self.edittext7.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext7)
        col1.addWidget(label7)
        col1.addWidget(self.edittext7)

        label8 = QLabel("Jitter:DDP:")
        self.edittext8 = QLineEdit()
        self.edittext8.setValidator(QDoubleValidator())
        self.edittext8.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext8)
        col1.addWidget(label8)
        col1.addWidget(self.edittext8)

        label9 = QLabel("MDVP:Shimmer:")
        self.edittext9 = QLineEdit()
        self.edittext9.setValidator(QDoubleValidator())
        self.edittext9.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext9)
        col1.addWidget(label9)
        col1.addWidget(self.edittext9)

        label10 = QLabel("MDVP:Shimmer(dB):")
        self.edittext10 = QLineEdit()
        self.edittext10.setValidator(QDoubleValidator())
        self.edittext10.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext10)
        col1.addWidget(label10)
        col1.addWidget(self.edittext10)

        label11 = QLabel("Shimmer:APQ3:")
        self.edittext11 = QLineEdit()
        self.edittext11.setValidator(QDoubleValidator())
        self.edittext11.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext11)
        col1.addWidget(label11)
        col1.addWidget(self.edittext11)

        label12 = QLabel("Shimmer:APQ5:")
        self.edittext12 = QLineEdit()
        self.edittext12.setValidator(QDoubleValidator())
        self.edittext12.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext12)
        col2.addWidget(label12)
        col2.addWidget(self.edittext12)

        label13 = QLabel("MDVP:APQ:")
        self.edittext13 = QLineEdit()
        self.edittext13.setValidator(QDoubleValidator())
        self.edittext13.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext13)
        col2.addWidget(label13)
        col2.addWidget(self.edittext13)

        label14 = QLabel("Shimmer:DDA:")
        self.edittext14 = QLineEdit()
        self.edittext14.setValidator(QDoubleValidator())
        self.edittext14.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext14)
        col2.addWidget(label14)
        col2.addWidget(self.edittext14)

        label15 = QLabel("NHR:")
        self.edittext15 = QLineEdit()
        self.edittext15.setValidator(QDoubleValidator())
        self.edittext15.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext15)
        col2.addWidget(label15)
        col2.addWidget(self.edittext15)

        label16 = QLabel("HNR:")
        self.edittext16 = QLineEdit()
        self.edittext16.setValidator(QDoubleValidator())
        self.edittext16.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext16)
        col2.addWidget(label16)
        col2.addWidget(self.edittext16)

        label17 = QLabel("RPDE:")
        self.edittext17 = QLineEdit()
        self.edittext17.setValidator(QDoubleValidator())
        self.edittext17.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext17)
        col2.addWidget(label17)
        col2.addWidget(self.edittext17)

        label18 = QLabel("DFA:")
        self.edittext18 = QLineEdit()
        self.edittext18.setValidator(QDoubleValidator())
        self.edittext18.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext18)
        col2.addWidget(label18)
        col2.addWidget(self.edittext18)

        label19 = QLabel("spread1:")
        self.edittext19 = QLineEdit()
        self.edittext19.setValidator(QDoubleValidator())
        self.edittext19.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext19)
        col2.addWidget(label19)
        col2.addWidget(self.edittext19)

        label20 = QLabel("spread2:")
        self.edittext20 = QLineEdit()
        self.edittext20.setValidator(QDoubleValidator())
        self.edittext20.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext20)
        col2.addWidget(label20)
        col2.addWidget(self.edittext20)

        label21 = QLabel("D2:")
        self.edittext21 = QLineEdit()
        self.edittext21.setValidator(QDoubleValidator())
        self.edittext21.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext21)
        col2.addWidget(label21)
        col2.addWidget(self.edittext21)

        label22 = QLabel("PPE:")
        self.edittext22 = QLineEdit()
        self.edittext22.setValidator(QDoubleValidator())
        self.edittext22.setFixedSize(QSize(150, 25))
        self.inputsArray.append(self.edittext22)
        col2.addWidget(label22)
        col2.addWidget(self.edittext22)


        self.answerButton = QPushButton("Get Answer")
        self.answerButton.clicked.connect(self.getAnswerFunc)
        self.answerButton.setFixedHeight(50)
        self.answerButton.setFixedHeight(50)

        self.answer = QLineEdit("ANSWER".upper())
        self.answer.setFixedHeight(40)
        self.answer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.answer.setDisabled(True)
        


        centerLayout.addLayout(HLayout)
        HLayout.addLayout(col1)
        HLayout.addLayout(col2)
        centerLayout.addWidget(self.answerButton)
        centerLayout.addWidget(self.answer)

        widget = QWidget()
        widget.setLayout(centerLayout)
        self.setCentralWidget(widget)

    def getAnswerFunc(self):
        allInputsFull = True
        inputsValues = []

        for input in self.inputsArray:
            if input.text() == "":
                allInputsFull = False
                break
            inputsValues.append(input.text())

        if allInputsFull == True:
            vals = np.array(inputsValues)
            vals = np.expand_dims(vals, axis=0)

            pred = predict_y(vals)
            if pred == 1:
                self.answer.setText('Parkinson: Positive')
            else:
                self.answer.setText('Parkinson: Negative')

app = QApplication([])

window = MainWindow()
window.show()

app.exec()