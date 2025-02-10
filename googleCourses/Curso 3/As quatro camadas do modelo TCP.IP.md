# Comunicação em Redes (Continuação)

## Modelo TCP/IP

O **modelo TCP/IP** é um framework usado para visualizar como os dados são organizados e transmitidos pela rede. Ele define padrões que permitem a comunicação entre dispositivos e é composto por **quatro camadas**, cada uma com funções específicas:

1. **Camada de Acesso à Rede**  
2. **Camada da Internet**  
3. **Camada de Transporte**  
4. **Camada do Aplicativo**  

### 1. Camada de Acesso à Rede  

Essa camada lida com a **criação e transmissão de pacotes de dados** dentro da rede. Ela envolve o hardware, como cabos, switches e placas de rede, garantindo que os dados cheguem fisicamente ao destino correto.  

**Exemplo:** Quando você conecta seu computador a um roteador via cabo Ethernet, a comunicação entre os dispositivos ocorre nesta camada.  

### 2. Camada da Internet  

Aqui, os pacotes de dados recebem **endereços IP** para identificar corretamente o remetente e o destinatário. Essa camada gerencia como as redes se conectam umas às outras, decidindo se os pacotes ficarão dentro de uma rede local (LAN) ou serão enviados para uma rede maior, como a Internet.  

**Exemplo:** Se você está acessando um site, essa camada define se o seu pedido será resolvido localmente ou enviado para um servidor remoto na Internet.  

### 3. Camada de Transporte  

A camada de transporte garante que os pacotes cheguem **de forma confiável e ordenada** ao destino. Ela é responsável pelo **controle de erros e gerenciamento do fluxo de dados**.  

Principais protocolos desta camada:  
- **TCP (Transmission Control Protocol)**: Protocolo confiável que garante que os pacotes cheguem ao destino sem erros e na ordem correta.  
- **UDP (User Datagram Protocol)**: Mais rápido, mas sem verificação de erro, usado para transmissões onde a velocidade é mais importante que a precisão (como streaming de vídeo).  

**Exemplo:** Ao baixar um arquivo, o TCP verifica se os pacotes chegaram corretamente e solicita retransmissão caso algum esteja faltando.  

### 4. Camada do Aplicativo  

Essa camada define como os pacotes de dados serão interpretados pelos dispositivos receptores. Ela contém protocolos para diferentes serviços, como:  
- **HTTP/HTTPS** – Comunicação de páginas web.  
- **SMTP/POP3** – Envio e recebimento de e-mails.  
- **FTP** – Transferência de arquivos.  

**Exemplo:** Quando você acessa um site digitando um URL, o navegador usa o protocolo HTTP ou HTTPS, que faz parte desta camada.  

## Conclusão  

O modelo **TCP/IP** organiza e padroniza a comunicação entre dispositivos. Para os profissionais de segurança, entender essas camadas é essencial para **monitorar redes, detectar anomalias e proteger sistemas contra ataques**. 

Próximo Modulo [[Saiba mais sobre o modelo TCP.IP]]
