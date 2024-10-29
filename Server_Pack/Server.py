import sys
#import packages
import socket
import TpMaster
import OpMaster
import threading
import time
import os


idle_clients=[]
service=True
   
def handle(client_socket, addr):
    idle_clients.append((client_socket, addr))
    threading.Thread(target=GameChoice, args=(client_socket,addr)).start()
    pass


def send_data(client_socket, addr, message):
    client_socket.send(message.encode())

def server_report():
    while True:
        #os.system('clear')
        count = len(idle_clients)
        print(f"Number of idle_clients: {count}")
        TpReport=TpMaster.getTpMaster_report()
        OpReport=OpMaster.getOpMaster_report()
        print(f"Two Player Waiting Lobby: {TpReport[1]}")
        print(f"Two Player Games: {TpReport[0]}")
        print(f"One Player Games: {OpReport}")
        time.sleep(15)

    

def GameChoice(socket,addr):
    choose=False
    while not choose:
        choice=socket.recv(1024).decode()
        #computer
        if choice=="Computer":
            idle_clients.remove((socket,addr))
            OpMaster.NewPlayer((socket,addr))
            choose=True
        #2p
        elif choice =="Two":
            idle_clients.remove((socket,addr))
            TpMaster.NewPlayer((socket,addr))
            choose=True


def start_server():
    server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 4632))
    server.listen()
    print("Server start")
    threading.Thread(target=server_report, daemon=True).start()
    
    while service:
        client, addr = server.accept()
        print(f"{addr} connected")
        handle(client, addr)
        
if __name__ == '__main__':
    print("Server is starting...")
    start_server()
