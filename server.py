import socket
import threading

def send_screenshots():
    #a function that sends the client constant screenshots
    pass

def move_mouse():
    #a function that moves the mouse to match the state of the client's mouse
    pass

def keyboard_presses():
    #a function that presses the keys that the client pressed
    pass



def start_server(ip, port):
    #a function that creates a server
    #creating a tcp/ip socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen()
    print(f"Server listening on  {ip}:{port}")

    try:
        while True:
            #accepting the connections and running the different functions on it
            conn, addr = server_socket.accept()
            screenshots_thread = threading.Thread(target=send_screenshots).start()
            mouse_thread = threading.Thread(target=move_mouse).start()
            keyboard_thread = threading.Thread(target=keyboard_presses).start()
            
            #wait for all of the threads to stop running
            screenshots_thread.join()
            mouse_thread.join()
            keyboard_thread.join()


    finally:
        #closing the server
        server_socket.close()





    
