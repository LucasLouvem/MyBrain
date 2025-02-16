# Ataques de Negacao de Servico (DoS e DDoS)

## O que é um ataque de negação de serviço (DoS)?

Um ataque de negação de serviço (DoS) tem como objetivo sobrecarregar uma rede ou servidor com um volume excessivo de tráfego. Isso impede que usuários legítimos acessem os serviços, causando prejuízos financeiros e deixando a organização vulnerável a outros ataques.

## Ataque Distribuído de Negação de Serviço (DDoS)

O ataque DDoS é uma variação do DoS que utiliza múltiplos dispositivos em diferentes localizações para inundar a rede-alvo com tráfego malicioso. Com isso, a probabilidade de sobrecarga do servidor aumenta significativamente.

Exemplo: Um invasor pode criar pacotes cuidadosamente estruturados para sobrecarregar um roteador, mesmo sem um alto volume de tráfego.

## Tipos de Ataques DoS em Nível de Rede

### 1. Ataque de Inundação de SYN

Este ataque explora o processo de handshake do protocolo TCP:

1. O dispositivo envia uma solicitação SYN para iniciar uma conexão.
2. O servidor responde com um pacote SYN/ACK e mantém uma porta aberta.
3. O dispositivo deve enviar um pacote ACK para completar a conexão.

O invasor envia um grande número de solicitações SYN sem concluir o handshake, esgotando as portas disponíveis do servidor e impedindo conexões legítimas.

### 2. Ataque de Inundação de ICMP

O protocolo ICMP é usado para relatar erros de transmissão na rede. No ataque de inundação de ICMP, o invasor envia repetidamente pacotes ICMP para um servidor, forçando-o a responder e consumir toda a largura de banda, até que o servidor falhe.

### 3. Ping of Death

Neste ataque, o invasor envia um pacote ICMP maior que 64 KB para um sistema alvo. Como o tamanho máximo de um pacote ICMP formatado corretamente é de 64 KB, isso pode sobrecarregar e travar o sistema.

## Conclusão

Os ataques DoS e DDoS são ameaças significativas à segurança de redes. Eles podem causar prejuízos financeiros, interromper operações e expor vulnerabilidades a outros ataques. É essencial que os analistas de segurança compreendam esses ataques e implementem medidas para mitigá-los.

Próximo Modulo [[Ler os registros do tcpdump]]
