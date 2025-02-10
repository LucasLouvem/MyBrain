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
# Fuzzing Recursivo: Uma Visão Geral

## Introdução

O fuzzing recursivo automatiza a exploração de diretórios e subdiretórios, economizando tempo ao escanear estruturas complexas de sites.

## Sinalizadores Recursivos

- Ao ativar a recursão, o scanner inicia novas verificações em diretórios descobertos.
    
- Sites podem ter uma grande árvore de subdiretórios, tornando o processo demorado.
    
- Definir uma profundidade (**depth**) evita varreduras excessivas em diretórios muito profundos.
    

## Uso do ffuf para Fuzzing Recursivo

- **Habilitar recursão:** `-recursion`
    
- **Definir profundidade:** `-recursion-depth <valor>`
    
    - Exemplo: `-recursion-depth 1` escaneia apenas diretórios principais e subdiretórios diretos.
        
- **Especificar extensão de arquivos:** `-e .php`
    
- **Gerar URLs completos:** `-v`
    

## Consideração Final

Utilizar recursão com profundidade controlada melhora a eficiência da varredura e permite foco em diretórios mais relevantes.

---

# Fuzzing de Subdomínios
## O que são Subdomínios?

Subdomínios são partes de um domínio principal, representando sites ou serviços distintos. Exemplo:

- **photos.google.com** é um subdomínio de **google.com**.

## Como Identificar Subdomínios com o ffuf

Podemos usar o **ffuf** para verificar se um subdomínio existe, testando diferentes entradas e verificando seus registros DNS.

### Requisitos:

1. **Wordlist:** Uma lista de palavras comuns para subdomínios.
2. **Target:** O domínio principal a ser analisado.

### Escolhendo uma Wordlist

No repositório **SecLists**, há listas de subdomínios em:

```
/opt/useful/seclists/Discovery/DNS/
```

Para um teste rápido, podemos usar:

```
subdomains-top1million-5000.txt
```

Se precisarmos de uma busca mais abrangente, podemos usar listas maiores.

### Executando o Fuzzing com ffuf

Podemos usar o ffuf para testar subdomínios da seguinte forma:

```bash
ffuf -u http://FUZZ.website.com -w /opt/useful/seclists/Discovery/DNS/subdomains-top1million-5000.txt -mc 200,302
```

**Explicação:**

- `-u http://FUZZ.website.com` → Substitui "FUZZ" pelos termos da wordlist.
- `-w ...` → Especifica a wordlist.
- `-mc 200,302` → Filtra respostas com códigos HTTP 200 (página encontrada) ou 302 (redirecionamento).

### Considerações

- Podemos melhorar a busca usando listas mais longas.
- Respostas **NXDOMAIN** indicam subdomínios inexistentes.
- Se o alvo bloquear muitas requisições, um **delay** pode ser necessário.

Dessa forma, conseguimos encontrar subdomínios ocultos que podem levar a novas superfícies de ataque!

---
# Vhost Fuzzing

## Diferença entre VHosts e Subdomínios

- **VHosts**: Servem diferentes sites no mesmo servidor e IP.
    
- **Subdomínios**: Podem ter registros DNS públicos e apontar para diferentes servidores.
    
- **Nem todos os VHosts possuem registros DNS públicos**.
    

## Problema com Fuzzing de Subdomínios Tradicional

- Fuzzing de subdomínios tradicionais identifica apenas subdomínios com registros DNS públicos.
    
- Subdomínios privados ou internos não são descobertos pelo método padrão.
    

## Solução: Vhost Fuzzing

- Em vez de depender de registros DNS, testamos diferentes VHosts diretamente no mesmo IP.
    
- O processo envolve modificar cabeçalhos HTTP, especificamente o cabeçalho **Host:**.
    

## Como Realizar Vhost Fuzzing com ffuf

Usamos o sinalizador **-H** para adicionar um cabeçalho HTTP personalizado:

```
ffuf -u http://IP_DO_ALVO -w wordlist.txt -H "Host: FUZZ.site.com"
```

- **-u**: Define a URL base.
    
- **-w**: Especifica a wordlist de possíveis VHosts.
    
- **-H**: Modifica o cabeçalho HTTP Host para testar diferentes VHosts.
    

## Benefício do Vhost Fuzzing

- Descoberta de subdomínios internos e VHosts que não estão em registros DNS públicos.
    
- Identifica possíveis serviços ou aplicações ocultas no mesmo IP.