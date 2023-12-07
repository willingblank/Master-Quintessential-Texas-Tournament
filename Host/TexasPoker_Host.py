import paho.mqtt.client as mqtt
import threading

lobby_client = mqtt.Client()
room_client = [0]
room_thread = [0]
room_Index = 0
room_ID = ""
room_name_list = [[]]

def room_thread_func():
    room_client[room_Index].loop_forever()

def on_connect_room(client, userdata, flags, rc):
    global room_ID
    if(rc == 0):
        print("Host successfully connected to the room = "+room_ID)
    client.subscribe('willingblank_TexasPoker_roomid='+room_ID+'/#')

def on_message_room(client, userdata, msg):
    print("on_message_room userdata = "+str(userdata))
    global room_ID
    room_Index_lock = userdata
    rec_msg = str(msg.payload)
    print("<<<"+msg.topic+" "+rec_msg+">>>")
    join_index = rec_msg.find("#join:")
    if(join_index != -1):
        room_name_list[room_Index_lock].append(rec_msg[join_index+5:-1])
        print(room_name_list[0])
        client.publish('willingblank_TexasPoker_roomid='+room_ID,payload='type /ready to ready',qos=0)
    if(rec_msg.find("#ready:") != -1):
        client.publish('willingblank_TexasPoker_roomid='+room_ID,payload='waiting other player to start',qos=0)

        

def on_connect_lobby(client, userdata, flags, rc):
    if(rc == 0):
        print("Host successfully connected to the lobby!")
    client.subscribe('willingblank_TexasPoker_lobby/#')

def on_message_lobby(client, userdata, msg):
    global room_Index
    global room_ID
    print("<<<"+msg.topic+" "+str(msg.payload)+">>>")
    if(str(msg.payload)[2:9] == "#create"):
        roomID_start_index = str(msg.payload).find(":")
        room_ID = str(msg.payload)[roomID_start_index+1:-1]
        room_client[room_Index] = mqtt.Client()
        room_client[room_Index].on_connect = on_connect_room
        room_client[room_Index].on_message = on_message_room
        room_client[room_Index].user_data_set(room_Index)
        room_client[room_Index].connect('broker.emqx.io', 1883, 60)

        room_thread[room_Index] = threading.Thread(target=room_thread_func)
        room_thread[room_Index].start()

        room_Index = room_Index + 1
        room_client.append(room_Index)
        room_thread.append(room_Index)
        room_name_list.append([])
        

lobby_client.on_connect = on_connect_lobby
lobby_client.on_message = on_message_lobby

lobby_client.connect('broker.emqx.io', 1883, 60)
#lobby_client.publish('willingblanktesttopic',payload='Hello World',qos=0)

lobby_client.loop_forever()

