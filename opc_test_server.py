from opcua import Server
import os, time, random

server = Server()

#url = "opc.tcp://192.168.1.17:4840"
PORT = 4840
IP = os.popen('hostname -I').read().split('\n')[0].split(' ')[0]

url = "opc.tcp://{}:{}".format(IP, PORT)

server.set_endpoint(url)

name = "INDUSTRIAL_SHIELD_OPCUA_SERVER"
addspace = server.register_namespace(name)

node = server.get_objects_node()

Param = node.add_object_type(addspace, "Parameters")

Ultrasound = Param.add_variable(addspace, "ultrasound", 0)
Luminosity = Param.add_variable(addspace, "luminosity", 0)
Led = Param.add_variable(addspace, "led", 0)

Ultrasound.set_writable()
Luminosity.set_writable()
Led.set_writable()

server.start()

print("{} started at {}".format(name, url))

while True:

    Ultrasound.set_value(random.randint(0, 100))
    Luminosity.set_value(random.randint(0, 100))
    Led.set_value(random.randint(0, 1))

    time.sleep(2)
