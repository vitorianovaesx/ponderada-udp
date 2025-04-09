import socket

# Mesmas configurações do servidor
ENDERECO = "127.0.0.1"
PORTA = 54321

# Cria socket UDP
socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Lê dois valores do usuário
valor_x = input("Primeiro valor: ")
valor_y = input("Segundo valor: ")
mensagem = f"{valor_x},{valor_y}"

print(f"[Cliente] enviando '{mensagem}' para {ENDERECO}:{PORTA}")
socket_cliente.sendto(mensagem.encode("utf-8"), (ENDERECO, PORTA))

# Aguarda a resposta
pacote, _ = socket_cliente.recvfrom(2048)
print("[Cliente] resposta do servidor:", pacote.decode("utf-8"))

socket_cliente.close()