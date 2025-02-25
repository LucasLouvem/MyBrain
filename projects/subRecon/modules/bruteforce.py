import requests

WORDLIST = ["www", "mail", "ftp"]

def brute_force(domain):
    print(f"[*] Fazendo brute-force em {domain}")
    found = []

    for sub in WORDLIST:
        subdomain = f"{sub}.{domain}"
        try:
            response = requests.get(f"http://{subdomain}",timeout=2)
            if response.status_code < 400:
                found.append(subdomain)
                print(f"[+] Encontrado: {subdomain}")
        except requests.ConnectionError:
            pass

    return found
