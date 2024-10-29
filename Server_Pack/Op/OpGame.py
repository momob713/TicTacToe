import CP
import time
import random
import OpMaster

def tell_player(player,msg):
    player.send(msg.encode())
    pass

def from_player(player):
    return player.recv(1024).decode()

"for bad acrtors"
def serverupdate(player, board):
    tell_player(player, "c"+str(board))
    pass
    
def update_board(opboard ,theirboard, place):
    cheat=False
    if opboard[place-1]==0 and theirboard[place-1]==0:
        theirboard[place-1]=1
        cheat=True
    return cheat

def endgamecheck(Aboard,Bboard):
    wincons={}
    wincons['win1']=[1,1,1,0,0,0,0,0,0]
    wincons['win2']=[0,0,0,1,1,1,0,0,0]
    wincons['win3']=[0,0,0,0,0,0,1,1,1]
    wincons['win4']=[1,0,0,1,0,0,1,0,0]
    wincons['win5']=[0,1,0,0,1,0,0,1,0]
    wincons['win6']=[0,0,1,0,0,1,0,0,1]
    wincons['win7']=[1,0,0,0,1,0,0,0,1]
    wincons['win8']=[0,0,1,0,1,0,1,0,0]
    for i in wincons:
        awin=0
        bwin=0
        c=0
        for a in wincons[i]:
            if Aboard[c]==1 and Aboard[c]==a:
                awin+=1
            elif Bboard[c]==1 and Bboard[c]==a:
                bwin+=1
            c+=1
        if awin==3:
            return int(1)
        elif bwin==3:
            return int(2)
    for a,b in zip(Aboard,Bboard):
        if a==0 and b==0:
            return int(0)
    return int(3)
def game(socket,addr):
    print("yes")
    p1board=[0,0,0,0,0,0,0,0,0]
    p2board=[0,0,0,0,0,0,0,0,0]
    p1=socket
    p1addr=addr
    tell_player(p1,"GameStartXO")
    WhoTurn=random.randint(1,2)
    go=True
    while go:
        pc=True
        if WhoTurn%2==0:
            tell_player(p1, "turn")
            while pc:
                if update_board(p2board,p1board,int(from_player(p1))):
                    pc=False
                else:
                    serverupdate(p1,p1board)
        else:
            tell_player(p1, "wait")
            ComputerChoice=CP.turn((p1board),(p2board))
            print(p1board,p2board,ComputerChoice)
            if update_board(p1board,p2board,int(ComputerChoice)):
                print("good")
                tell_player(p1,str(p2board))
        check=endgamecheck(p1board,p2board)
        if check>0:
            go=False
            if check==1:
                tell_player(p1,("Win"+str(p2board)))
            elif check==2:
                tell_player(p1,("Lose"+str(p2board)))
            elif check==3:
                tell_player(p1,("Tie"+str(p2board)))
            OpMaster.gameover()
        WhoTurn+=1
