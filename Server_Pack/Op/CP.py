
def ToBit(board):
    bin= "0b"
    for i in board:
        bin+=str(i)
    return int(bin,2)

def toBBF(i):
    temp=[0,0,0,0,0,0,0,0,0]
    temp[i-1]=1
    return ToBit(temp)

def Score(place,myBoard,opBoard):
    wincons=[0b111000000,0b000111000,0b000000111,0b100100100,0b010010010,0b001001001,0b100010001,0b001010100]
    SingleDigit=[1,2,4,8,16,32,64,128,256]
    score=0
    trap=False
    for con in wincons:
        #1 for every possible win
        if ((place & con)>0) and ((opBoard & con)==0):
            score+=1
            #if win, win
            win=myBoard & con
            OpSoonWin=True
            for Int in SingleDigit:
                if Int == int(win):
                    OpSoonWin=False
            if OpSoonWin:
                score+=15
        #1 if will lose, block
        #checks by looking if the opponent has
        #two spaces occupied in wincon
        if (opBoard & con>0) and (place & con>0):
            lose=opBoard & con
            OpSoonWin=True
            for Int in SingleDigit:
                if Int == int(lose):
                    OpSoonWin=False
            if OpSoonWin:
                score+=10
            
    return score

def think(opboard,myboard):
    bestmove=-1
    bestscore=-1
    #evaluate all open spaces
    for i in range(1,10):
        #to board binary form
        bi=toBBF(i)
        #if space taken skip
        if (bi & opboard==0) and (bi & myboard==0):
            newScore=Score(bi,myboard,opboard)
            if newScore>bestscore:
                bestmove=i
                bestscore=newScore
    
    return bestmove

def turn(opboard,myboard):
    print(opboard)
    myBoard=ToBit(myboard)
    opBoard=ToBit(opboard)
    BM=think(opBoard,myBoard)
    return BM

