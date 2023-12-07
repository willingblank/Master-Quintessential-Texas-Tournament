import paho.mqtt.client as mqtt
import threading
import lobby
import room

print("TexasPoker Host Sever Program running.... \n")
lobby.lobby_client_init()

while 1:
    if(lobby.get_lobby_create_req_flag()):
        roomid = lobby.get_lobby_toRoom()
        room.room_init(roomid)
        lobby.set_lobby_create_req_flag(0)