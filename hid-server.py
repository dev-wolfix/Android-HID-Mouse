import socket
import time

# Print Connection and Moving logs
DEBUG = True

HOST = "0.0.0.0"
PORT = 54321

def move_payload(dx, dy):
    with open("/dev/hidg1", "wb") as f:
        f.write(bytes([0x00, dx & 0xFF, dy & 0xFF, 0x00, 0x00, 0x00, 0x00, 0x00]))

def move_to(x, y, steps=20):
    for i in range(steps):
        move_payload(x // steps, y // steps)
        time.sleep(0.01)

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"TCP server started on {HOST}:{PORT}")

    while True:
        client, addr = s.accept()
        if DEBUG: print(f"Connection from {addr}")
        with client:
            while True:
                data = client.recv(1024)
                if not data: break
                cmd = data.decode().strip().split()
                if len(cmd) == 3 and cmd[0].upper() == "MOVE":
                    try:
                        if DEBUG: print(f"Moving to ({int(cmd[1])}, {int(cmd[2])})")
                        move_to(int(cmd[1]), int(cmd[2]))
                        client.sendall(b"OK\n")
                    except ValueError:
                        client.sendall(b"ERROR: Invalid coordinates\n")
                else:
                    print(f"Unknown command: {cmd}")
                    client.sendall(b"ERROR: Unknown command\n")
