import dns.resolver;

def resolve_subdomains(subdomains):
    print(f"[*] Resolvendo DNS dos subdomínios...")
    resolved = {} 

    for subdomain in subdomains:
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            resolved[subdomain] = [answer.to_text() for answer in answers]
            print(f"[+] {subdomain} -> resolved{[subdomain]}")
        except dns.resolver.NXDOMAIN:
            pass
        except dns.resolver.NoAnswer:
            pass

    return resolved
