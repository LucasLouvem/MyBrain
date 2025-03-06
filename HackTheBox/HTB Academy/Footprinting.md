# Princípios de Enumeração

## O que é Enumeração?

Enumeração é o processo de coleta de informações por meio de métodos ativos (varreduras) e passivos (uso de provedores terceirizados). Diferente do OSINT, que se baseia apenas na coleta passiva de dados, a enumeração envolve interações diretas com o alvo e deve ser realizada separadamente.

Este processo é um ciclo contínuo onde os dados coletados servem para identificar novos pontos de investigação, abrangendo domínios, endereços IP, serviços acessíveis e outros elementos da infraestrutura.

## Importância da Compreensão da Infraestrutura

Ao analisar a segurança de uma empresa, é essencial compreender sua estrutura, serviços utilizados e medidas de segurança adotadas. O erro comum de muitos pentesters é focar diretamente em ataques, como força bruta contra serviços de autenticação (SSH, RDP, WinRM), sem antes entender o contexto. Isso pode ativar sistemas de defesa e resultar na perda de acesso ao ambiente de teste.

A abordagem correta envolve um planejamento detalhado, semelhante a um caçador de tesouros que estuda mapas antes de começar sua busca. O objetivo é identificar todas as formas possíveis de acessar os sistemas, em vez de simplesmente tentar invadi-los sem estratégia.

## Princípios da Enumeração

Para guiar a investigação, devemos nos basear nas seguintes perguntas:

- O que podemos ver?
- Por que podemos vê-lo?
- Que imagem isso nos cria?
- Como podemos usar essa informação?
- O que não podemos ver?
- Por que não podemos ver?
- Que informação podemos inferir a partir disso?

A compreensão técnica é mais importante do que a habilidade de explorar sistemas. Muitas vezes, a dificuldade em prosseguir não se deve à falta de ferramentas, mas sim à falta de entendimento sobre como um sistema pode ser explorado.

### Três Princípios Fundamentais:

1. **Há mais do que aparenta** – Considere diferentes perspectivas.
2. **Distinguir entre o que vemos e o que não vemos** – O invisível pode ser tão importante quanto o visível.
3. **Sempre há formas de obter mais informações** – O conhecimento do alvo é essencial.

Para aplicar esses princípios de forma eficaz, é recomendável mantê-los visíveis durante a investigação, consultando-os sempre que necessário.

# Metodologia de Enumeração

A enumeração em testes de intrusão é um processo complexo que exige uma metodologia padronizada para garantir que nenhum aspecto seja negligenciado. Como os sistemas-alvo variam amplamente, a abordagem não pode ser rigidamente predefinida. Assim, a metodologia precisa equilibrar estrutura e flexibilidade.

### **Três Níveis de Enumeração**

1. **Enumeração baseada em infraestrutura** - Coleta informações gerais sobre a presença online e proteções externas.
2. **Enumeração baseada em hosts** - Foca nos serviços acessíveis e nos processos internos.
3. **Enumeração baseada no sistema operacional** - Identifica configurações, permissões e vulnerabilidades específicas do OS.

### **Camadas da Metodologia**

A metodologia de enumeração é dividida em seis camadas, representando barreiras a serem superadas para aprofundar o conhecimento sobre o alvo:

1. **Presença na Internet**
    
    - Identifica domínios, subdomínios, blocos de IP, ASN, instâncias em nuvem e medidas de segurança.
    - Objetivo: mapear a infraestrutura exposta.
2. **Gateway**
    
    - Examina medidas de proteção da infraestrutura, como firewalls, proxies, VPNs, e segmentação de rede.
    - Objetivo: entender como a rede é protegida e quais pontos podem ser explorados.
3. **Serviços Acessíveis**
    
    - Identifica portas abertas, versões de serviços e suas configurações.
    - Objetivo: aprender como interagir com os serviços e encontrar vulnerabilidades.
4. **Processos**
    
    - Examina dados processados, origem, destino e dependências de serviços.
    - Objetivo: identificar vulnerabilidades nos processos internos.
5. **Privilégios**
    
    - Analisa grupos de usuários, permissões e restrições.
    - Objetivo: descobrir erros de configuração e possíveis elevações de privilégio.
6. **Configuração do OS**
    
    - Coleta informações sobre o sistema operacional, patches, configuração de rede e arquivos sensíveis.
    - Objetivo: avaliar a segurança interna do sistema e identificar brechas.

### **Metodologia na Prática**

A metodologia não é um guia passo a passo, mas um conjunto de procedimentos sistemáticos que direcionam a exploração de um alvo.

- A abordagem e as ferramentas variam conforme o ambiente.
- O foco é encontrar vulnerabilidades de forma eficiente.
- A enumeração bem planejada economiza tempo e aumenta as chances de sucesso.

Em suma, a metodologia de enumeração é um processo dinâmico que equilibra estrutura e adaptação ao alvo para maximizar a coleta de informações e a identificação de vulnerabilidades.

# OSINT - Reconhecimento de Domínios

## Introdução
A coleta de informações de domínio é uma etapa essencial em testes de penetração. Não se trata apenas da descoberta de subdomínios, mas de toda a presença online da empresa, identificando tecnologias e estruturas utilizadas para a prestação de serviços.

## Coleta Passiva de Informações
A coleta passiva é realizada sem interações diretas com a empresa-alvo, garantindo que o processo permaneça discreto. Utilizamos serviços de terceiros para obter insights sem alertar a organização.

### Passos Iniciais
1. Examinar o site principal da empresa.
2. Analisar os textos e identificar tecnologias empregadas.
3. Entender os serviços prestados e suas necessidades técnicas.

## Identificação de Presença Online
Após compreender os serviços da empresa, podemos investigar sua infraestrutura digital através de:

### Certificados SSL
- O certificado SSL do domínio principal pode conter múltiplos subdomínios.
- Usamos **crt.sh** para consultar logs de transparência de certificados:
  ```bash
  curl -s "https://crt.sh/?q=inlanefreight.com&output=json" | jq .
  ```
- Podemos filtrar os subdomínios exclusivos:
  ```bash
  curl -s "https://crt.sh/?q=inlanefreight.com&output=json" | jq . | grep name | cut -d":" -f2 | grep -v "CN=" | cut -d'"' -f2 | sort -u
  ```

## Identificação de Hosts
Após a descoberta de subdomínios, identificamos quais hosts estão diretamente acessíveis:
```bash
for i in $(cat subdomainlist); do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f1,4; done
```

## Uso do Shodan
Após identificar os IPs, podemos usá-los para buscar informações detalhadas no Shodan:
```bash
for i in $(cat ip-addresses.txt); do shodan host $i; done
```

### Exemplo de Saída
```
10.129.24.93
City: Berlin
Country: Germany
Organization: InlaneFreight
Open Ports: 80/tcp (nginx), 443/tcp (nginx)
```


## Registros DNS - Informações de Domínio

Os registros DNS são fundamentais para o funcionamento da rede, permitindo resolver domínios em endereços IP e oferecendo informações sobre e-mail, servidores e segurança. A consulta foi feita utilizando o comando `dig` para o domínio `inlanefreight.com`.

## Comando Executado:
`dig any inlanefreight.com`

Este comando retorna uma série de registros relacionados ao domínio, incluindo IPs, servidores de e-mail, servidores de nome, entre outros.

## Resultados Principais:

- **A (Address Record)**: Este registro mapeia um nome de domínio para um endereço IP. No caso, vemos dois endereços IPs associados ao domínio:
  - `10.129.27.33`
  - `10.129.95.250`

- **MX (Mail Exchange)**: Define os servidores de e-mail responsáveis pela entrega de e-mails para o domínio. Os registros MX encontrados apontam para servidores do Google:
  - `aspmx.l.google.com`
  - `aspmx2.googlemail.com`
  - Outros registros relacionados ao Google para garantir a entrega de e-mails.

- **NS (Name Server)**: Registros de servidores de nome que ajudam a resolver o FQDN (Fully Qualified Domain Name) para endereços IP. Isso indica os servidores que gerenciam as resoluções do domínio:
  - `ns.inwx.net`
  - `ns2.inwx.net`
  - `ns3.inwx.eu`

- **TXT (Text Record)**: Contém informações adicionais sobre o domínio, como chaves de verificação e configurações de segurança de e-mail (SPF, DMARC, DKIM). Exemplos de registros encontrados:
  - **Verificações**: `google-site-verification`, `atlassian-domain-verification`, etc.
  - **SPF (Sender Policy Framework)**: Um registro SPF ajuda a validar a origem dos e-mails enviados para evitar falsificação. Exemplo: `v=spf1 include:mailgun.org include:_spf.google.com ~all`
  - **Verificação de domínio**: Usada para confirmar que o domínio pertence a um serviço específico (como Google, Atlassian).

- **SOA (Start of Authority)**: Este registro contém informações sobre a zona DNS, como o servidor responsável pelo domínio e os tempos de atualização.
  - Exemplo: `ns.inwx.net. hostmaster.inwx.net. 2021072600 10800 3600 604800 3600`

## Informações de Interesse Adicional:
- **Provedores**: Os registros TXT revelam alguns serviços importantes usados pelo domínio:
  - **Google Gmail**: Indica que o Google é utilizado para gerenciamento de e-mails.
  - **Atlassian**: Usado para desenvolvimento e colaboração de software, como Jira e Confluence.
  - **LogMeIn**: Plataforma de acesso remoto, crucial para gestão de infraestrutura e acesso a sistemas.
  - **Mailgun**: Serviço de API de e-mail, que pode ser explorado em busca de vulnerabilidades.
  - **Outlook (Microsoft)**: Sugerindo o uso de Office 365 para gerenciamento de documentos e nuvem.
  - **INWX**: Provedor de hospedagem onde o domínio foi registrado.

## Pontos de Segurança:
- **Risco de Comprometimento**: Se for possível acessar plataformas como **LogMeIn** através de métodos como reutilização de senha, um atacante poderia ganhar controle remoto sobre sistemas vitais.
- **Exploração de API**: O serviço **Mailgun** pode ser alvo de ataques como IDOR ou SSRF se vulnerabilidades forem encontradas em suas interfaces de API.

Esses registros DNS fornecem uma visão importante dos serviços e infraestrutura que o domínio utiliza, e podem ser explorados para diferentes fins, como exploração de vulnerabilidades ou coleta de informações sobre a empresa.


## Conclusão
A coleta passiva de informações fornece um panorama detalhado da infraestrutura de uma empresa sem a necessidade de varreduras ativas. Isso permite um planejamento mais eficiente das próximas etapas do teste de penetração, garantindo um reconhecimento aprofundado da superfície de ataque.

# **Recursos de Nuvem**

O uso de nuvem, como **AWS**, **GCP**, **Azure** e outros, é essencial para muitas empresas hoje, permitindo que elas trabalhem de qualquer lugar com uma infraestrutura centralizada. No entanto, as empresas ainda precisam estar atentas às configurações de segurança, pois as configurações inadequadas podem tornar seus recursos vulneráveis, especialmente no caso de armazenamento em nuvem, como **S3 buckets (AWS)**, **blobs (Azure)** e **cloud storage (GCP)**. Se configurados de forma errada, esses recursos podem ser acessados sem autenticação.

### **Pesquisa de Recursos de Nuvem**

A pesquisa e identificação de recursos de nuvem, como servidores e armazenamento, pode ser feita de várias formas, incluindo comandos de terminal e técnicas de pesquisa no Google:

#### **Exemplo de Comando:**


`for i in $(cat subdomainlist); do host $i | grep "has address" | grep inlanefreight.com | cut -d" " -f1,4; done`

Esse comando busca subdomínios associados a um domínio e exibe seus respectivos endereços IP. O resultado pode incluir URLs de armazenamento em nuvem, como **AWS S3**, com o endereço `s3-website-us-west-2.amazonaws.com` (exemplo de armazenamento em nuvem).

#### **Pesquisa no Google**:

Você pode usar o Google para encontrar arquivos armazenados na nuvem de uma empresa, utilizando **Google Dorks**. Exemplos de operadores úteis são:

- **`inurl:`** — Restringe a pesquisa ao URL.
- **`intext:`** — Restringe a pesquisa ao texto da página.

Esses links frequentemente levam a arquivos como PDFs, documentos de texto e até códigos. Esses arquivos podem ser armazenados em servidores de nuvem, como AWS, Azure e GCP, sem autenticação adequada.

#### **Ferramentas de Pesquisa para Recursos em Nuvem**:

- **Domain.glass**: Ajuda a encontrar informações sobre a infraestrutura da empresa.
- **GrayHatWarfare**: Permite pesquisas sobre recursos de armazenamento em nuvem, classificando e filtrando por formato de arquivo.

#### **Dicas Adicionais**:

- Empresas frequentemente usam abreviações no nome de seus recursos de nuvem.
- A pesquisa simultânea de arquivos pode revelar novos armazenamentos em nuvem.

### **Vazamento de Chaves SSH**

Erros humanos podem levar ao vazamento de chaves **SSH**, que são usadas para autenticação em servidores. Quando uma chave privada SSH vaza, qualquer pessoa pode fazer login em servidores sem precisar de uma senha, comprometendo a segurança da empresa. Este tipo de erro geralmente ocorre quando os funcionários estão sobrecarregados ou sob pressão, resultando em falhas na segurança.