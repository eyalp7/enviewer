import socket
import threading

def recieve_screenshots():
    #a function that recieves the screenshots and desplays them
    pass

def send_mouse_info():
    #a function that sends information about the mouse
    pass

def send_keyboard_press():
    #a function that sends keyboard presses
    pass

def connect_to_server(ip, port):
    #a function that connects to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        #connecting to the server
        client_socket.connect((ip, port))
        print("Connected to the server!")

        #creating a thread that will handle each major task
        screenshots_thread = threading.Thread(target=recieve_screenshots).start()
        mouse_thread = threading.Thread(target=send_mouse_info).start()
        keyboard_thread = threading.Thread(target=send_keyboard_press).start()

        #waiting for all of the threads to end
        screenshots_thread.join()
        mouse_thread.join()
        keyboard_thread.join()

    finally:
        #closing the connection
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    connect_to_server()



