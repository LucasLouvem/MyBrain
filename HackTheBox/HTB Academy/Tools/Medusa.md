### **O que é Medusa (Brute-Force)?**

Medusa é uma ferramenta de **força bruta** de alto desempenho usada para testar a segurança de sistemas de autenticação. Ela suporta uma variedade de protocolos, como SSH, FTP, HTTP, MySQL, RDP, entre outros. É uma alternativa ao Hydra, mas com algumas diferenças em termos de desempenho e funcionalidades.

---

### **Como usar o Medusa?**

#### **Instalação**

1. **No Linux**:
    
    - No Debian/Ubuntu:
        
        bash
        
        Copy
        
        sudo apt update
        sudo apt install medusa
        
    - No Arch Linux:
        
        bash
        
        Copy
        
        sudo pacman -S medusa
        
    - Ou compile a partir do código-fonte:
        
        bash
        
        Copy
        
        git clone https://github.com/jmk-foofus/medusa.git
        cd medusa
        ./configure
        make
        sudo make install
        
2. **No Windows**:
    
    - O Medusa é nativo do Linux, mas pode ser usado no Windows via WSL (Windows Subsystem for Linux) ou em máquinas virtuais.
        

---

### **Uso Básico**

1. **Sintaxe básica**:
    
    bash
    
    Copy
    
    medusa -h <host> -u <usuário> -P <wordlist> -M <módulo>
    
    - `-h`: Host ou IP do alvo.
        
    - `-u`: Nome de usuário ou arquivo com lista de usuários.
        
    - `-P`: Wordlist de senhas.
        
    - `-M`: Módulo do protocolo (ex: ssh, ftp, http).
        
2. **Exemplo de ataque SSH**:
    
    bash
    
    Copy
    
    medusa -h 192.168.1.100 -u admin -P /caminho/para/wordlist.txt -M ssh
    
3. **Exemplo de ataque FTP**:
    
    bash
    
    Copy
    
    medusa -h 192.168.1.100 -U /caminho/para/usuarios.txt -P /caminho/para/senhas.txt -M ftp
    
4. **Opções adicionais**:
    
    - `-t`: Número de threads (padrão: 16).
        
    - `-O`: Arquivo de log para salvar os resultados.
        
    - `-f`: Parar após encontrar a primeira credencial válida.
        
    - `-n`: Porta do serviço (útil se o serviço não estiver na porta padrão).
        
    
    Exemplo com threads e log:
    
    bash
    
    Copy
    
    medusa -h 192.168.1.100 -u admin -P /caminho/para/wordlist.txt -M ssh -t 32 -O resultados.log
    

---

### **Módulos Suportados**

O Medusa suporta vários protocolos. Para ver a lista completa de módulos, use:

bash

Copy

medusa -d

Alguns módulos comuns:

- `ssh`: Para serviços SSH.
    
- `ftp`: Para serviços FTP.
    
- `http`: Para autenticação HTTP.
    
- `mysql`: Para bancos de dados MySQL.
    
- `rdp`: Para Remote Desktop Protocol (RDP).
    
- `smbnt`: Para SMB (Windows compartilhamento de arquivos).
    

---

### **Exemplos Práticos**

1. **Ataque SSH com lista de usuários e senhas**:
    
    bash
    
    Copy
    
    medusa -h 192.168.1.100 -U usuarios.txt -P senhas.txt -M ssh -t 32
    
2. **Ataque HTTP básico**:
    
    bash
    
    Copy
    
    medusa -h 192.168.1.100 -u admin -P senhas.txt -M http -m DIR:/admin
    
3. **Ataque FTP com porta personalizada**:
    
    bash
    
    Copy
    
    medusa -h 192.168.1.100 -u ftpuser -P senhas.txt -M ftp -n 2121
    

---

### **Dicas de Uso**

4. **Use wordlists eficientes**: Wordlists como `rockyou.txt` ou listas personalizadas aumentam as chances de sucesso.
    
5. **Ajuste o número de threads**: Aumentar o número de threads pode acelerar o processo, mas pode sobrecarregar o sistema ou o alvo.
    
6. **Teste em ambientes controlados**: Use o Medusa apenas em sistemas onde você tem permissão para realizar testes de segurança.
    

---

### **Aviso Legal**

- O uso do Medusa para realizar ataques de força bruta sem autorização é **ilegal** e antiético.
    
- Utilize a ferramenta apenas para testes de segurança em sistemas que você possui ou tem permissão explícita para testar.