import socket
import sqlite3



def Main():
    host = "127.0.0.1"
    port = 5000
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
            DBconn = sqlite3.connect('..\db.sqlite3')
            cursor = DBconn.cursor()
            print("Opened database successfully")
            uniqueId = str(data)
            Query = "UPDATE polls_cqrcode set isAuthenticated = 1 where uniqueId = " + str(uniqueId)
            print (str(Query))
            try:
                DBconn.execute(Query)
                DBconn.commit()
            except:
                print ("Not auth")

            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    DBconn.close()
     
if __name__ == '__main__':
    Main()