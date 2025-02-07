# Web Fuzzing

## O que é Fuzzing?
Fuzzing é uma técnica de teste que envia várias entradas para um sistema para analisar como ele reage. No contexto de **Web Fuzzing**, usamos listas de palavras para testar diretórios e páginas ocultas em um site.

**Exemplo:**  
Se visitarmos `https://www.hackthebox.eu/doesnotexist`, o site retorna um **404 (Página Não Encontrada)**. Mas se tentarmos `https://www.hackthebox.eu/login`, ele retorna um **200 (OK)** e mostra a página de login.

## Por que fazer Web Fuzzing?
Sites geralmente não listam todos os diretórios e páginas disponíveis. O **fuzzing** ajuda a descobrir caminhos ocultos que podem conter informações sensíveis ou vulnerabilidades.

**Exemplo:**  
Se um site tem uma página de administração (`/admin`), mas ela não aparece nos links, podemos encontrá-la fazendo fuzzing.

## Automatização com Ferramentas
Testar manualmente seria muito demorado. Por isso, usamos ferramentas como **ffuf** para testar rapidamente várias URLs e analisar suas respostas.

**Exemplo de comando com ffuf:**  
```bash
ffuf -u http://SERVER_IP:PORT/FUZZ -w /opt/useful/SecLists/Discovery/Web-Content/directory-list-2.3-medium.txt
```
- `-u`: Define a URL a ser testada.  
- `FUZZ`: Marcador onde as palavras da lista serão inseridas.  
- `-w`: Especifica a lista de palavras usada para fuzzing.  

## Listas de Palavras (Wordlists)
Usamos listas predefinidas que contêm diretórios e páginas comuns. O repositório **SecLists** no GitHub é uma das principais fontes dessas listas.

**Exemplo de diretórios comuns em um site:**  
```
admin
login
dashboard
uploads
backup
config
```
Se encontrarmos `/admin` ou `/backup`, podemos investigar e possivelmente explorar vulnerabilidades.

## Resumo
- **Web Fuzzing** descobre páginas e diretórios ocultos em sites.  
- **Ferramentas automáticas** como `ffuf` fazem isso rapidamente.  
- **Wordlists** ajudam a aumentar as chances de encontrar caminhos válidos.  
- **Códigos de resposta HTTP** indicam se um diretório existe ou não.  

Isso ajuda no **pentest** para mapear alvos e encontrar possíveis falhas de segurança.

---
# Fuzzing de Diretório

## Introdução
Agora que entendemos o conceito de Web Fuzzing, podemos usar o **ffuf** para encontrar diretórios ocultos em sites.

## Instalando o ffuf
O **ffuf** já vem pré-instalado no **PwnBox**, mas se quiser usá-lo em outra máquina, execute:
```bash
apt install ffuf -y
```
Ou baixe diretamente do [repositório oficial](https://github.com/ffuf/ffuf).

## Usando o ffuf
Primeiro, verificamos a ajuda do comando para entender suas opções:
```bash
ffuf -h
```
Principais opções:
- `-w`: Define a **wordlist** para fuzzing.
- `-u`: Define a **URL-alvo**.
- `-mc`: Filtra **códigos de resposta** HTTP.
- `-fs`: Filtra **tamanhos de resposta**.
- `-t`: Define **threads** para maior velocidade.

## Exemplo de Fuzzing de Diretório
### Definição da Wordlist
Usamos uma wordlist específica para diretórios:
```bash
ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ
```
### Testando Diretórios na URL-Alvo
Inserimos `FUZZ` na posição do diretório dentro da URL:
```bash
ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt -u http://SERVER_IP:PORT/FUZZ
```
### Exemplo de Saída do ffuf
```bash
blog                    [Status: 301, Size: 326, Words: 20, Lines: 10]
```
Isso indica que o diretório **/blog** existe.

## Aumentando a Velocidade
Podemos aumentar o número de **threads** para acelerar o processo:
```bash
ffuf -w <wordlist> -u <URL> -t 200
```
⚠ **Cuidado:** Isso pode sobrecarregar o site e causar um **Denial of Service (DoS)**.

## Próximos Passos
Se encontrarmos um diretório, podemos explorá-lo manualmente ou usar fuzzing para descobrir arquivos ocultos dentro dele.


---

# Fuzzing de Página com FFUF

## Introdução
- O **ffuf** é usado para fuzzing de diretórios, arquivos e extensões.
- Podemos descobrir páginas ocultas em um site analisando extensões e arquivos.

---

## Fuzzing de Extensão
1. Descubra quais tipos de páginas o site usa (.html, .php, .aspx, etc.).
2. Utilize uma lista de palavras para testar diferentes extensões.

### Comando:
```bash
ffuf -w /opt/useful/seclists/Discovery/Web-Content/web-extensions.txt:FUZZ \
     -u http://SERVER_IP:PORT/blog/indexFUZZ
```

**Explicação:**
- `web-extensions.txt` contém as extensões mais comuns.
- `indexFUZZ` testa várias extensões no arquivo `index`.
- Se receber **200 OK**, significa que a extensão existe.

### Exemplo de saída:
```bash
.php  [Status: 200, Size: 0]
.phps [Status: 403, Size: 283]
```
- `.php` está presente e acessível.
- `.phps` existe, mas está restrito.

---

## Fuzzing de Arquivos PHP
- Após descobrir a extensão, testamos arquivos ocultos.
- Usamos `.php` e uma lista de palavras com possíveis nomes de arquivos.

### Comando:
```bash
ffuf -w /opt/useful/seclists/Discovery/Web-Content/directory-list-2.3-small.txt:FUZZ \
     -u http://SERVER_IP:PORT/blog/FUZZ.php
```

### Exemplo de saída:
```bash
index    [Status: 200, Size: 0]
admin    [Status: 200, Size: 465]
```
- `index.php` é vazio.
- `admin.php` contém conteúdo e pode ser útil para exploração.

---

## Conclusão
- Fuzzing ajuda a encontrar arquivos ocultos e potenciais pontos de entrada.
- Combine listas de palavras adequadas para melhorar os resultados.
- Sempre analise as respostas do servidor (códigos HTTP e tamanho da resposta).

---
