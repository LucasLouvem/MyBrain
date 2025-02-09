# Comunicação em Redes

## Modelo TCP/IP

O **TCP/IP** (Protocolo de Controle de Transmissão e Protocolo de Internet) é o modelo padrão usado para comunicação em rede. Ele define como os dispositivos se comunicam entre si pela Internet. Vamos entender os dois componentes principais deste modelo.

### O que é TCP?

**TCP** (Protocolo de Controle de Transmissão) é um protocolo de comunicação que permite que dois dispositivos formem uma conexão e transmitam dados de forma organizada. Ele inclui um conjunto de instruções que garante que os pacotes de dados cheguem ao destino correto, estabelecendo uma conexão confiável entre os dispositivos.

### O que é IP?

**IP** (Protocolo de Internet) é um conjunto de padrões usados para rotear e endereçar pacotes de dados à medida que eles viajam pela rede. O IP também atribui um **endereço IP** a cada dispositivo na rede, funcionando como um endereço único para cada dispositivo. O endereço IP é essencial para garantir que os pacotes cheguem ao destino certo. 

### Endereço IP

O endereço IP funciona de forma semelhante a um endereço físico, identificando de maneira única cada dispositivo em uma rede. Aprenderemos mais sobre como os endereços IP são estruturados em uma seção posterior.

### Portas de Rede

Quando pacotes de dados são enviados e recebidos em uma rede, eles são associados a **portas**. No sistema operacional de um dispositivo de rede, uma **porta** é uma interface baseada em software que organiza o envio e o recebimento de dados.

As portas ajudam a dividir o tráfego de rede em **segmentos** com base no serviço que será executado entre os dois dispositivos. Elas permitem que os computadores processem e priorizem os dados recebidos com base no número da porta.

### Exemplo de Funcionamento das Portas

Imagine que você está enviando uma carta para um amigo que mora em um prédio de apartamentos. O entregador de correspondência sabe como encontrar o prédio e também sabe exatamente qual apartamento (número da porta) entregar a carta.

Do mesmo jeito, os pacotes de dados têm instruções sobre qual **número de porta** devem usar para garantir que os dados sejam entregues corretamente ao serviço certo no dispositivo receptor.

### Portas Comuns

Alguns números de portas comuns são:

- **Porta 25**: Usada para e-mails.
- **Porta 443**: Usada para comunicação segura pela Internet (HTTPS).
- **Porta 20**: Usada para transferências de arquivos (FTP).

Esses números de porta ajudam a organizar e priorizar o tráfego na rede, garantindo que cada tipo de comunicação seja tratado adequadamente.

## Conclusão

O modelo TCP/IP é a base de toda a comunicação de dados na Internet. Entender como ele funciona é crucial para garantir uma comunicação eficiente e segura entre dispositivos.
