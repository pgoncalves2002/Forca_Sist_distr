import socket

def send_string():
    # Criação do socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('26.3.238.10', 12345))  # IP e porta do servidor
    palavra = input("Digite uma palavra: ")
    # Envia dados
    client_socket.sendall(palavra.encode('utf-8'))

    # Fecha a conexão
    client_socket.close()
    print("Palavra enviada com sucesso!")


print("Jogador 1")
send_string()