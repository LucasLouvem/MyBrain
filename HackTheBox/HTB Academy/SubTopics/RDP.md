## **RDP (Remote Desktop Protocol)**

RDP (Remote Desktop Protocol) é um protocolo desenvolvido pela Microsoft que permite a conexão remota a outro computador com uma interface gráfica. Ele é amplamente utilizado para administração remota de servidores e suporte técnico.

---

## **1. Como Funciona?**

O RDP permite que um usuário acesse outro computador remotamente como se estivesse fisicamente presente nele. A conexão acontece via **porta 3389 (TCP/UDP)**, e os dados são transmitidos de forma criptografada. O usuário vê a área de trabalho remota e pode interagir com ela usando teclado e mouse.

---

## **2. Como Conectar a um Servidor RDP?**

### **Windows**

1. **Abrir o Cliente RDP**  
    Pressione `Win + R`, digite `mstsc` e pressione Enter.
2. **Digite o IP ou Nome do Servidor**
3. **Clique em "Conectar"**
4. **Insira suas Credenciais**
    - Usuário e senha do Windows do computador remoto.
5. **Confirme a Conexão**  
    Se aparecer um aviso de certificado, clique em "Sim".

### **Linux**

No Linux, pode-se usar `rdesktop`, `xfreerdp` ou `remmina`:

`xfreerdp /u:usuario /p:senha /v:IP_DO_SERVIDOR`

### **MacOS**

No macOS, pode-se usar o **Microsoft Remote Desktop** (disponível na App Store).

---

## **3. Configurações Avançadas**

### **Redirecionamento de Recursos**

É possível redirecionar **unidades USB, impressoras e área de transferência**:

`xfreerdp /u:usuario /p:senha /v:IP_DO_SERVIDOR /drive:USB,/mnt/usb`

### **Ajuste de Qualidade e Performance**

Para conexões lentas, desative efeitos gráficos:

`xfreerdp /u:usuario /p:senha /v:IP_DO_SERVIDOR +compression -themes -wallpaper`

O **Remote Desktop Protocol (RDP)** é um dos principais alvos de ataques cibernéticos, sendo frequentemente explorado por ransomwares, ataques de força bruta e vulnerabilidades críticas. Para garantir um ambiente seguro, é fundamental implementar **camadas de proteção** e adotar boas práticas.

---

## 🚨 **Principais Ameaças e Explorações do RDP**

O RDP pode ser explorado de diversas formas. Aqui estão os vetores mais comuns:

### 1️⃣ **Ataques de Força Bruta**

- Atacantes tentam várias combinações de usuário/senha automaticamente até encontrar uma válida.
- Ferramentas usadas: `hydra`, `ncrack`, `crowbar`

`hydra -L users.txt -P passwords.txt rdp://IP_DO_ALVO`

✅ **Mitigação:**  
🔹 Utilize **autenticação multifator (MFA)**.  
🔹 Bloqueie tentativas excessivas de login (**Account Lockout Policy**).  
🔹 Monitore logs (`Event ID 4625` no Windows).  
🔹 Use listas de **IPs permitidos (whitelisting)** no firewall.

---

### 2️⃣ **Exploração de Vulnerabilidades**

Diversas falhas críticas foram descobertas no RDP. Algumas das mais notórias:

| CVE                    | Vulnerabilidade | Impacto                                          |
| ---------------------- | --------------- | ------------------------------------------------ |
| **CVE-2019-0708**      | **BlueKeep**    | Execução remota sem autenticação                 |
| **CVE-2020-0609/0610** | **DejaBlue**    | Execução remota e escalonamento de privilégios   |
| **CVE-2012-0002**      | **MS12-020**    | Execução remota (sem necessidade de credenciais) |

✅ **Mitigação:**  
🔹 **Atualize regularmente** o sistema operacional.  
🔹 **Desative RDP caso não seja necessário.**  
🔹 Habilite **Network Level Authentication (NLA)** para exigir credenciais antes de iniciar a sessão.

`reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v UserAuthentication /t REG_DWORD /d 1 /f`

---

### 3️⃣ **Ataques Man-in-the-Middle (MITM)**

- Se a conexão RDP não estiver **criptografada**, um atacante pode interceptá-la.
- Ferramentas como `ettercap` e `MITMf` podem capturar credenciais.

✅ **Mitigação:**  
🔹 **Use VPN** para proteger conexões remotas.  
🔹 **Habilite TLS e CredSSP** para garantir criptografia forte.  
🔹 Desative **autenticação padrão (RDP Security Layer)** e use **SSL/TLS**:

powershell

`gpedit.msc → Computer Configuration → Administrative Templates → Windows Components → Remote Desktop Services → Remote Desktop Session Host → Security → Require use of specific security layer → SSL`

---

### 4️⃣ **Ataques de Pass-the-Hash (PTH)**

- Se um atacante obtiver um **hash NTLM** da vítima, ele pode autenticar sem precisar da senha real.

✅ **Mitigação:**  
🔹 **Desative o armazenamento de credenciais na memória**:

powershell

`reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v DisableRestrictedAdmin /t REG_DWORD /d 1 /f`

🔹 Utilize **autenticação Kerberos** em vez de NTLM.  
🔹 **Implemente LAPS** para gerenciar senhas de administradores locais.

---

### 5️⃣ **Ataques de Ransomware via RDP**

- O RDP é um vetor comum para ransomwares como **Ryuk, Sodinokibi e Dharma**.
- Atacantes acessam a máquina via RDP e executam malware.

✅ **Mitigação:**  
🔹 **Desative RDP quando não estiver em uso.**  
🔹 Restrinja conexões apenas a IPs confiáveis.  
🔹 Utilize **contas com privilégios mínimos** para evitar que um atacante escale permissões.  
🔹 **Habilite a autenticação MFA** (Windows Hello for Business, Duo, etc.).

---

## 🔧 **Configurações Avançadas para Proteger o RDP**

Aqui estão algumas configurações recomendadas para aumentar a segurança do RDP:

### **1️⃣ Desativar RDP para Usuários Não Administradores**

powershell

`gpedit.msc → Computer Configuration → Windows Settings → Security Settings → Local Policies → User Rights Assignment → Deny log on through Remote Desktop Services`

### **2️⃣ Alterar a Porta Padrão do RDP**

A porta padrão `3389` é constantemente escaneada. Mudar para outra porta pode reduzir ataques automatizados.

powershell

`reg add "HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumber /t REG_DWORD /d 54321 /f`

✅ **Não se esqueça de abrir a nova porta no firewall!**

### **3️⃣ Bloquear Tentativas de Login Falhas**

powershell

`net accounts /lockoutthreshold:3 /lockoutduration:30`

### **4️⃣ Habilitar Logs e Monitoramento**

🔹 Ative o log de tentativas de login RDP:

powershell

`gpedit.msc → Windows Settings → Security Settings → Local Policies → Audit Policy → Audit logon events → Success, Failure`

🔹 Utilize ferramentas como **Splunk, Graylog, ou Wazuh** para monitorar atividades suspeitas.

### **5️⃣ Usar Firewall para Bloquear Acessos Suspeitos**

powershell

`New-NetFirewallRule -DisplayName "Block RDP Attacks" -Direction Inbound -Protocol TCP -LocalPort 3389 -Action Block`

---

## **🛑 Conclusão**

O RDP é uma ferramenta poderosa, mas **extremamente vulnerável** se não for configurado corretamente. Para garantir segurança:

✅ **Desative RDP quando não for necessário**  
✅ **Utilize autenticação multifator (MFA)**  
✅ **Habilite logs e monitoramento**  
✅ **Aplique atualizações e patches de segurança**  
✅ **Restrinja acesso com firewall e VPN**

Se o RDP estiver **exposto à internet sem proteção**, ele é um alvo fácil para ataques. Implementando essas práticas, você reduz significativamente o risco de comprometimento da sua rede.