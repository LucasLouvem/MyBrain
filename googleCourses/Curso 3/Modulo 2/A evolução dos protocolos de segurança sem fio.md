# Evolução dos Protocolos de Segurança Sem Fio

## Introdução

Inicialmente, toda a comunicação da Internet ocorria por cabos físicos. Nos anos 1980, os EUA designaram um espectro de frequências de ondas de rádio para uso sem licença, possibilitando a expansão da Internet sem fio. No final dos anos 1990, tecnologias de transmissão de dados por rádio foram desenvolvidas, permitindo o surgimento do Wi-Fi.

O Wi-Fi, baseado nos padrões IEEE 802.11, é protegido por protocolos de segurança que evoluíram para solucionar vulnerabilidades e melhorar a proteção das redes sem fio.

## Protocolos de Segurança Wi-Fi

### WEP (Wired Equivalent Privacy)

- Introduzido em 1999, visava oferecer segurança semelhante às redes com fio.
- Utilizava criptografia fraca, sendo suscetível a ataques.
- Atualmente obsoleto, mas ainda pode ser encontrado em roteadores antigos.

### WPA (Wi-Fi Protected Access)

- Introduzido em 2003 como solução temporária para substituir o WEP.
- Utiliza o protocolo TKIP (Temporal Key Integrity Protocol), que gera chaves dinâmicas.
- Inclui verificação de integridade para evitar alterações maliciosas nas transmissões.
- Vulnerável a ataques KRACK (Key Reinstallation Attack), permitindo descriptografia de transmissões interceptadas.

### WPA2

- Introduzido em 2004, substituiu o WPA como padrão de segurança.
- Utiliza criptografia AES e protocolo CCMP para garantir autenticação e integridade das mensagens.
- Disponível em dois modos:
    - **Pessoal:** Utiliza uma frase secreta compartilhada, ideal para redes domésticas.
    - **Empresarial:** Utiliza um servidor de autenticação, adequado para redes corporativas.
- Vulnerável a ataques KRACK.

### WPA3

- Introduzido em 2018, resolve vulnerabilidades do WPA2.
- Utiliza SAE (Simultaneous Authentication of Equals) para proteger contra ataques de força bruta.
- Implementa criptografia de 128 bits, com opção de 192 bits no modo empresarial.
- Impede que atacantes baixem dados para tentar descriptografá-los posteriormente.

## Conclusão

Como analista de segurança, é essencial compreender a evolução dos protocolos Wi-Fi e suas vulnerabilidades. Para proteger redes sem fio, é recomendável utilizar as versões mais recentes e atualizadas dos protocolos de segurança, garantindo maior proteção contra ameaças.

### Exemplo de Configuração Segura:

1. **Evite WEP e WPA** – Opte por WPA2 ou WPA3.
2. **Utilize senhas fortes** – No WPA2-Pessoal, escolha uma senha complexa.
3. **Atualize firmwares** – Mantenha roteadores e dispositivos sempre atualizados.
4. **Ative firewalls e filtros de MAC** – Para maior controle de acesso.

Próximo Modulo [[Firewalls e medidas de segurança de rede]]
