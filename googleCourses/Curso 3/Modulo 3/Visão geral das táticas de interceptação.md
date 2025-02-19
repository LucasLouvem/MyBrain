### **O que são ataques de interceptação?**

Os ataques de interceptação envolvem a captura de pacotes de dados enquanto eles trafegam pela rede. Isso pode ser feito por meio de técnicas como **sniffing de pacotes** e **spoofing de IP**, permitindo que invasores obtenham informações sigilosas ou manipulem comunicações.

## **Interceptação de Pacotes**

A **Placa de Interface de Rede (NIC)** é responsável por direcionar pacotes para o dispositivo correto dentro da rede. Normalmente, ela recebe apenas pacotes endereçados ao seu **endereço MAC**. No entanto, se configurada no **modo promíscuo**, a NIC pode aceitar e capturar todos os pacotes da rede.

Exemplo:

- Um invasor usa **Wireshark** para monitorar o tráfego em uma rede privada e capturar credenciais transmitidas sem criptografia.
- Após obter informações como endereços **IP** e **MAC**, ele pode realizar ataques de **spoofing de IP**.

## **Spoofing de IP**

Após interceptar pacotes, um invasor pode falsificar endereços IP e MAC para parecer um dispositivo autorizado e **burlar regras de segurança**.

### **Principais ataques que utilizam spoofing de IP:**

### **1. Ataque On-Path (Man-in-the-Middle - MITM)**

Um invasor se posiciona entre dois dispositivos confiáveis e intercepta suas comunicações, podendo capturar credenciais ou modificar os dados transmitidos.

Exemplo:

- Um hacker intercepta uma consulta DNS e redireciona o usuário para um site falso com código malicioso, roubando informações bancárias.

**Mitigação:**

- Uso de **criptografia (TLS/SSL)** para proteger a comunicação.
- Implementação de **DNSSEC** para evitar falsificação de respostas DNS.

### **2. Ataque Smurf**

Combinação de **spoofing de IP** e ataque **DDoS**, onde um invasor inunda uma rede com pacotes ICMP (ping), sobrecarregando servidores e causando negação de serviço.

Exemplo:

- Um invasor falsifica o IP de um alvo e envia uma solicitação de **ping** para toda a rede. Os dispositivos respondem ao IP falsificado, sobrecarregando o sistema do alvo e derrubando a rede.

**Mitigação:**

- Configuração de **firewalls avançados (NGFW)** para bloquear tráfego ICMP suspeito.
- Filtragem de **endereços IP falsificados** em roteadores.

### **3. Ataque de Negação de Serviço (DoS)**

Diferente do spoofing de IP, um ataque **DoS** impede que um servidor ou sistema execute operações legítimas, bombardeando-o com requisições falsas até sobrecarregá-lo.

Exemplo:

- Um site recebe milhões de solicitações falsas simultaneamente, tornando-o inacessível para usuários reais.

**Mitigação:**

- Uso de **CDN e balanceadores de carga** para distribuir o tráfego.
- Monitoramento de **padrões anômalos** no tráfego da rede.

## **Conclusão**

Ataques de interceptação representam sérios riscos à segurança das redes. A implementação de **criptografia, firewalls avançados e segmentação de rede** ajuda a mitigar essas ameaças. Além disso, o **princípio da defesa em profundidade** deve ser aplicado, combinando múltiplas camadas de proteção para garantir a segurança dos sistemas.

Próximo Modulo [[Atividade Analisar ataques à rede de computadores]]
