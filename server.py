import socket
from _thread import *
from player import Player
import pickle

SERVER = '127.0.0.1'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((SERVER, PORT))
except socket.error as e:
    print(e)

s.listen()
print('Waiting for connection. Server started.')

players = [Player(0, 0, 100, 100, (255, 0, 0)), Player(50, 50, 100, 100, (255, 0, 255))]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print('Disconnected')
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            # print(f'Received: {data}')
            # print(f'Sending: {reply}')

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print('Lost connection')
    conn.close()


current_player = 0
connected = True

while connected:
    conn, addr = s.accept()
    print(f'Connected to {addr}')

    start_new_thread(threaded_client, (conn, current_player))
    current_player += 1

