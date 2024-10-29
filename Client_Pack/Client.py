import socket 
import UI
import ast

def connect_to_server():
    host=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.connect(('localhost', 4632))
    return host

def recieve_data(host):
    return str(host.recv(1024).decode())

def send_data(host,message):
    return host.send(str(message).encode())

def send_to_ui(Console_display, message):
    Console_display.print_to_ui(message)
    pass

def get_input(Console_display):
    return Console_display.input()

def update_myboard(myboard,a):
    myboard[a-1]=1
    return myboard

def update_opboard(opboar):
    return opboar

def updateTheBoard(char, board, TheBoard):
    column=0
    row=0
    for i in board:
        if i==1:
            TheBoard[row][column]=char
        column+=1
        if column==3:
            row+=1
            column=0
    
    return TheBoard

def validmovecheck(A,B,c):
    if A[c-1]==0 and B[c-1]==0:
        return False
    else:
        return True
        
if __name__ == '__main__':
    game_on=True
    #pick game style
    Console_display = UI.consoleui()
    send_to_ui(Console_display, "Play against Computer(1) or another Player(2)?")
    choice=get_input(Console_display)
    Choice=""
    if choice==1:
        Choice="Computer"
    elif choice==2:
        Choice="Two"
    host=connect_to_server()
    send_data(host,Choice)
    myboard=[0,0,0,0,0,0,0,0,0]
    opboard=[0,0,0,0,0,0,0,0,0]
    TheBoard=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    mychar=""
    opchar=""
    while game_on:
        data=recieve_data(host)
        if data=="connected":
            send_to_ui(Console_display,"Connected to Server")
        if data=="Waiting for lobby...":
            send_to_ui(Console_display,"Waiting for lobby...")
        elif data[0:9]=="GameStart":
             Console_display.clear_screen() 
             send_to_ui(Console_display,"Game Starting...")
             mychar=data[9:10]
             opchar=data[10:11]
             Console_display.clear_screen()
        elif data=="turn":
            Console_display.clear_screen()
            send_to_ui(Console_display,"Your Turn")
            send_to_ui(Console_display,f"You are: {mychar}")
            Console_display.print_board()
            nogo=True
            choice=6
            while nogo:
                send_to_ui(Console_display,"Choose a valid space.")
                choice=get_input(Console_display)
                nogo=validmovecheck(myboard,opboard,choice)
            myboard=update_myboard(myboard,choice)
            TheBoard=updateTheBoard(mychar,myboard, TheBoard)
            Console_display.updateBoard(TheBoard)
            Console_display.print_board()
            send_data(host,choice)
        elif data[0]=="[":
            opboard=update_opboard(ast.literal_eval(data))
            TheBoard=updateTheBoard(opchar, opboard, TheBoard)
            Console_display.updateBoard(TheBoard)
        elif data=="wait":
            send_to_ui(Console_display,"Waiting on opponent")
        elif data[0:4]=="Lose":
            Console_display.clear_screen()
            send_to_ui(Console_display,"You Lose.")
            opboard=update_opboard(ast.literal_eval(data[4:]))
            TheBoard=updateTheBoard(opchar, opboard, TheBoard)
            send_to_ui(Console_display,"End Game State")
            Console_display.updateBoard(TheBoard)
            Console_display.print_board()
            game_on=False
        elif data[0:3]=="Win":
            Console_display.clear_screen()
            send_to_ui(Console_display,"You win!!!")
            opboard=update_opboard(ast.literal_eval(data[3:]))
            TheBoard=updateTheBoard(opchar, opboard, TheBoard)
            send_to_ui(Console_display,"End Game State")
            Console_display.updateBoard(TheBoard)
            Console_display.print_board()
            game_on=False
        elif data[0:3]=="Tie":
            Console_display.clear_screen()
            send_to_ui(Console_display,"Tie!")
            send_data(get_input(Console_display))
            opboard=update_opboard(ast.literal_eval(data[3:]))
            TheBoard=updateTheBoard(opchar, opboard, TheBoard)
            send_to_ui(Console_display,"End Game State")
            Console_display.updateBoard(TheBoard)
            Console_display.print_board()
            game_on=False
        elif data[0]=="c":
            myboard=update_myboard(ast.literal_eval(data[1:]))
            TheBoard=updateTheBoard(mychar, myboard, TheBoard)
            Console_display.updateBoard(TheBoard)
            send_to_ui(Console_display,"Invalid Space. Try again.")
    host.close()
