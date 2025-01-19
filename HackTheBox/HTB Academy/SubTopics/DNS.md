O **DNS (Domain Name System)** é um sistema que traduz nomes de domínio amigáveis para humanos, como `www.google.com`, em endereços IP, como `142.250.64.78`, que são utilizados pelos computadores para localizar e se comunicar com outros dispositivos na rede. Ele é essencial para o funcionamento da internet, pois permite que os usuários acessem sites e serviços sem precisar memorizar longas sequências de números.

---

### Como o DNS funciona?

1. **Entrada do domínio pelo usuário:** Quando você digita um domínio no navegador (por exemplo, `www.google.com`), uma consulta DNS é iniciada para determinar o endereço IP correspondente.
    
2. **Resolução do nome:** A consulta percorre várias etapas até encontrar o endereço IP. O processo geralmente segue este fluxo:
    
    - **Cache local:** O sistema operacional verifica se já tem o endereço IP armazenado em cache.
    - **DNS recursivo:** Se não estiver no cache, a solicitação é enviada para um servidor DNS recursivo, geralmente fornecido pelo provedor de internet.
    - **Consulta aos servidores DNS:** O recursivo pode consultar outros servidores para resolver o domínio, passando por:
        - **Servidor raiz (Root):** O ponto inicial que direciona a consulta para o TLD correto (por exemplo, `.com`, `.org`).
        - **Servidor TLD (Top-Level Domain):** Responsável por gerenciar domínios de alto nível e apontar para o servidor autoritativo do domínio.
        - **Servidor autoritativo:** Contém o mapeamento exato do domínio para seu endereço IP.
3. **Resposta:** O DNS recursivo retorna o endereço IP ao dispositivo cliente, permitindo que ele se conecte ao servidor correspondente.
    

---

### Componentes principais do DNS

1. **Domínio:**
    
    - É o nome amigável associado a um recurso na internet (exemplo: `www.google.com`).
    - Dividido em partes hierárquicas, como:
        - **TLD (Top-Level Domain):** `.com`, `.org`, `.net`.
        - **Domínio de segundo nível:** `google` em `google.com`.
        - **Subdomínio:** `www` em `www.google.com`.
2. **Servidores DNS:**
    
    - **Servidor raiz (Root Server):** O ponto inicial de toda consulta DNS, mantém informações sobre TLDs.
    - **Servidor TLD:** Gerencia domínios específicos de alto nível, como `.com` ou `.br`.
    - **Servidor autoritativo:** Armazena os registros finais do domínio.
3. **Registros DNS:** Contêm informações específicas sobre o domínio. Alguns tipos comuns incluem:
    
    - **A:** Mapeia um nome de domínio para um endereço IPv4.
    - **AAAA:** Mapeia um nome de domínio para um endereço IPv6.
    - **CNAME (Canonical Name):** Redireciona um domínio para outro.
    - **MX (Mail Exchange):** Define servidores responsáveis por e-mails.
    - **TXT:** Armazena informações arbitrárias, como validações SPF e DKIM.
    - **NS (Name Server):** Indica os servidores DNS autoritativos de um domínio.
    - **PTR:** Realiza a resolução reversa de IPs para nomes de domínio.
4. **Servidor DNS recursivo:** É o intermediário que lida com a consulta inicial e resolve o nome de domínio em um endereço IP, comunicando-se com outros servidores DNS.
    

---

### Tipos de Consulta DNS

1. **Consulta recursiva:** O cliente solicita que o servidor DNS encontre o endereço IP completo. O servidor recursivo faz todo o trabalho de comunicação com outros servidores.
    
2. **Consulta iterativa:** O servidor DNS fornece a melhor resposta possível, geralmente redirecionando o cliente ao próximo servidor DNS na hierarquia.
    
3. **Consulta reversa:** Traduz um endereço IP para um nome de domínio, utilizando registros PTR.
    

---

### Cache no DNS

Para melhorar o desempenho, os resultados de consultas DNS são armazenados em cache em:

- O próprio cliente.
- O servidor DNS recursivo.
- Navegadores.

O tempo de retenção no cache é determinado pelo valor **TTL (Time to Live)** definido no registro DNS.

---

### Segurança no DNS

- **DNSSEC (DNS Security Extensions):** Adiciona assinaturas digitais aos dados DNS para proteger contra falsificação de registros (DNS spoofing).
- **Ataques comuns:**
    - **DNS Spoofing:** Inserção de informações falsas na cache DNS.
    - **DDoS usando DNS:** Amplificação de consultas para sobrecarregar servidores.