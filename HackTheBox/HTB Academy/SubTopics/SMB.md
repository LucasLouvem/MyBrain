### **SMB (Server Message Block): O que é, Como Funciona e Segurança**

#### **O que é SMB?**

O **Server Message Block (SMB)** é um protocolo de rede utilizado para **compartilhamento de arquivos, impressoras e outros recursos** entre dispositivos em uma rede local (**LAN**). Ele permite que sistemas Windows, Linux e macOS acessem arquivos remotos como se estivessem em um diretório local.

#### **Como Funciona?**

- O SMB opera no modelo **cliente-servidor**, onde um cliente solicita acesso a recursos compartilhados de um servidor SMB.
- Ele usa o **protocolo TCP/IP** para comunicação e normalmente funciona na **porta 445**.
- SMB é integrado ao **Windows**, mas pode ser usado no Linux com o **Samba** (implementação livre do SMB).

#### **Versões do SMB**

1. **SMBv1** (1983) – Antigo e vulnerável, responsável pelo ataque do **WannaCry**.
2. **SMBv2** (2006) – Melhorias na segurança e desempenho.
3. **SMBv3** (2012) – Introduziu criptografia e autenticação mais forte.

#### **Comandos Básicos no Linux (Usando Samba)**

- **Listar compartilhamentos em um servidor:**
    
    `smbclient -L //192.168.1.1`
    
- **Acessar um compartilhamento SMB:**
    
    `smbclient //192.168.1.1/compartilhamento -U usuario`
    
- **Montar um compartilhamento SMB no Linux:**
    
    `mount -t cifs //192.168.1.1/compartilhamento /mnt -o username=usuario,password=senha`
    

#### **Principais Vulnerabilidades e Ataques**

4. **SMBv1 (EternalBlue)** – Exploração da vulnerabilidade **MS17-010**, usada pelo ransomware **WannaCry**.
5. **Ataques de força bruta** – Tentativa de adivinhar credenciais usando ferramentas como **Hydra** ou **CrackMapExec**.
6. **Pass-the-Hash** – Usa hashes NTLM roubados para autenticação sem precisar da senha em texto claro.
7. **Interceptação de tráfego (MITM)** – Captura e manipulação da comunicação SMB se não houver criptografia.

#### **Ferramentas para Exploração**

- **enum4linux** – Coleta informações sobre servidores SMB.
- **smbclient** – Interage com compartilhamentos SMB.
- **Metasploit** – Exploração de vulnerabilidades SMB.
- **CrackMapExec** – Teste de credenciais em redes Windows.

#### **Medidas de Segurança**

✅ **Desativar SMBv1** em servidores Windows antigos.  
✅ **Usar SMBv3** sempre que possível, pois possui criptografia.  
✅ **Bloquear a porta 445** em redes externas para evitar ataques.  
✅ **Utilizar autenticação forte** e evitar senhas fracas.  
✅ **Monitorar logs SMB** para detectar acessos suspeitos.

#### **Conclusão**

O SMB é essencial para compartilhamento de arquivos em redes corporativas, mas versões antigas representam riscos críticos. Manter o SMB atualizado e aplicar boas práticas de segurança é fundamental para evitar ataques cibernéticos.