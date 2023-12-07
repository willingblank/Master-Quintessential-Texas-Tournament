
publish_to_name = ""

def set_publish_to_name(name):
    global publish_to_name
    publish_to_name = name

def get_publish_to_name():
    global publish_to_name
    return publish_to_name

def client_publish_to_msg_consist(command,para):
    global publish_to_name
    msg_consist = "(sever)"+"<"+publish_to_name+">"+command+":"+str(para)
    return msg_consist

def client_publish_msg_all_consist(command,para):
    msg_consist = "(sever)"+"<"+"all"+">"+command+":"+str(para)
    return msg_consist