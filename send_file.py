def send_file(filename: str = "myfile.txt", testing: bool = False) -> None:
    import socket

    port = 12312  
    sock = socket.socket()  
    host = socket.gethostname()  
    sock.bind((host, port))  
    sock.listen(5)  

    while True:
        conn, addr = sock.accept()  
        data = conn.recv(1024)

        with open(filename, "rb") as in_file:
            data = in_file.read(1024)
            while data:
                conn.send(data)
                data = in_file.read(1024)

        print("Gonderildi")
        conn.close()
        if testing:
            break

    sock.shutdown(1)
    sock.close()


if __name__ == "__main__":
    send_file()
