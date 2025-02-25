import requests;

def get_subdomains(domain):
    print(f"[*] Coletando subdomínios via APIs para {domain}")
    subdomains = []

    url = f"https://api.hackertarget.com/hostsearch/?q={domain}"
    response = requests.get(url)

    if response.status_code == 200:
        lines = response.text.split("\n")
        for line in lines:
            subdomain = line.split(",")[0]
            subdomains.append(subdomain)

    return subdomains
