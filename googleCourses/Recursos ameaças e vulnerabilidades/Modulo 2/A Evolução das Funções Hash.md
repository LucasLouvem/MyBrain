

As funções hash são controles importantes na estratégia de segurança das empresas. Elas são amplamente usadas para autenticação e não repúdio, garantindo que a autenticidade das informações não possa ser negada.

## O que é Hashing?

O hashing é um processo que converte informações em um valor único e de tamanho fixo, garantindo sua integridade. As funções hash são algoritmos que produzem códigos que não podem ser descriptografados.

## Origens do Hash

As funções hash existem desde os primórdios da computação, sendo inicialmente criadas para agilizar a pesquisa de dados. Esses algoritmos foram projetados para representar qualquer dado como um valor pequeno e de tamanho fixo, armazenado em estruturas conhecidas como tabelas hash.

### MD5: O Início

Uma das primeiras funções hash foi o **Message Digest 5 (MD5)**, desenvolvido por Ronald Rivest no início dos anos 90. O MD5 converte dados em um valor de **128 bits** (32 caracteres), garantindo que qualquer alteração no arquivo gere um novo hash. No entanto, descobriu-se que essa função era vulnerável a ataques de colisão.

## Colisões de Hash

Como as funções hash mapeiam qualquer entrada para um valor fixo, existe um número limitado de saídas possíveis. Isso pode levar a **colisões**, onde diferentes entradas geram o mesmo hash. No caso do MD5, essa vulnerabilidade compromete a autenticidade dos dados, permitindo ataques de falsificação.

## Algoritmos de Hash Seguro (SHA)

Para evitar colisões, foram desenvolvidas funções hash mais robustas, conhecidas como **Secure Hashing Algorithms (SHA)**. Esses algoritmos foram aprovados pelo **National Institute of Standards and Technology (NIST)** e oferecem maior segurança:

- **SHA-1** (160 bits) - Não é mais considerado seguro.
- **SHA-224**
- **SHA-256**
- **SHA-384**
- **SHA-512**

Quanto maior o tamanho do hash, menor a chance de colisões.

## Armazenamento Seguro de Senhas

As senhas geralmente são armazenadas em bancos de dados e protegidas por funções hash. No entanto, se um banco de dados for comprometido e as senhas estiverem em **texto simples**, os atacantes podem obter acesso facilmente. O hashing adiciona uma camada de proteção, tornando impossível a reversão do valor original.

### Ataques com Tabelas Arco-Íris

As **tabelas arco-íris** contêm valores hash pré-gerados para diferentes combinações de senhas fracas, permitindo que atacantes as decifrem rapidamente.

### Adicionando "Sal" ao Hash

Para evitar ataques com tabelas arco-íris, adiciona-se um **salt**, que é uma sequência aleatória de caracteres inserida antes do hashing. Isso garante que senhas idênticas tenham hashes diferentes, tornando o ataque ineficaz.

Exemplo:

```
Senha: password
Hash sem salt: 5f4dcc3b5aa765d61d8327deb882cf99
Hash com salt: a7f8e3b2c89a3f4e5d678fa2d1c3b9a2
```

## Conclusão

O hash é uma ferramenta essencial para garantir a integridade dos dados. No entanto, algoritmos antigos como o MD5 ainda são usados por empresas menores, apesar de suas vulnerabilidades. A implementação de funções SHA seguras, combinadas com técnicas como **salting**, ajuda a mitigar ataques e proteger dados sensíveis.