## **Interceptação de Pacotes**

A interceptação de pacotes é o ato de capturar e analisar os dados que trafegam em uma rede. Essa técnica pode ser usada tanto para fins legítimos, como a investigação de incidentes de segurança e depuração de redes, quanto para fins maliciosos, onde atacantes tentam obter informações sigilosas sem autorização.

Cada pacote transmitido na rede contém um **cabeçalho**, com informações como os endereços IP de origem e destino, e um **corpo**, que pode armazenar conteúdos sensíveis, como credenciais de login, dados bancários e mensagens privadas.

### **Como Agentes Mal-Intencionados Interceptam Pacotes?**

Atacantes podem inserir-se em uma conexão legítima entre dois dispositivos e monitorar os pacotes que trafegam entre eles. Para isso, eles podem usar softwares como **Wireshark** ou ferramentas específicas de sniffing, capturando e analisando os dados em busca de informações úteis. Além disso, dispositivos de hardware, como antenas Wi-Fi modificadas, também podem ser usados para esse fim.

Exemplo:

- Um hacker em um café pode usar um **sniffer** de pacotes em uma rede Wi-Fi pública para capturar dados de usuários conectados. Se os sites acessados não usarem criptografia (HTTP ao invés de HTTPS), ele pode ver logins e senhas em texto claro.

### **Tipos de Interceptação de Pacotes**

#### **Interceptação Passiva**

Nesse tipo de ataque, o invasor apenas observa o tráfego de rede sem interferir nos pacotes. Isso é semelhante a um carteiro abrindo e lendo cartas sem alterar seu conteúdo. Como todo o tráfego de uma rede é visível para qualquer host conectado a um hub, um invasor pode visualizar informações confidenciais transmitidas sem criptografia.

Exemplo:

- Um atacante conectado a um hub em uma rede empresarial pode capturar tráfego interno e visualizar e-mails enviados sem criptografia.

#### **Interceptação Ativa**

Aqui, o atacante não apenas captura os pacotes, mas também altera seu conteúdo antes de entregá-los ao destinatário. Ele pode, por exemplo, modificar uma mensagem de e-mail, trocar credenciais ou até mesmo redirecionar os pacotes para um servidor controlado por ele.

Exemplo:

- Um atacante pode modificar os detalhes de uma transferência bancária interceptando um pacote e alterando o número da conta destinatária antes que ele chegue ao banco.

### **Como Proteger-se contra a Interceptação de Pacotes?**

1. **Uso de VPNs**
    
    - Uma **VPN (Rede Privada Virtual)** criptografa os pacotes, tornando impossível para atacantes lerem o conteúdo, mesmo que consigam capturá-los.
    - Exemplo: Se você acessar sua conta bancária usando uma VPN, mesmo em uma rede Wi-Fi pública, seus dados estarão protegidos.
2. **Acesso a Sites com HTTPS**
    
    - O protocolo **HTTPS** usa SSL/TLS para criptografar as informações entre o usuário e o site, impedindo ataques de interceptação.
    - Exemplo: Ao fazer login em um site de compras, sempre verifique se há um **cadeado ao lado do endereço** no navegador, indicando que a comunicação está protegida.
3. **Evitar Redes Wi-Fi Abertas**
    
    - Redes públicas, como as de cafés e aeroportos, geralmente não possuem criptografia. Isso facilita a captura de pacotes.
    - Exemplo: Se precisar usar um Wi-Fi público, evite acessar contas bancárias ou redes sociais sem uma VPN ativa.

---

Com essas medidas, é possível reduzir os riscos de interceptação de pacotes e garantir maior segurança na transmissão de dados.

Próximo Modulo [[IPS Spoofing]]
