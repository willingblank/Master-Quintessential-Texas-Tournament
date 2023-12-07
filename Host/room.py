
import paho.mqtt.client as mqtt
import threading
import publish_msg

room_list = []
room_counter = 0

def room_msg_handle(client,userdata,msg):
    if(str(msg).find("(client)") == 2):
        if(str(msg).find("#start") != -1):
            publish_data =  publish_msg.client_publish_msg_all_consist("#start",1)
            client.publish('willingblank_TexasPoker_roomid='+userdata,
                payload=publish_data,qos=0)

def room_thread_func(room_counter):
    room_list[room_counter].loop_forever()


def on_connect_room(client, userdata, flags, rc):
    if(rc == 0):
        print("Host successfully connected to the room = "+str(userdata))
    client.subscribe('willingblank_TexasPoker_roomid='+userdata+'/#')

def on_message_room(client, userdata, msg):
    rec_msg = str(msg.payload)
    print("<<<"+msg.topic+" "+rec_msg+">>>")
    room_msg_handle(client,userdata,rec_msg)


def room_init(roomid):
    global room_counter
    room_client = mqtt.Client()
    room_client.on_connect = on_connect_room
    room_client.on_message = on_message_room
    room_client.user_data_set(roomid)
    room_client.connect('broker.emqx.io', 1883, 60)
    room_list.append(room_client)

    room_thread = threading.Thread(target=room_thread_func,args=(room_counter,))
    room_thread.start()

    room_counter = room_counter + 1