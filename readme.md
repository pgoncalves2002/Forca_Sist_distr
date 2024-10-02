# Jogo da Forca Distribuído

Este projeto implementa um jogo da forca simples utilizando a arquitetura cliente-servidor em Python. O servidor recebe a palavra secreta do cliente e gerencia todo o jogo localmente após a palavra ser enviada. O cliente, por sua vez, apenas envia a palavra secreta ao servidor.

## Funcionalidades

- Dois jogadores: Um escolhe a palavra secreta (cliente) e o outro tenta adivinhar (servidor).
- Implementação distribuída usando sockets TCP.
- Jogo gerenciado localmente no servidor após o envio da palavra secreta.
- Número máximo de 5 erros permitidos para adivinhar a palavra.

## Arquitetura

A arquitetura do jogo segue o modelo cliente-servidor:

- **Cliente (`perguntaPalavra.py`)**: Envia a palavra secreta ao servidor e encerra a conexão.
- **Servidor (`jogo5Tent.py`)**: Recebe a palavra secreta e gerencia o jogo localmente, onde o jogador realiza seus chutes diretamente.

## Pré-requisitos

- Python 3.x instalado.
- Biblioteca `socket` (já incluída na biblioteca padrão do Python).

## Como Executar

1. **Iniciar o servidor:**

   No terminal, execute o seguinte comando para iniciar o servidor:

   ```bash
   python jogo.py
    ```
   
1. **Iniciar o servidor:**

   No terminal, execute o seguinte comando para iniciar o cliente:

   ```bash
   python perguntaPalavra.py
    ```
   
