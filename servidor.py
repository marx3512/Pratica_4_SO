from base64 import decode
import socket
import datetime
from this import d


def server(host = 'localhost', port=8082):
    data_payload = 2048 
    
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = (host, port)
    print ("Iniciando servidor na porta %s %s" % server_address)
    sock.bind(server_address)
    
    sock.listen(5)
    i = 0
    while True:
        print ("Esperando mensagem do cliente")
        client, address = sock.accept()
        data = client.recv(data_payload)
  
        if data:
            print ("Solicitação: %s" %data.decode())
            response = mostrar(data.decode())
            client.send(response.encode('utf-8'))
            client.close()


def mostrar(pedidoCliente):
    date = datetime.datetime.now()
    dia = f"{date.day}/{date.month}/{date.year}"
    hora = f"{date.hour}:{date.minute}:{date.second}"

    if(pedidoCliente == "1"):
        response = dia
    elif(pedidoCliente == "2"):
        response = hora
    elif(pedidoCliente == "3"):
        response = f"{dia} {hora}"
    else:
        response = "Invalid Request"

    return response

    
server()