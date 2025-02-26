### **Seção 1: Identificação do ataque**

Uma possível explicação para a mensagem de erro de tempo limite na conexão do site é um ataque de **SYN Flood**. Esse tipo de ataque pode resultar na sobrecarga do servidor, impedindo que conexões legítimas sejam estabelecidas corretamente.

Os logs da rede indicam **diversas solicitações SYN originadas do mesmo endereço IP (203.0.113.0)**, sem a correspondente finalização do handshake TCP. Esse comportamento sugere a tentativa de esgotar os recursos do servidor ao acumular conexões pendentes.

Com base nesses indícios, o evento pode ser classificado como um **ataque de negação de serviço (DoS) do tipo SYN Flood**, que visa exaurir a capacidade do servidor de aceitar novas conexões.

---

### **Seção 2: Impacto do ataque e funcionamento**

Quando visitantes tentam acessar o site, uma conexão é estabelecida através do **handshake de três vias do protocolo TCP**, que ocorre da seguinte forma:

1. O cliente envia um pacote **SYN** para o servidor, solicitando a conexão.
    
2. O servidor responde com um pacote **SYN-ACK**, confirmando o recebimento da solicitação.
    
3. O cliente finaliza o processo enviando um **ACK**, estabelecendo a conexão com sucesso.
    

No caso de um ataque **SYN Flood**, um invasor envia um grande volume de pacotes **SYN**, e o servidor responde com **SYN-ACK**, aguardando a resposta final (**ACK**) que nunca chega. Como resultado:

- O servidor fica com **múltiplas conexões pendentes** na fila de conexões TCP, esgotando seus recursos.
    
- Conexões legítimas não conseguem ser estabelecidas, resultando em **falhas no acesso ao site** e **queda do serviço**.
    

Os logs confirmam o ataque ao registrar **inúmeras solicitações SYN do mesmo IP (203.0.113.0)**, sem que a sequência do handshake seja concluída. Isso caracteriza um **DoS de Nível de Rede**, prejudicando a disponibilidade do servidor.

---

### **Conclusão**

O ataque identificado é um **SYN Flood**, que causa uma sobrecarga ao servidor impedindo conexões legítimas. Medidas de mitigação devem ser implementadas, como:

- Configuração de **limites de conexão** por IP.
    
- Uso de **firewalls e filtros de pacotes SYN anormais**.
    
- Implementação de **SYN cookies** para validar conexões reais.

Próximo Modulo [[Termos do glossário do Curso 3, Módulo 3]]
