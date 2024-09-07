import socket

palavra_secreta = ""
chutes = []
chutesdados = 0


def start_server():
    # Criação do socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # IP e porta
    server_socket.listen(1)  # Máximo de conexões em espera

    print("Aguardando conexão...")
    conn, addr = server_socket.accept()
    print(f"Conectado a {addr}")
    print("Aguardando que o outro Jogador escolha a palavra secreta...")

    # Recebe dados
    data = conn.recv(1024).decode('utf-8')
    print(f"Palavra secreta recebida: {data}")

    # Fecha a conexão
    conn.close()
    server_socket.close()

    return data


def ganhou():
    for letra in palavra_secreta:
        if letra not in chutes:
            return False
    return True


def enforcou():
    erros = 0
    for chute in chutes:
        if chute not in palavra_secreta:
            erros += 1
    return erros >= 5


def abertura():
    print("/****************/")
    print("/  Jogo de Forca! /")
    print("/****************/\n")


def chuta():
    global chutesdados
    chute = input("Qual letra? ")
    if jachutou(chute):
        print(f"Você já chutou a letra '{chute}'. Tente outra.")
    else:
        chutes.append(chute)
        chutesdados += 1


def jachutou(letra):
    return letra in chutes


def desenha_forca():
    print("Palavra: ", end="")
    for letra in palavra_secreta:
        if letra in chutes:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print()


def joga():
    global palavra_secreta
    abertura()
    palavra_secreta = start_server()  # Recebe a palavra secreta via socket
    while not ganhou() and not enforcou():
        desenha_forca()
        chuta()

    if ganhou():
        print("\nParabéns! Você ganhou!")
    else:
        print(f"\nVocê foi enforcado! A palavra era '{palavra_secreta}'")


# Inicia o jogo
if __name__ == "__main__":
    joga()
