### **Spoofing de IP: Ataques e Proteção**

O **spoofing de IP** é um ataque onde um invasor altera o IP de origem de um pacote de dados para se passar por um sistema autorizado. Isso permite contornar regras de firewall e acessar redes privadas. Os principais tipos de ataques envolvendo spoofing de IP são:

#### **1. Ataque On-Path (Man-in-the-Middle - MitM)**

O atacante se coloca entre duas partes em uma conexão legítima (por exemplo, um navegador e um servidor). Ele intercepta os pacotes, obtém os endereços IP e MAC dos dispositivos e pode manipular os dados.  
📌 **Exemplo:** Um hacker se insere entre um usuário e um site bancário, capturando senhas e informações financeiras.

#### **2. Ataque de Repetição (Replay Attack)**

O invasor intercepta um pacote e o retransmite posteriormente. Isso pode causar falhas na comunicação ou permitir que ele se passe por um usuário autorizado.  
📌 **Exemplo:** Se um hacker interceptar uma solicitação de login e repeti-la, pode acessar uma conta sem precisar de credenciais.

#### **3. Ataque Smurf**

Uma variação de ataque **DDoS**, onde o invasor envia um grande volume de pacotes a um endereço IP, sobrecarregando o sistema e causando falhas.  
📌 **Exemplo:** Um servidor pode ser derrubado ao receber um número massivo de solicitações forjadas com endereços falsificados.

### **Como se Proteger**

✅ **Criptografia**: Dados protegidos evitam a interceptação e manipulação por agentes mal-intencionados.  
✅ **Firewalls bem configurados**: Devem bloquear pacotes de entrada com IPs que parecem ser internos, pois isso indica possível falsificação.  
✅ **Regras de filtragem**: Firewalls podem ser configurados para rejeitar tráfego suspeito e monitorar padrões incomuns.

Com essas medidas, é possível mitigar os riscos de spoofing de IP e manter a rede mais segura.

Próximo Modulo [[ Visão geral das táticas de interceptação]]
