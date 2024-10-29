import copy
import os

class consoleui(object):
    board=""
    rawboard=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    def __init__(self):
        self.board=f" {self.rawboard[0][0]} | {self.rawboard[0][1]} | {self.rawboard[0][2]} \n-----------\n {self.rawboard[1][0]} | {self.rawboard[1][1]} | {self.rawboard[1][2]} \n-----------\n {self.rawboard[2][0]} | {self.rawboard[2][1]} | {self.rawboard[2][2]} "

    def clear_screen(self):
        os.system('clear')
    
    def print_to_ui(self, message):
        print(message)
        pass
    
    def print_board(self):
        print(self.board)
        pass
    
    def input(self):
        return int(input())
    
    def updateBoard(self,newboard):
        self.rawboard=copy.deepcopy(newboard)
        self.board=f" {self.rawboard[0][0]} | {self.rawboard[0][1]} | {self.rawboard[0][2]} \n-----------\n {self.rawboard[1][0]} | {self.rawboard[1][1]} | {self.rawboard[1][2]} \n-----------\n {self.rawboard[2][0]} | {self.rawboard[2][1]} | {self.rawboard[2][2]} "
        pass
