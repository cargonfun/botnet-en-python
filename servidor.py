from socket import *
puertoServidor = 4444
socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
socketServidor.bind(('', puertoServidor))
socketServidor.listen(1)
print("Servidor en escucha y a la espera de conexiones")
socketConexion, addr = socketServidor.accept()
print("Conexión realizada " + str(addr))
mensaje = connection.Socket.recv(1024)
print(mensaje)
comando = ""
while comando != "exit":
	comando = input("Ingrese un comando: ")
	socketConexion.send(commando.encode())
	mensaje = socketConexion.recv(1024).decode()
	print(mensaje)

socketConexion.shutdown(SHUT_RDWR)
socketConexion.close()
