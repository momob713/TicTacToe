import OpGame
import threading
import time
import os

GameCount=0

def NewPlayer(player):
    newgame(player)

def gameover():
    global GameCount
    GameCount=GameCount - 1

def getOpMaster_report():
    global GameCount
    return GameCount
def newgame(player):
    player1=player
    print(f"{player1[1]} starting solo game.")
    Thread = threading.Thread(target=OpGame.game, args=(player1))
    Thread.start()
    global GameCount
    GameCount+=1
            
