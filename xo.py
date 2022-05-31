from functools import partial
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QGridLayout,QGroupBox
from PyQt6.QtGui import QPixmap,QIcon
from PyQt6.QtCore import Qt
from sys import argv
from random import shuffle

class XO(QMainWindow):
    def __init__(self,**kwargs):
        super().__init__()
        
        self.plan = kwargs
        
        self.setWindowTitle("XO")
        self.setFixedSize(640,640)
        self.setWindowIcon(QIcon("x.png"))
        
        self.colors_list = ["#9D00FF","#B1C5C2","#FF6600","#00FF00","#0062FF","#FF0099","#3500FF","#FFFE37","#EE82EE"]
        shuffle(self.colors_list)
        self.colors_list = iter(self.colors_list)
        
        self.grid = QGroupBox()
        self.grid_layout = QGridLayout()
        self.grid_matrix = []
        self.bitwise = 0
       
        for row in range(3):
            x = []
            for column in range(3):
                square = QLabel()
                square.setFixedSize(200,200)
                square.setStyleSheet(f"background-color:{next(self.colors_list)};")
                square.mousePressEvent = partial(self.replace,row,column)
                self.grid_layout.addWidget(square,row,column,Qt.AlignmentFlag.AlignCenter)
                x.append([square,False,None])
            self.grid_matrix.append(x)
                
        
        self.grid.setLayout(self.grid_layout)
        
        self.setCentralWidget(self.grid)
        
        self.endgame = 0
        
        self.counter = 0
        
        self.show()
        
    def replace(self,row,column,e):
        if not self.endgame:
            self.counter += 1
            if not self.bitwise and not self.grid_matrix[row][column][1]:
                self.grid_matrix[row][column][0].setPixmap(QPixmap("x.png").scaled(200,200))
                self.grid_matrix[row][column][1] = True
                self.grid_matrix[row][column][2] = "x"
                self.bitwise = not self.bitwise
            elif self.bitwise and not self.grid_matrix[row][column][1]:
                self.grid_matrix[row][column][0].setPixmap(QPixmap("o.png").scaled(200,200))
                self.grid_matrix[row][column][1] = True
                self.grid_matrix[row][column][2] = "o"
                self.bitwise = not self.bitwise
                
            if all([True if self.grid_matrix[i][i][1] and self.grid_matrix[i][i][2] == "x" else False for i in range(3)]) or all([True if self.grid_matrix[i][3 - i - 1][1] and self.grid_matrix[i][3 - i - 1][2] == "x" else False for i in range(3)]):
                self.setWindowTitle(self.plan["player1"][0])
                self.endgame = 1
            elif all([True if self.grid_matrix[i][i][1] and self.grid_matrix[i][i][2] == "o" else False for i in range(3)]) or all([True if self.grid_matrix[i][3 - i - 1][1] and self.grid_matrix[i][3 - i - 1][2] == "o" else False for i in range(3)]):
                self.setWindowTitle(self.plan["player2"][0])
                self.endgame = 1
            else:    
                for i in range(3):
                    x_row_reply = all([True if self.grid_matrix[i][j][1] and self.grid_matrix[i][j][2] == "x" else False for j in range(3)])
                    x_column_reply = all([True if self.grid_matrix[j][i][1] and self.grid_matrix[j][i][2] == "x" else False for j in range(3)])
                    o_row_reply = all([True if self.grid_matrix[i][j][1] and self.grid_matrix[i][j][2] == "o" else False for j in range(3)])
                    o_column_reply = all([True if self.grid_matrix[j][i][1] and self.grid_matrix[j][i][2] == "o" else False for j in range(3)])
                    if x_row_reply or x_column_reply:
                        self.setWindowTitle(self.plan["player1"][0] + " WINS !!")
                        self.endgame = 1
                    elif o_row_reply or o_column_reply:
                        self.setWindowTitle(self.plan["player2"][0] + " WINS !!")
                        self.endgame = 1
            if self.counter == 9:
                self.setWindowTitle("NULL !!")