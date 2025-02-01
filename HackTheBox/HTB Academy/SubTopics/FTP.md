O **FTP (File Transfer Protocol)** é um protocolo padrão para transferência de arquivos entre um cliente e um servidor. Ele é amplamente usado para upload e download de arquivos em servidores web, servidores internos de empresas e até mesmo em redes domésticas.

Apesar de ser funcional, o FTP **não é seguro** por padrão, pois transmite dados em **texto claro** (incluindo senhas), tornando-se um alvo fácil para ataques.

---

## **1. O Que é FTP?**

O **FTP** permite que usuários enviem e recebam arquivos de um servidor remoto. Ele opera no **modelo cliente-servidor**, onde um cliente se conecta a um servidor FTP para enviar, baixar ou gerenciar arquivos.

**Portas padrão:**

- **21** → Controle da conexão FTP.
- **20** → Transferência de arquivos (modo ativo).

🔹 **Principais características:**  
✅ Permite envio e download de arquivos.  
✅ Pode ser acessado por navegadores, linha de comando ou programas como **FileZilla**.  
✅ Suporta autenticação com usuário e senha (mas sem criptografia por padrão).  
✅ Pode operar nos modos **ativo** ou **passivo**.

---

## **2. Como Usar o FTP?**

### **A) Acessar um Servidor FTP via Linha de Comando**

Conectar-se a um servidor FTP:

`ftp IP_do_Servidor`

📌 **Exemplo:**

`ftp 192.168.1.100`

Digite o **usuário** e a **senha** quando solicitado.

### **B) Comandos Básicos do FTP**

🔹 **Navegação:**

```
ls       # Lista arquivos 
cd pasta  # Entra na pasta 
pwd      # Mostra diretório atual

```

🔹 **Transferência de Arquivos:**

`get arquivo.txt   # Baixa arquivo put arquivo.txt   # Envia arquivo`

🔹 **Encerrar Conexão:**

`bye  # Sai do FTP exit # Alternativa para sair`

---

### **C) Usar FTP com FileZilla**

1️⃣ Abra o **FileZilla**.  
2️⃣ Em **Host**, digite o endereço do servidor FTP.  
3️⃣ Insira **usuário e senha**.  
4️⃣ Clique em **Conectar**.

Agora, você pode **arrastar e soltar arquivos** para transferi-los entre seu computador e o servidor.

---

## **3. Modos de Funcionamento do FTP**

### **A) Modo Ativo**

- O **cliente** inicia a conexão na porta 21.
- O **servidor** usa a porta 20 para enviar arquivos.
- 🔴 **Problema:** Firewalls podem bloquear a conexão.

### **B) Modo Passivo**

- O **cliente** se conecta na porta 21.
- O **servidor** escolhe uma porta aleatória para transferir arquivos.
- ✅ **Solução mais compatível com firewalls.**

---

## **4. Tipos de FTP**

### **A) FTP Simples (Padrão)**

- **Não criptografa dados**.
- **Inseguro para uso na internet**.

### **B) FTPS (FTP Secure)**

- Usa **TLS/SSL** para criptografia.
- Mais seguro que o FTP padrão.

### **C) SFTP (SSH File Transfer Protocol)**

- **Não é FTP!** Usa SSH para transferir arquivos.
- **Muito mais seguro** que FTP tradicional.

---

## **5. Principais Ataques Contra FTP**

### **A) Sniffing (Captura de Pacotes)**

- Como FTP transmite dados sem criptografia, atacantes podem capturar senhas.
- **Ferramentas:** [[Wireshark]], [[Tcpdump]].
- **Mitigação:** Use **FTPS** ou **SFTP**.

### **B) Ataque de Força Bruta**

- Tentativa de adivinhar senhas.
- **Ferramentas:** [[Hydra]], [[Medusa]], [[Ncrack]].
- **Mitigação:** Senhas fortes, limitar tentativas de login.

📌 **Exemplo de ataque com Medusa:**

`medusa -h 192.168.1.100 -u ftpuser -P wordlist.txt -M ftp -t 5`

### **C) Exploração de Vulnerabilidades**

- Servidores FTP desatualizados podem ter falhas exploráveis.
- **Ferramentas:** Nmap, Metasploit.

📌 **Exemplo de verificação de vulnerabilidades:**

`nmap -sV --script ftp-vuln* 192.168.1.100`

### **D) Ataques de Permissão e Upload de Arquivos Maliciosos**

- Se o servidor permitir uploads, atacantes podem enviar **backdoors**.
- **Mitigação:** Restringir permissões de escrita no servidor FTP.

---

## **6. Configuração Segura do Servidor FTP**

### **A) Alterar a Porta do FTP**

No arquivo de configuração (`/etc/vsftpd.conf`):

ini

`listen_port=2121`

Reinicie o serviço:

`systemctl restart vsftpd`

### **B) Bloquear Usuário Root no FTP**

ini

`ftpusers=root`

### **C) Habilitar FTP Seguro (FTPS ou SFTP)**

Para SFTP (usando SSH):

`sftp usuario@192.168.1.100`

Para FTPS (com SSL/TLS), configure no `vsftpd.conf`:

ini

`ssl_enable=YES`

---

## **7. Exemplos Práticos de FTP**

### **A) Listar Arquivos em um Servidor FTP**

`ftp 192.168.1.100 ls`

### **B) Baixar um Arquivo**

`get backup.zip`

### **C) Enviar um Arquivo**

`put relatório.pdf`

### **D) Usar Wget para Baixar Arquivos de um Servidor FTP**

`wget ftp://usuario:senha@192.168.1.100/arquivo.zip`

---

## **Conclusão**

O FTP ainda é muito usado, mas tem **grandes falhas de segurança**. O ideal é sempre utilizar **FTPS** ou **SFTP** para proteger os dados. Se precisar usar FTP comum, recomenda-se aplicá-lo **apenas em redes internas** e com **medidas extras de segurança**.

🔥 **Dica:** Se quiser testar ataques contra FTP, use máquinas virtuais no **Hack The Box** ou **TryHackMe**!