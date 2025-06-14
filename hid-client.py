import socket
from time import sleep

HOST = "LOCAL_IP_OF_YOUR_PHONE"
PORT = 54321

def send_move_command(x, y):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(f"MOVE {x} {y}\n".encode())
        print(s.recv(1024).decode().strip())

if __name__ == "__main__":

    ### Enjoy :3

    send_move_command(300, 0)
    sleep(0.01)
    send_move_command(0, 300)
    sleep(0.01)
    send_move_command(-300, 0)
    sleep(0.01)
    send_move_command(0, -300)
