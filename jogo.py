import socket

palavra_secreta = ""
chutes = []
chutesdados = 0
max_erros = 5  # Máximo de erros permitidos
chutesErrados = []


def start_server():
    try:
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
        print(f"Palavra secreta recebida com sucesso!")

        # Fecha a conexão
        conn.close()
        server_socket.close()

        return data

    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")
        return ""


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
    return erros >= max_erros


def abertura():
    print("/****************/")
    print("/Palavra Enforcada/")
    print("/****************/\n")


def chuta():
    global chutesdados
    chute = input("\nQual letra? ").lower()  # Converte para minúsculas
    if chute not in palavra_secreta:
        chutesErrados.append(chute)
        print(f"\nNão tem a letra '{chute}' na palavra secreta")
        print(f"Letras erradas: {chutesErrados}")
    if not chute.isalpha() or len(chute) != 1:  # Verifica se é uma única letra
        print("Entrada inválida. Digite uma letra.")
    elif jachutou(chute):
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


def erros_restantes():
    erros = 0
    for chute in chutes:
        if chute not in palavra_secreta:
            erros += 1
    return max_erros - erros


def joga():
    global palavra_secreta
    abertura()
    palavra_secreta = start_server()  # Recebe a palavra secreta via socket
    if not palavra_secreta:
        print("Erro: não foi possível iniciar o jogo sem uma palavra secreta.")
        return

    while not ganhou() and not enforcou():
        desenha_forca()
        print(f"Você tem {erros_restantes()} vidas restantes.")
        chuta()

    if ganhou():
        print(f"\nParabéns! Você ganhou! A palavra era '{palavra_secreta}'")
        print(f"Você conseguiu com {erros_restantes()} vidas")
        print(f"chutes errados: {chutesErrados}")
        diferenca = set(chutes) - set(chutesErrados)
        print(f"chutes corretos: {diferenca}")

    else:
        print(f"\nVocê foi enforcado! A palavra era '{palavra_secreta}'")
        print(f"chutes errados: {chutesErrados}")
        diferenca = set(chutes) - set(chutesErrados)
        print(f"chutes corretos: {diferenca}")


# Inicia o jogo
if __name__ == "__main__":
    joga()
