O Nmap é usado para identificar e escanear sistemas na rede. É uma parte importante do diagnóstico de rede e avaliação de sistemas conectados à rede.

---

# Enumeração

A **enumeration** é a etapa mais crítica no processo de hacking. O objetivo não é apenas acessar um sistema, mas descobrir todas as formas possíveis de atacá-lo. Isso requer não apenas ferramentas, mas conhecimento sobre como interpretar e utilizar as informações coletadas.

### Pontos principais:

1. **Ferramentas são auxiliares, não substitutos do conhecimento.** É essencial entender como os serviços funcionam, a sintaxe necessária e como interagir com eles.
2. **O foco é obter o máximo de informações possível.** Mais informações facilitam a identificação de vetores de ataque.
3. **Importância da interação ativa.** Entender os serviços ajuda a identificar configurações incorretas ou negligência de segurança.
4. **Manual enumeration é essencial.** Ferramentas automatizadas podem ser limitadas por medidas de segurança, como tempo limite ou portas mal interpretadas.
5. **Conhecimento técnico economiza tempo.** Saber mais sobre os serviços evita erros e acelera o progresso.

**Conclusão:** A chave da enumeration é entender as tecnologias e usar uma abordagem manual quando necessário para obter informações detalhadas e identificar vulnerabilidades de forma eficaz.

---

# Introdução ao Nmap;

O **Network Mapper (Nmap)** é uma ferramenta de código aberto para análise de redes e auditoria de segurança, escrita em C, C++, Python e Lua. É amplamente utilizada para identificar hosts, serviços, versões de aplicativos e sistemas operacionais em uma rede, além de detectar configurações de firewalls, filtros de pacotes e sistemas de detecção de intrusão (IDS).

### Principais usos:

- Auditoria de segurança de redes.
- Testes de penetração.
- Verificação de firewalls e IDS.
- Mapeamento de redes.
- Identificação de portas abertas.
- Avaliação de vulnerabilidades.

---

### Técnicas e recursos:

O Nmap oferece várias técnicas de varredura, como:

- **Descoberta de hosts**: Identifica máquinas ativas na rede.
- **Varredura de portas**: Detecta portas abertas ou filtradas.
- **Enumeração de serviços**: Identifica serviços e versões em execução.
- **Detecção de SO**: Determina o sistema operacional do alvo.
- **Nmap Scripting Engine (NSE)**: Permite interação programável com o serviço.

---

### Tipos de escaneamento:

1. **TCP SYN Scan (-sS)** (popular e eficiente):
    - Envia pacotes SYN sem completar o handshake TCP.
    - Respostas:
        - **SYN-ACK**: Porta **aberta**.
        - **RST**: Porta **fechada**.
        - Nenhuma resposta: Porta **filtrada**.
2. **Outros escaneamentos**: TCP Connect (-sT), UDP (-sU), Null (-sN), Xmas (-sX), entre outros.

---
# Host Discovery

### **Principais Conceitos:**

1. **Objetivo da Descoberta de Host**: Identificar sistemas ativos na rede para testes de penetração.
2. **Armazenamento de Resultados**: Importante para documentar, comparar e relatar resultados.
3. **Varredura de Intervalo de Rede**: Uso de intervalos de IP (CIDR) e varreduras específicas.
4. **Trabalho com Listas de IPs**: Facilita a varredura em redes maiores com listas predefinidas.
5. **Análise de Respostas**: Avaliação dos pacotes enviados e recebidos para determinar a atividade do host.
6. **Diferentes Métodos de Descoberta de Host**:
    - Solicitações de eco ICMP (padrão com `-sn`).
    - Detecção ARP e ICMP.
    - Desativação de pings ARP para varreduras específicas.

### **Comandos Importantes do Nmap:**

- `-sn`: Desativa a varredura de portas e realiza apenas a descoberta de hosts.
- `-oA`: Salva os resultados em todos os formatos (`.nmap`, `.gnmap`, `.xml`).
- `-PE`: Força o uso de solicitações ICMP Echo Request.
- `--packet-trace`: Exibe pacotes enviados e recebidos.
- `--disable-arp-ping`: Desativa solicitações ARP, focando em ICMP.
- `--reason`: Explica o motivo dos resultados exibidos.

### **Casos de Uso com Exemplos:**

- **Varredura de uma Rede Inteira**:
    
    `sudo nmap 10.129.2.0/24 -sn -oA tnet`
    
    Identifica hosts ativos em uma rede /24 (255 IPs).
    
- **Varredura com Lista de IPs**:
    
    `sudo nmap -sn -oA tnet -iL hosts.lst`
    
    Usa uma lista de IPs para verificar atividade.
    
- **Verificar Intervalo Específico de IPs**:
    
    `sudo nmap -sn -oA tnet 10.129.2.18-20`
    
    Varre apenas os IPs especificados.
    
- **Varredura de IP Único com ICMP Echo Request**:
    
    `sudo nmap 10.129.2.18 -sn -oA host -PE --packet-trace`
    
### **Destaques Técnicos:**

1. **Solicitação ICMP Echo Request (`-PE`)**:
    
    - Útil quando ARP pings são bloqueados ou indesejados.
    - Força o uso de pacotes ICMP para verificar a atividade.
    
2. **Análise Avançada com `--packet-trace`**:
    
    - Visualiza detalhes de pacotes enviados/recebidos.
    - Auxilia na depuração de resultados inesperados.
    
3. **Razões dos Resultados com `--reason`**:
    
    - Explica o porquê de um host ser considerado "ativo" ou "inativo".
    
4. **Desativação de ARP com `--disable-arp-ping`**:
    
    - Para redes onde ARP é desativado ou ICMP é preferido.

### **Dicas Práticas:**

- Use o comando com `grep` e `cut` para filtrar apenas os IPs ativos:
    
    `| grep for | cut -d" " -f5`
    
- Documente sempre os resultados para análise futura e relatórios.

---

# Host and Port Scanning

### **Escaneamento de Hosts e Portas**

Compreender como ferramentas como o Nmap funcionam é essencial para interpretar corretamente os resultados. Após confirmar que o alvo está ativo, o objetivo é obter informações detalhadas, como:

- **Portas abertas e serviços associados**
- **Versões de serviços**
- **Sistema operacional**

#### **Estados das Portas**

1. **Open**: Conexão estabelecida (TCP, UDP ou SCTP).
2. **Closed**: Porta fechada; resposta contém o flag RST.
3. **Filtered**: Sem resposta ou erro, indicando possível firewall.
4. **Unfiltered**: Porta acessível, mas estado indefinido (TCP-ACK).
5. **Open | Filtered**: Falta de resposta sugere proteção por firewall.
6. **Closed | Filtered**: Estado inconclusivo (ocorre em varreduras IP ID idle).

---

### **Descobrindo Portas TCP Abertas**

O Nmap, por padrão, escaneia as 1000 portas TCP mais frequentes usando o **SYN Scan** (`-sS`), que é configurado como padrão ao ser executado como root. Sem privilégios, usa o **TCP Connect Scan** (`-sT`).

#### **Opções de Escaneamento**

- **Top 10 portas**:
    
    `sudo nmap 10.129.2.28 --top-ports=10`
    
    Escaneia as portas mais comuns, retornando estados como "open" ou "filtered".
    
- **Porta específica com rastreamento de pacotes**:
    
    `sudo nmap 10.129.2.28 -p 21 --packet-trace -Pn -n --disable-arp-ping`
    
    Mostra pacotes enviados e recebidos.
    

#### **TCP Connect Scan (`-sT`)**

- Realiza o handshake completo do TCP.
- Alta precisão, mas menos furtivo (gera logs).
- Útil contra firewalls que permitem conexões de saída.

Exemplo:

`sudo nmap 10.129.2.28 -p 443 --packet-trace --disable-arp-ping -Pn -n -sT`

Retorna informações detalhadas, incluindo estado da porta, como `open` com resposta `SYN-ACK`.

---

### **Considerações**

O **SYN Scan** é mais rápido e furtivo, enquanto o **TCP Connect Scan** é mais detalhado e confiável para situações específicas. Ambas as abordagens têm vantagens dependendo do contexto, como restrições de rede e ferramentas de defesa.

### Portas Filtradas

- **Causa:** Firewall bloqueando pacotes.
- **Comportamento:**
    - Pacotes enviados não recebem resposta (são descartados).
    - Nmap reenvia pacotes (padrão: 10 tentativas) devido ao `--max-retries`.
    - Exemplo:
        
        `sudo nmap 10.129.2.28 -p 139 --packet-trace -n --disable-arp-ping -Pn`
        
    - Resultado: Porta **filtrada** (sem confirmação ou rejeição explícita).

---

### **Portas Rejeitadas**

- **Causa:** Firewall configurado para retornar erro explícito.
- **Comportamento:**
    - Recebe-se um pacote ICMP com tipo 3 e código 3 ("Port Unreachable").
    - Exemplo:
        
        `sudo nmap 10.129.2.28 -p 445 --packet-trace -n --disable-arp-ping -Pn`
        
    - Resultado: Porta **filtrada** (mas detectado ICMP de rejeição).

---

### **Scan UDP**

- **Características:**
    - **Mais lento:** UDP é sem estado, e as respostas dependem da configuração da aplicação.
    - **Estados:**
        - `open`: Resposta recebida.
        - `closed`: ICMP com erro.
        - `open|filtered`: Sem resposta (não se sabe se é aberto ou filtrado).
    - Exemplo de escaneamento básico:
        
        `sudo nmap 10.129.2.28 -F -sU`
        

#### **Exemplos específicos de portas UDP:**

1. **Porta aberta:**
    
    `sudo nmap 10.129.2.28 -sU -Pn -n --disable-arp-ping --packet-trace -p 137 --reason`
    
    - Resposta UDP recebida: Estado **open**.
2. **Porta fechada:**
    
    `sudo nmap 10.129.2.28 -sU -Pn -n --disable-arp-ping --packet-trace -p 100 --reason`
    
    - ICMP "Port Unreachable": Estado **closed**.
3. **Porta open|filtered:**
    
    `sudo nmap 10.129.2.28 -sU -Pn -n --disable-arp-ping --packet-trace -p 138 --reason`
    
    - Sem resposta, marcado como **open|filtered**.

---

### **Scan de Versões (-sV)**

- **Utilidade:** Identificar detalhes adicionais sobre serviços e versões nas portas abertas.
- **Comando:**
    
    `sudo nmap 10.129.2.28 -sV`

---

# Salvando os Resultados

### **1. Formatos de Saída do Nmap**

- **Saída normal (-oN)**: Gera uma saída humanamente legível e salva com extensão `.nmap`.
    
- **Saída Grepable (-oG)**: Produz uma saída formatada para ser filtrada com ferramentas como `grep`, salva com extensão `.gnmap`.
    
- **Saída XML (-oX)**: Ideal para scripts ou geração de relatórios detalhados, salva com extensão `.xml`.
    
- **Opção combinada (-oA)**: Salva os resultados em todos os três formatos simultaneamente, com o mesmo prefixo para o nome dos arquivos.
    

---

### **2. Exemplo de Comando para Salvar Resultados**

`sudo nmap 10.129.2.28 -p- -oA target`

Este comando:

- Escaneia todas as portas (`-p-`) do IP `10.129.2.28`.
- Salva os resultados nos formatos `.nmap`, `.gnmap` e `.xml`, com o prefixo `target`.

Após a execução, os arquivos gerados estarão no diretório atual:

`target.nmap  target.gnmap  target.xml`

---

### **3. Analisando os Resultados**

- **Saída Normal (`target.nmap`)**: Formato simples e direto, útil para revisões rápidas.  
    
    `PORT   STATE SERVICE 22/tcp open  ssh 25/tcp open  smtp 80/tcp open  http`
    
- **Saída Grepable (`target.gnmap`)**:  
    Formatada para facilitar busca e filtragem com scripts.
    
    `Host: 10.129.2.28 ()	Ports: 22/open/tcp//ssh///, 25/open/tcp//smtp///, 80/open/tcp//http///`
    
- **Saída XML (`target.xml`)**:  
    Estruturada para ser processada por ferramentas ou convertida em HTML.
    
---

### **4. Convertendo XML em HTML**

Com a ferramenta **xsltproc**, podemos transformar o arquivo XML em um relatório HTML.  
Comando:

`xsltproc target.xml -o target.html`

O arquivo `target.html` pode ser aberto em um navegador, apresentando os resultados de forma clara e detalhada, ideal para relatórios profissionais ou documentação.

---
# Enumeração de serviço

A enumeração de serviço é crucial para determinar o aplicativo e sua versão, o que pode ajudar a encontrar vulnerabilidades conhecidas e analisar o código-fonte dessa versão. Conhecer a versão exata facilita a busca por exploits mais precisos para o serviço e o sistema operacional alvo.

**Detecção de Versão de Serviço**

Primeiro, é recomendável realizar uma varredura rápida de portas para ter uma visão geral sem gerar muito tráfego, evitando a detecção. A varredura de versão (-sV) permite verificar os serviços e suas versões nas portas abertas (-p-). Para visualização do progresso, pode-se pressionar a barra de espaço durante a varredura.

**Comando Exemplo:**

`sudo nmap 10.129.2.28 -p- -sV`

**Opções:**

- `-p-`: Verifica todas as portas.
- `-sV`: Realiza a detecção de versão.
- `--stats-every=5s`: Exibe o progresso da verificação a cada 5 segundos.

**Aumentar Verbosidade:** Para mais detalhes durante o escaneamento, use o parâmetro `-v`.

**Captura de Banner**

Após a verificação, o Nmap exibe as portas abertas com seus respectivos serviços e versões. Se o Nmap não conseguir identificar a versão via banners, ele tenta com um sistema de correspondência de assinaturas, o que pode aumentar o tempo de varredura.

**Exemplo de Resultados de Nmap:**

`PORT      STATE    SERVICE      VERSION
	22/tcp    open     ssh          OpenSSH 7.6p1 Ubuntu 
	25/tcp    open     smtp         Postfix smtpd 
	80/tcp    open     http         Apache httpd 2.4.29`

**Ferramentas Complementares**

1. **Tcpdump:** Pode ser utilizado para interceptar o tráfego de rede e capturar mais informações do que o Nmap, como detalhes que não foram mostrados durante a varredura.
    
2. **Netcat (nc):** Permite conectar-se manualmente ao serviço e pegar o banner diretamente.
    

**Exemplo de Uso do Tcpdump:**

`sudo tcpdump -i eth0 host 10.10.14.2 and 10.129.2.28`

**Exemplo de Uso do Netcat:**

`nc -nv 10.129.2.28 25`

**Conclusão**

A enumeração de serviço é um processo vital para identificar os serviços em execução em um sistema e suas versões, ajudando na busca por vulnerabilidades. Ferramentas como Nmap, Tcpdump e Netcat são fundamentais para coletar essas informações, seja pela verificação de banners ou pela interceptação direta do tráfego.

---

# Nmap Scripting Engine (NSE)

O **Nmap Scripting Engine (NSE)** é um recurso poderoso que permite realizar varreduras e detectar vulnerabilidades de forma automatizada através de scripts personalizados em Lua. Ele oferece uma grande variedade de scripts categorizados, cada um projetado para uma tarefa específica.

### Categorias de Scripts do NSE:

1. **auth**: Determinação de credenciais de autenticação.
2. **broadcast**: Descoberta de hosts através de transmissão e adição automática às verificações.
3. **brute**: Força bruta para login nos serviços.
4. **default**: Scripts padrão executados com a opção `-sC`.
5. **discovery**: Identificação de serviços acessíveis.
6. **dos**: Testes de negação de serviço, que podem prejudicar o serviço alvo.
7. **exploit**: Exploração de vulnerabilidades conhecidas.
8. **external**: Scripts que utilizam serviços externos.
9. **fuzzer**: Identificação de vulnerabilidades com manipulação de pacotes.
10. **intrusive**: Scripts que podem afetar o sistema de destino.
11. **malware**: Verificação de malware no sistema alvo.
12. **safe**: Scripts defensivos, sem acesso intrusivo ou destrutivo.
13. **version**: Detecção de versões de serviços.
14. **vuln**: Identificação de vulnerabilidades específicas.

### Comandos para Executar Scripts NSE:

- **Scripts padrão**:
    
    `sudo nmap <target> -sC`
    
- **Especificar categoria de scripts**:
    
    `sudo nmap <target> --script <category>`
    
- **Especificar scripts individuais**:
    
    `sudo nmap <target> --script <script-name>,<script-name>,...`
    

### Exemplos Práticos:

1. **Exemplo de Detecção de Banner e Comandos SMTP**:
    
    - Comando:
        
        `sudo nmap 10.129.2.28 -p 25 --script banner,smtp-commands`
        
    - **Resultado**: O script `banner` revela a versão do serviço (Postfix no Ubuntu), e o `smtp-commands` lista comandos suportados pelo servidor SMTP, como `PIPELINING`, `VRFY`, `STARTTLS`, etc. Isso pode ajudar a descobrir usuários existentes.
2. **Exemplo de Scan Agressivo**:
    
    - Comando:
        
        `sudo nmap 10.129.2.28 -p 80 -A`
        
    - **Resultado**: O Nmap realiza uma varredura agressiva, identificando o servidor web (Apache 2.4.29), aplicação (WordPress 5.3.4) e título da página (`blog.inlanefreight.com`), além de fornecer uma estimativa do sistema operacional (Linux).
3. **Exemplo de Detecção de Vulnerabilidades**:
    
    - Comando:
        
        `sudo nmap 10.129.2.28 -p 80 -sV --script vuln`
        
    - **Resultado**: O script `vuln` verifica o servidor web e seu aplicativo (WordPress), procurando vulnerabilidades conhecidas. Identifica a versão do Apache (2.4.29) e vulnerabilidades específicas, como o CVE-2019-0211.

### Análise de Vulnerabilidades com Scripts:

- **http-enum**: Descobre páginas e arquivos interessantes, como `/wp-login.php` e `/readme.html`, revelando informações sobre a versão do WordPress.
- **http-wordpress-users**: Identifica usuários do WordPress, como `admin`.
- **vulners**: Verifica vulnerabilidades conhecidas associadas a serviços e versões, como os CVEs do Apache.

### Conclusão:

O NSE do Nmap é uma ferramenta robusta para automatizar testes de penetração e auditoria de segurança. Com ele, é possível identificar serviços, versões e vulnerabilidades de forma eficiente, além de executar uma série de testes para identificar falhas de segurança e expor vulnerabilidades em sistemas alvo. A utilização de diferentes categorias de scripts permite que a varredura seja personalizada conforme a necessidade do teste.

---

# Performance

O Nmap oferece diversas opções de configuração para otimizar a performance das verificações, especialmente em redes grandes ou com limitações de largura de banda. Aqui estão alguns pontos importantes abordados:

### 1. **Otimização de RTT (Round-Trip-Time)**

O valor de **RTT** define o tempo de ida e volta de um pacote entre o scanner e o alvo. Quando você otimiza o tempo limite, pode melhorar significativamente o tempo de varredura, embora, se o limite for muito curto, você pode perder informações importantes ao não obter respostas de alguns hosts.

- **Verificação padrão**: Realiza a varredura sem otimizações.
- **RTT otimizado**: Ajusta os tempos de resposta (inicial e máximo) para diminuir o tempo total da varredura.

### 2. **Máximo de Tentativas (Max Retries)**

Ao reduzir o número de tentativas (**--max-retries**) o Nmap não tenta várias vezes se a porta não responder. Isso acelera a verificação, mas pode resultar na perda de dados se o alvo tiver uma resposta mais lenta ou congestionada.

- **Verificação padrão**: Realiza tentativas múltiplas antes de desistir de uma porta.
- **Repetições reduzidas**: Tenta um número mínimo de vezes, ignorando portas que não respondem rapidamente.

### 3. **Taxa de Envio de Pacotes**

Com a opção **--min-rate**, você pode especificar quantos pacotes o Nmap deve enviar simultaneamente. Isso pode ser útil para redes de alta largura de banda ou quando o teste precisa ser feito rapidamente.

- **Verificação padrão**: Envia pacotes a uma taxa padrão.
- **Verificação otimizada**: Aumenta a taxa de pacotes enviados por segundo, acelerando a varredura.

### 4. **Modelos de Tempo (-T)**

Os modelos de tempo oferecem diferentes níveis de agressividade para a varredura:

- **-T 0 (paranoid)**: Muito lento, com menos chances de ser detectado por sistemas de segurança.
- **-T 1 (sneaky)**: Lento, mas mais eficiente que o modelo paranoid.
- **-T 2 (polite)**: Agressivo, mas respeitoso com a rede.
- **-T 3 (normal)**: Equilibrado, modelo padrão.
- **-T 4 (aggressive)**: Muito rápido e agressivo, pode ser detectado.
- **-T 5 (insane)**: Extremamente rápido, mas pode sobrecarregar a rede e sistemas de segurança.
### Considerações:

- A aceleração da verificação pode resultar em perda de informações importantes.
- O **-F** limita a verificação às 100 principais portas.

### Conclusão

A otimização de performance no Nmap depende do equilíbrio entre rapidez e precisão. Ajustes nas configurações de **RTT**, **número de tentativas**, **taxa de pacotes** e **modelos de tempo** podem acelerar a varredura, mas você sempre deve estar atento para não perder informações importantes ou ser detectado. Isso é essencial em ambientes de pentest, especialmente em redes de grandes dimensões ou quando há sistemas de segurança ativos.

---

# Firewall e evasão de IDS/IPS

### 1. **Firewall e IDS/IPS**

#### **Firewalls**

Firewalls são sistemas de segurança que bloqueiam ou permitem o tráfego de rede com base em regras predefinidas. Eles podem bloquear ou permitir pacotes com base no endereço IP de origem, destino, tipo de pacote e portas usadas.

- **Pacotes Dropped**: O firewall simplesmente descarta o pacote, sem enviar resposta.
- **Pacotes Rejected**: O firewall envia uma resposta indicando que o pacote foi rejeitado, geralmente com um sinalizador **RST**.

#### **IDS/IPS**

- **IDS (Intrusion Detection System)**: Sistema de monitoramento que detecta ataques com base em padrões e gera alertas.
- **IPS (Intrusion Prevention System)**: Detecta e, além disso, impede ataques automaticamente.

### 2. **Maneiras de Contornar Firewalls e IDS/IPS com Nmap**

#### **Varredura SYN (SYN Scan - `-sS`)**

Este é o método mais básico de varredura, onde o Nmap envia pacotes SYN para as portas alvo e aguarda a resposta (SYN-ACK para portas abertas, RST para portas fechadas).

- **Problema**: Firewalls podem bloquear pacotes SYN de redes externas.
- **Exemplo**:
    
    bash
    
    CopyEdit
    
    `sudo nmap 10.129.2.28 -p 21,22,25 -sS -Pn`
    
- **Ação**: Use este tipo de varredura em redes onde o firewall não bloqueia pacotes SYN.

#### **Varredura ACK (ACK Scan - `-sA`)**

A varredura ACK envia pacotes com o sinalizador ACK, que são mais difíceis de bloquear por firewalls, pois o firewall não pode determinar se a conexão foi iniciada pela rede interna ou externa.

- **Exemplo**:
    
    bash
    
    CopyEdit
    
    `sudo nmap 10.129.2.28 -p 21,22,25 -sA -Pn`
    
- **Resultado esperado**: O firewall pode responder com **RST** para portas abertas ou **nada** para portas filtradas.

#### **Evasão com Decoys (`-D RND:n`)**

Com o método **Decoy**, o Nmap envia pacotes de múltiplos IPs aleatórios para disfarçar o seu endereço de origem. Isso pode enganar sistemas IDS/IPS que monitoram a origem dos pacotes.

- **Exemplo**:
    
    bash
    
    CopyEdit
    
    `sudo nmap 10.129.2.28 -p 80 -sS -Pn -D RND:5`
    
    Isso cria 5 IPs de origem aleatórios, com o seu IP real no meio, dificultando a detecção.
    
- **Ação**: Use Decoys para confundir sistemas de monitoramento e evitar que seu IP real seja bloqueado.
    

#### **Escaneamento por IP de Origem Diferente (`-S`)**

Você pode especificar um IP de origem diferente (como o IP de outro servidor VPS) para mascarar a origem do ataque e evitar o bloqueio do seu IP principal.

- **Exemplo**:
    
    bash
    
    CopyEdit
    
    `sudo nmap 10.129.2.28 -p 445 -S 10.129.2.200 -e tun0`
    
- **Resultado esperado**: O Nmap usará o IP `10.129.2.200` como origem, ajudando a evitar que o seu IP original seja detectado.

#### **Varredura com ICMP Desabilitado (`-Pn`)**

Desabilitar o uso de ICMP pode ser útil para evitar a detecção de dispositivos de monitoramento de rede que possam reagir a um **ping** de descoberta. Isso impede que você seja bloqueado por medidas simples de filtro de ping.

- **Exemplo**:
    
    bash
    
    CopyEdit
    
    `sudo nmap 10.129.2.28 -p 445 -Pn`
    
- **Ação**: Use sempre que você suspeitar que a rede de destino tem filtros ICMP habilitados.

### 3. **Testando Regras de Firewall**

#### **Exemplo de Teste com Varredura SYN**

Quando uma porta está **filtrada**, você pode não obter uma resposta para pacotes SYN enviados, indicando que o firewall está bloqueando a porta.

- **Exemplo**: Ao rodar um **SYN scan**, o Nmap pode não receber nenhuma resposta para portas filtradas.

#### **Testando com Diferentes IPs de Origem**

Caso um firewall bloqueie seu IP, você pode testar varreduras com diferentes IPs de origem para contornar essa restrição, trocando o IP com `-S`.

### 4. **Dicas de Como Agir em um Teste de Penetração**

- **Variabilidade**: Não confie apenas em um tipo de varredura. Misture varreduras SYN, ACK e Decoy para dificultar a detecção.
- **Disfarce**: Use **Decoys** e IPs de origem diferentes para enganar IDS/IPS.
- **Evitar Detecção Rápida**: Use **varreduras lentas** para evitar a detecção imediata, principalmente ao testar múltiplas portas.

### Conclusão

Essas técnicas permitem que você teste redes de forma furtiva, contornando firewalls e sistemas IDS/IPS, enquanto coleta informações detalhadas sobre as portas e serviços da rede. A chave é variar os métodos para evitar padrões detectáveis.