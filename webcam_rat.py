import cv2
import socket
import pickle
import struct
import time

def capture_webcam():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Erreur: Impossible d'ouvrir la webcam.")
        return None
    ret, frame = cap.read()
    if not ret:
        print("Erreur: Impossible de capturer une image.")
        return None
    cap.release()
    return frame

def send_image_over_network(image, host='127.0.0.1', port=8080):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    data = pickle.dumps(image)
    message = struct.pack("Q", len(data)) + data
    client_socket.sendall(message)
    client_socket.close()

def capture_and_send():
    while True:
        image = capture_webcam()
        if image is not None:
            send_image_over_network(image)
            print("Image envoyée avec succès.")
        else:
            print("Échec de la capture de l'image.")
        time.sleep(5)

if __name__ == "__main__":
    capture_and_send()