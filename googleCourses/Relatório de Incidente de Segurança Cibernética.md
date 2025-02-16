### **Análise de Tráfego de Rede**

## **Parte 1: Resumo do Problema Encontrado no Log de Tráfego DNS e ICMP**

Durante a análise de tráfego de rede, foram identificadas mensagens ICMP indicando **"UDP port 53 unreachable"** após tentativas de acesso ao domínio **"yummyrecipesforme.com"**. Foram registradas **três tentativas de conexão**, todas resultando em erro de entrega.

O problema mais provável é que o servidor DNS esteja **inacessível** ou que um **firewall esteja bloqueando os pacotes**. Para determinar se há um ataque DDoS, seria necessário verificar **um alto volume de solicitações repetitivas**, vindas de múltiplos endereços IP, o que não foi observado neste caso.

---

## **Parte 2: Análise dos Dados e Causa do Incidente**

### **Horário do incidente:**

De acordo com os registros analisados, as solicitações ocorreram nos seguintes horários:

- **13:24:32**
- **13:26:14**
- **13:28:51**

Cada requisição foi feita com um intervalo de aproximadamente **2 minutos** e originada do mesmo endereço IP **192.51.100.15**, utilizando a porta de origem **52444** para acessar a **porta 53 (DNS)** do servidor de destino.

### **Como a equipe de TI tomou conhecimento do incidente:**

A equipe de TI identificou o problema utilizando a ferramenta de análise de tráfego **Tcpdump**, que registrou os pacotes ICMP de erro retornados pelo servidor DNS.

### **Ações tomadas pela equipe de TI para investigar o incidente:**

Após a detecção dos erros, os engenheiros de segurança foram acionados para investigar o problema. A equipe notificou o supervisor direto e iniciou uma análise detalhada do tráfego de rede.

### **Principais descobertas da investigação da equipe de TI:**

- O tráfego DNS **não obteve resposta do servidor**.
- O erro **"UDP port 53 unreachable"** foi registrado **três vezes**, indicando que o servidor pode estar bloqueando solicitações ou inativo.
- Não foram observadas **múltiplas fontes de tráfego suspeito**, o que **não indica** um ataque DDoS.

### **Causa provável do incidente:**

A causa mais provável é que um **firewall esteja bloqueando o tráfego DNS na porta 53**, possivelmente devido a uma configuração incorreta ou uma política de segurança ativada para restringir conexões externas. Outra possibilidade é que o servidor DNS esteja **offline** ou **com falha temporária**.