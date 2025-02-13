# Conversão de Endereços de Rede (NAT)
Dispositivos em redes locais possuem endereços IP privados para se comunicarem internamente. Para acessar a internet, precisam de um único IP público, fornecido pelo roteador através do NAT (Network Address Translation). O NAT traduz IPs privados em públicos e vice-versa, operando nas camadas de Internet e Transporte do modelo TCP/IP.

## Endereços IP
### IPs Privados:
- Atribuídos pelo roteador
- Válidos apenas dentro da rede local
- Uso gratuito
- Intervalos:
  - `10.0.0.0 - 10.255.255.255`
  - `172.16.0.0 - 172.31.255.255`
  - `192.168.0.0 - 192.168.255.255`

### IPs Públicos:
- Atribuídos pelo ISP/IANA
- Únicos na internet
- Podem ter custo
- Intervalos:
  - `1.0.0.0 - 9.255.255.255`
  - `11.0.0.0 - 126.255.255.255`
  - `128.0.0.0 - 172.15.255.255`
  - `172.32.0.0 - 192.167.255.255`
  - `192.169.0.0 - 233.255.255.255`

# Protocolos de Rede
## DHCP (Dynamic Host Configuration Protocol)
O DHCP automatiza a configuração de dispositivos na rede, atribuindo dinamicamente endereços IP, servidores DNS e gateways.
- **Portas:** UDP 67 (servidores), UDP 68 (clientes)

### Exemplo de uso:
- Quando um celular se conecta ao Wi-Fi, o roteador fornece automaticamente um IP via DHCP.

## ARP (Address Resolution Protocol)
O ARP converte endereços IP em endereços MAC para comunicação dentro da mesma rede. 
- **Porta:** Nenhuma

### Exemplo de uso:
- Quando um PC quer enviar um pacote para outro na LAN, ele usa o ARP para descobrir o MAC de destino.

## Telnet
Permite conexão remota via linha de comando, mas sem criptografia.
- **Porta:** TCP 23

### Exemplo de uso:
- Conectar-se a um switch de rede para configurar regras.

## SSH (Secure Shell)
Protocolo seguro para acesso remoto via linha de comando.
- **Porta:** TCP 22

### Exemplo de uso:
- Administradores usam SSH para acessar servidores Linux remotamente.

## POP3 (Post Office Protocol)
Usado para baixar e-mails do servidor para um dispositivo local. 
- **Portas:**
  - TCP/UDP 110 (não criptografado)
  - TCP/UDP 995 (SSL/TLS)

### Exemplo de uso:
- Clientes de e-mail como Outlook baixam mensagens via POP3.

## IMAP (Internet Message Access Protocol)
Permite acessar e-mails diretamente no servidor, sem necessidade de download.
- **Portas:**
  - TCP 143 (não criptografado)
  - TCP 993 (SSL/TLS)

### Exemplo de uso:
- A sincronização de e-mails entre dispositivos usando Gmail.

## SMTP (Simple Mail Transfer Protocol)
Usado para envio de e-mails.
- **Portas:**
  - TCP/UDP 25 (não criptografado)
  - TCP/UDP 587 (TLS)

### Exemplo de uso:
- Quando um e-mail é enviado do Outlook para outro servidor.

# Resumo das Portas
| Protocolo | Porta |
|-----------|-------|
| DHCP (servidor) | UDP 67 |
| DHCP (cliente) | UDP 68 |
| ARP | Nenhuma |
| Telnet | TCP 23 |
| SSH | TCP 22 |
| POP3 | TCP/UDP 110, 995 (SSL/TLS) |
| IMAP | TCP 143, 993 (SSL/TLS) |
| SMTP | TCP/UDP 25, 587 (TLS) |

Esses protocolos e portas são essenciais para a segurança cibernética e devem ser memorizados, pois são frequentemente abordados em entrevistas e práticas profissionais.

Próximo Modulo [[A evolução dos protocolos de segurança sem fio]]