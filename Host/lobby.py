import paho.mqtt.client as mqtt
import threading

lobby_client = mqtt.Client()
lobby_create_req_flag = 0
lobby_toRoom = ""

def get_lobby_toRoom():
    global lobby_toRoom
    return lobby_toRoom

def set_lobby_create_req_flag(num):
    global lobby_create_req_flag
    lobby_create_req_flag = num

def get_lobby_create_req_flag():
    global lobby_create_req_flag
    return lobby_create_req_flag

def lobby_msg_handle(msg):
    global lobby_create_req_flag
    global lobby_toRoom
    if(str(msg).find("#create") != -1):
        roomID_start_index = str(msg).find(":")
        room_ID = str(msg)[roomID_start_index+1:-1]
        lobby_toRoom = room_ID
        lobby_create_req_flag = 1

def lobby_thread_func():
    lobby_client.loop_forever()

def on_connect_lobby(client, userdata, flags, rc):
    if(rc == 0):
        print("Host successfully connected to the lobby!")
    client.subscribe('willingblank_TexasPoker_lobby/#')

def on_message_lobby(client, userdata, msg):
    print("<<<"+msg.topic+" "+str(msg.payload)+">>>")
    lobby_msg_handle(str(msg.payload))
    

def lobby_client_init():
    lobby_client.on_connect = on_connect_lobby
    lobby_client.on_message = on_message_lobby
    lobby_client.connect('broker.emqx.io', 1883, 60)
    lobby_thread_entity = threading.Thread(target=lobby_thread_func)
    lobby_thread_entity.start()


