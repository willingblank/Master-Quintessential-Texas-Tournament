import time
import paho.mqtt.client as mqtt
import threading

isLobbyFlag = 1
client_lobby = mqtt.Client()
client_room = mqtt.Client()

def room_thread_func():
    client_room.publish('willingblank_TexasPoker_roomid='+roomid,payload="#join:"+name,qos=0)
    client_room.loop_forever()

def on_connect_room(client, userdata, flags, rc):
    print('Connected with result code '+str(rc))
    client.subscribe('willingblank_TexasPoker_roomid='+roomid+'/#')
    

def on_message_room(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client_room.on_connect = on_connect_room
client_room.on_message = on_message_room

# ====================================================================

name = input("willingblank's TexasPoker! \nplease enter your name:\t")
print("Nice to meet you :)  ",'<'+name+'>\n')
print("Welcom to Lobby, type /help to get command list.")

client_lobby.connect('broker.emqx.io', 1883, 60)
client_lobby.publish('willingblank_TexasPoker_lobby',payload="#lobbyIn:"+name,qos=0)

while 1:
    command = input()
    if(command == "/help"):
        print(">> /help (show command list)")
    elif(command == "/quit"):
        print(">> quit gmae")
        break
    elif(command == "/create"):
        roomid = input(">> input your room id: ")
        client_lobby.publish('willingblank_TexasPoker_lobby',payload="#create:"+roomid,qos=0)
        client_room.connect('broker.emqx.io', 1883, 60)
        time.sleep(1)
        room_thread = threading.Thread(target=room_thread_func)
        room_thread.start()
        isLobbyFlag = 0
        
    if(isLobbyFlag == 0):
        if(command == "/ready"):
            client_room.publish('willingblank_TexasPoker_roomid='+roomid,payload="#ready:"+name,qos=0)



print("Game Main Thread over")