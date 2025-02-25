import argparse;
from modules import bruteforce, dns_resolver, api_scraper, exporter

def main():
    parser = argparse.ArgumentParser(description="SubRecon - Enumeração de subdomínios")
    parser.add_argument("-d", "--domain", required=True, help="Domínio a ser analisado")
    parser.add_argument("-o", "--output", help="Arquivo de saida para salvar resultados")
    args = parser.parse_args()

    domain = args.domain
    print(f"[+] Iniciando enumeração para: {domain}")
    
    subdomains = api_scraper.get_subdomains(domain)

    subdomains += bruteforce.brute_force(domain)

    subdomains = set(subdomains)

    resolved_subdomains = dns_resolver.resolve_subdomains(subdomains)

    if resolved_subdomains:
        if args.output:
            exporter.save_results(resolved_subdomains, args.output)
        print("[+] Enumeração Concluida")
    else:
        print(f"[-] Nenhum subdominio encontrado.")

if __name__ == "__main__":
    main()
