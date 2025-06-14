import socket
import struct
import pickle
import cv2

def receive_image(host='127.0.0.1', port=8080):
    # Crée un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Serveur en écoute sur {host}:{port}")

    conn, addr = server_socket.accept()
    with conn:
        print('Connexion établie avec', addr)
        while True:
            # Reçoit la taille de l'image
            data = conn.recv(1024)
            if not data:
                break
            msg_size = struct.unpack("Q", data[:8])[0]
            data = conn.recv(msg_size)

            # Désérialise l'image
            image = pickle.loads(data)
            cv2.imwrite('received_image.jpg', image)
            print("Image reçue et enregistrée sous 'received_image.jpg'")

if __name__ == "__main__":
    receive_image()