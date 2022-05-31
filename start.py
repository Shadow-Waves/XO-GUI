from functools import partial
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton,QComboBox,QGroupBox,QVBoxLayout,QLineEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from sys import argv
from xo import XO

class Start(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("XO")
        self.setFixedSize(250,300)
        self.setWindowIcon(QIcon("x.png"))
        
        self.symbols = ["x","o"]
        
        self.main_window = QGroupBox()
        self.main_window_layout = QVBoxLayout()
        self.main_window_layout.setSpacing(20)
        
        self.player1_name = QLineEdit(self)
        self.player1_name.setPlaceholderText("Player 1")
        self.player1_choice = QComboBox(self)
        self.player1_choice.addItems(self.symbols)
        self.player1_choice.currentIndexChanged.connect(partial(self.mutate))
        self.main_window_layout.addWidget(self.player1_name,Qt.AlignmentFlag.AlignCenter)
        self.main_window_layout.addWidget(self.player1_choice,Qt.AlignmentFlag.AlignCenter)
        
        self.player2_name = QLineEdit(self)
        self.player2_name.setPlaceholderText("Player 2")
        self.player2_choice = QComboBox(self)
        self.player2_choice.addItems(self.symbols)
        self.player2_choice.setCurrentIndex(1)
        self.player2_choice.setEnabled(False)
        self.main_window_layout.addWidget(self.player2_name,Qt.AlignmentFlag.AlignCenter)
        self.main_window_layout.addWidget(self.player2_choice,Qt.AlignmentFlag.AlignCenter)
        
        self.play = QPushButton("PLAY",self)
        self.play.clicked.connect(partial(self.play_func))
        self.main_window_layout.addWidget(self.play,Qt.AlignmentFlag.AlignCenter)
        
        self.main_window.setLayout(self.main_window_layout)
        
        self.setCentralWidget(self.main_window)
        
        self.show()
        
    def mutate(self,e):
        self.player2_choice.setCurrentIndex(1 - self.player1_choice.currentIndex())
        
    def play_func(self):
        if self.player1_name.text() and self.player2_name.text():
            self.game = XO(player1 = [self.player1_name.text(),self.player1_choice.currentText()],player2 = [self.player2_name.text(),self.player2_choice.currentText()])
            self.close()
        
if __name__ == "__main__":
    application = QApplication(argv)
    start = Start()
    application.exec()