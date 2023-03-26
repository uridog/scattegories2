import socket as so
import sqlite3
import threading as th
from queue import Queue

from db import check_if_in_db, add_user_sql, check_password, build_db

#build_db()
clients = []
conn_q = Queue()
buf = 1024
file = open("countries.txt")
countriesList = file.read().split("\n")
file2 = open("cities.txt")
citiesList = file2.read().split("\n")
file3 = open("boy.txt")
boyList = file3.read().split("\n")
file4 = open("movies.txt")
movieList = file4.read().split("\n")
file5 = open("animals.txt", encoding="utf8")
animalsList = file5.read().split("\n")
file6 = open("fruitsAndVeggies.txt")
fruitsAndVeggiesList = file6.read().split()
def handle_client(client_socket):

    print("222", th.get_native_id())
    """Handles a single client connection."""
    cattegoriesarr = [0,0,0,0,0,0]
    while True:
        try:
            data = client_socket.recv(1024).decode()
            print(data)
        #    if "username:" in data:
         #       print("gghsfj")
          #      while check_if_in_db(data.split(":")[1]):
          #          client_socket.send("username is already taken".encode())
           #         data = client_socket.recv(1024).decode()
            #    print("GH")
             #   client_socket.send("Accepted".encode())
              #  add_user_sql(data)
               # clients.append((client_socket, data.split(":")[1]))
                #print(clients)
         #       client_socket.send("Accepted".encode())
          #  if "usernameold:" in data:
          #      while check_if_in_db(data.split(":")[1]) is not True:
          #          client_socket.send("user not found.".encode())
           #         data = client_socket.recv(1024).decode()
            #    username = data.split(":")[1]
             #   client_socket.send("Accepted".encode())
              #  data = client_socket.recv(1024).decode()
              #  while check_password(username,data.split(":")[1]) is not True:
              #      client_socket.send("password is wrong:".encode())
              #      data = client_socket.recv(1024).decode()
              #  client_socket.send("Accepted".encode())
         #   else:
            MyText = data.lower()
            MyText = MyText.title()
            MyTextList = MyText.split(" ")
            for i in countriesList:
                    if i in MyTextList:
                        print("you said a country")
                        client_socket.send("you said a country".encode())
                        cattegoriesarr[0] = 1
                        break
            for x in citiesList:
                    if x in MyTextList:
                        print("you said a capital")
                        client_socket.send("you said a capital".encode())
                        cattegoriesarr[1] = 1
                        break
            for j in boyList:
                    if j in MyTextList:
                        print("you said a boy")
                        client_socket.send("you said a boy".encode())
                        cattegoriesarr[2] = 1
                        break
            for p in movieList:
                    if p in MyTextList:
                        print("you said a movie")
                        client_socket.send("you said a movie".encode())
                        cattegoriesarr[3] = 1
                        break
            for t in animalsList:
                    if t in MyTextList:
                        print("you said an animal")
                        client_socket.send("you said a animal".encode())
                        cattegoriesarr[4] = 1
                        break
            for n in fruitsAndVeggiesList:
                    if n in MyTextList:
                        print("you said an fruit/vegetable")
                        client_socket.send("you said an fruit/vegetable".encode())
                        cattegoriesarr[5] = 1
                        break
            print("Did you say ", MyText)
            if 0 not in cattegoriesarr:
                    client_socket.send("nice, you finished all cattegories")
        except:
            pass
def main():
    print("Start Serv")
    server_socket = so.socket()
    server_socket.bind(('0.0.0.0', 8820))
    server_socket.listen(1)
    while True:
        (client_socket, client_address) = server_socket.accept()
        try:
            a = th.Thread(target=handle_client, args=(client_socket,))
        except:
            pass
        a.start()

main()