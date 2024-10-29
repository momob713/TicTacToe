import TpGame
import threading
import time
import os

GameCount=0
waiting_clients=[]

def tell_client(client,message):
    client[0].send(message.encode())
    pass
def get_next():
    global waiting_clients
    chosen=waiting_clients[0]
    waiting_clients.remove(chosen)
    return chosen

def NewPlayer(player):
    print(player[0])
    print(player[1])
    global waiting_clients
    waiting_clients.append(player)
    #start if enough
    if len(waiting_clients)>1:
        newgame()
    else:
        tell_client(player, "Waiting for lobby...")

def gameover():
    global GameCount
    GameCount-=1

def getTpMaster_report():
    global waiting_clients
    global GameCount
    return (GameCount,len(waiting_clients))

def newgame():
        global GameCount
        player1=get_next()
        player2=get_next()
        print(f"{player1[1]} and {player2[1]} are starting a game.")
        Thread = threading.Thread(target=TpGame.game, args=(player1,player2))
        Thread.start()
        GameCount+=1
