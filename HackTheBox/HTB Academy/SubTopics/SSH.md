## **1. O Que é SSH?**

O **SSH** substitui protocolos antigos como o **Telnet** e o **Rlogin**, que transmitiam dados em **texto puro**, permitindo que atacantes interceptassem credenciais e comandos. Com SSH, os dados são criptografados, garantindo **confidencialidade, integridade e autenticidade** durante a comunicação.

Ele opera na **porta 22 por padrão**, mas pode ser configurado para usar outras portas.

**Principais características:**  
✅ Comunicação segura e criptografada.  
✅ Suporte a autenticação por **senha** ou **chave SSH**.  
✅ Transferência segura de arquivos via **SCP** e **SFTP**.  
✅ Redirecionamento de portas para tunelamento seguro.

---

## **2. Como Utilizar o SSH?**

### **A) Acessando um Servidor Remoto**

Para conectar-se a um servidor via SSH, utilize o comando:

`ssh usuário@IP -p PORTA`

📌 **Exemplo:**

`ssh root@192.168.1.100 -p 22`

Se a autenticação for feita com senha, ele pedirá para digitá-la.

### **B) Acessando um Servidor com Chave SSH**

As chaves SSH eliminam a necessidade de senhas e aumentam a segurança.

1️⃣ **Gerar um par de chaves (pública e privada):**

`ssh-keygen -t rsa -b 4096`

2️⃣ **Copiar a chave pública para o servidor remoto:**

`ssh-copy-id usuário@IP`

Agora, você pode acessar o servidor sem digitar a senha:

`ssh usuário@IP`

### **C) Transferência de Arquivos com SSH**

Usando **SCP (Secure Copy Protocol)**:

`scp arquivo.txt usuário@IP:/caminho/destino/`

📌 **Exemplo:**

`scp backup.zip root@192.168.1.100:/home/root/`

Para transferir um diretório inteiro:

`scp -r pasta/ usuário@IP:/caminho/`

Usando **SFTP (SSH File Transfer Protocol)**:

`sftp usuário@IP`

Dentro do terminal SFTP, você pode usar comandos como `ls`, `get`, `put`, `exit`, etc.

---

## **3. Tipos de Ataques Contra SSH**

Mesmo sendo seguro, o SSH pode ser alvo de ataques se mal configurado.

### **A) Ataque de Força Bruta**

Os atacantes tentam várias senhas até encontrar a correta. Ferramentas como **Hydra, Medusa e Ncrack** são usadas para esse tipo de ataque.

📌 **Exemplo de ataque com Hydra:**

`hydra -l root -P wordlist.txt ssh://192.168.1.100`

🔹 **Mitigação:**

- Usar autenticação por **chave SSH** em vez de senha.
- Limitar tentativas de login com **fail2ban**.
- Alterar a porta padrão do SSH.

---

### **B) Ataque Man-in-the-Middle (MITM)**

Um invasor intercepta a comunicação SSH, tentando capturar credenciais.

🔹 **Mitigação:**

- Sempre verificar a **impressão digital** (fingerprint) do servidor ao conectar pela primeira vez.
- Utilizar **algoritmos de criptografia fortes**.

---

### **C) Exploração de Vulnerabilidades**

Se o servidor estiver usando uma versão desatualizada do OpenSSH, pode haver falhas exploráveis.

📌 **Exemplo:** Ataque a versões vulneráveis do OpenSSH.

`nmap -sV --script ssh-vuln* 192.168.1.100`

🔹 **Mitigação:**

- Manter o OpenSSH atualizado.
- Desativar versões antigas do protocolo SSH (ex: SSHv1).

---

### **D) Ataque de Redirecionamento de Porta (Port Forwarding Abuse)**

Um invasor com acesso ao SSH pode tunelar conexões para outros serviços na rede.

📌 **Exemplo:**

`ssh -L 8080:interna:80 user@servidor`

🔹 **Mitigação:**

- Restringir **PermitOpen** no `sshd_config`.
- Monitorar conexões com **logs**.

---

## **4. Configuração Segura do SSH**

### **A) Alterar a Porta do SSH**

No arquivo `/etc/ssh/sshd_config`, modifique:

yaml

`Port 2222`

Após isso, reinicie o serviço:

`systemctl restart sshd`

### **B) Desativar Login de Root**

No mesmo arquivo, altere:

nginx

`PermitRootLogin no`

### **C) Restringir Tentativas de Login**

Com **fail2ban**, limite tentativas de login:

`apt install fail2ban -y`

Configurar no `/etc/fail2ban/jail.local`:

ini

`[sshd] enabled = true maxretry = 3 bantime = 3600`

Reinicie:

`systemctl restart fail2ban`

---

## **5. Exemplos Práticos de SSH**

### **A) Acesso Simples**

`ssh usuario@192.168.1.100`

### **B) Encaminhamento de Porta (Port Forwarding)**

`ssh -L 8080:localhost:80 usuario@192.168.1.100`

🔹 **Explicação:** Redireciona conexões na porta 8080 para a porta 80 do servidor remoto.

### **C) Acesso sem Senha com Chaves SSH**

1️⃣ Gerar chave:

`ssh-keygen -t rsa`

2️⃣ Copiar para o servidor:

`ssh-copy-id usuario@192.168.1.100`

---

## **Conclusão**

O SSH é essencial para a administração remota segura de servidores. No entanto, se mal configurado, pode ser alvo de ataques. Medidas como autenticação por chaves, fail2ban e alteração da porta padrão ajudam a fortalecer sua segurança.

🔥 **Bônus:** Se quiser praticar ataques e defesas em SSH, pode testar em máquinas do **Hack The Box** ou **TryHackMe**!