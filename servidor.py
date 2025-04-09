import socket

# Configurações de endereço
ENDERECO = "127.0.0.1"
PORTA = 54321

# Cria socket UDP e faz bind
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_servidor.bind((ENDERECO, PORTA))

print(f"[Servidor] escutando em {ENDERECO}:{PORTA}...")

while True:
    try:
        # Recebe até 2048 bytes
        pacote, cliente = socket_servidor.recvfrom(2048)
        texto = pacote.decode("utf-8").strip()
        print(f"[Servidor] recebidos de {cliente}: '{texto}'")

        # Espera algo como "3.5,2"
        partes = texto.split(",")
        if len(partes) != 2:
            resposta = "Erro: envie exatamente dois valores separados por vírgula"
        else:
            try:
                a, b = map(float, partes)
                produto = a * b
                resposta = f"Produto: {produto}"
            except ValueError:
                resposta = "Erro: informe dois números válidos"

        # Envia de volta para o cliente
        socket_servidor.sendto(resposta.encode("utf-8"), cliente)

    except Exception as err:
        print(f"[Servidor] erro interno: {err}")