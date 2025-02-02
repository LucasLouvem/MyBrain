#### **O que é Telnet?**

Telnet (Telecommunication Network) é um **protocolo de comunicação** usado para acessar remotamente dispositivos em uma rede. Ele permite que um usuário controle um sistema remoto como se estivesse diretamente nele, através de uma **conexão baseada em linha de comando**.

#### **Como Funciona?**

- Utiliza o protocolo **TCP na porta 23**.
- Permite conexão entre um **cliente** (quem acessa) e um **servidor** (máquina remota).
- Após se conectar, o usuário pode **executar comandos** e interagir com o sistema remoto.
- Por padrão, **não utiliza criptografia**, o que o torna inseguro.

#### **Exemplo de Uso**

Para conectar-se a um servidor via Telnet no Linux:

bash

CopyEdit

`telnet [IP_do_Servidor]`

Se o servidor estiver rodando Telnet, ele solicitará credenciais (usuário e senha) para acessar.

#### **Principais Problemas de Segurança**

1. **Dados em texto plano**: Tudo, incluindo senhas, é transmitido **sem criptografia**, permitindo interceptação via **sniffing** (ataques Man-in-the-Middle).
2. **Sem autenticação forte**: Qualquer um que obtenha credenciais pode acessar o sistema remotamente.
3. **Vulnerável a ataques de força bruta**: Como não tem proteção avançada, ataques automatizados podem testar várias senhas até encontrar a correta.

#### **Tipos de Ataques**

- **Sniffing**: Captura de dados trafegados na rede para roubo de senhas.
- **Ataques de força bruta**: Uso de ferramentas como **Hydra** para descobrir senhas.
- **MITM (Man-in-the-Middle)**: Um invasor intercepta a comunicação entre cliente e servidor.

#### **Alternativa Segura: SSH**

Devido às falhas de segurança do Telnet, ele foi substituído pelo **SSH (Secure Shell)**, que oferece criptografia forte e autenticação segura.

#### **Conclusão**

- Telnet **ainda é usado** em alguns dispositivos legados e redes internas, mas é altamente inseguro para conexões em redes públicas.
- Em vez de Telnet, **use SSH sempre que possível** para proteger suas conexões remotas.