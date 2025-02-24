import argparse;
from modules import bruteforce, dns_resolver, api_scraper, exporter

def main():
    parser = argparse.ArgumentParser(description="SubRecon - Enumeração de subdomínios")
    parser.add_argument("-d", "--domain", required=True, help="Domínio a ser analisado")
    parser.add_argument("-o", "--output", help="Arquivo de saida para resultados")
    args = parser.parse_arg()

    domain = args.domain
    print(f"[+] Iniciando enumeração para: {domain}")
    
    subdomains = api_scraper.get_subdomains(domain)

    subdomains += bruteforce.brute_force(domain)

    subdomains = set(subdomains)

    resolved_subdomains = dns_resolver.resolver_subdomains(subdomains)

    if args.output:
        exporter.save_results(resolved_subdomains, args.output)
    
    print("[+] Enumeração Concluida")

if __name__ == "__main__":
    main()