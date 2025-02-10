Começando por uma varredura de portas para responder a pergunta quantas portas estão abertas. Resposta = **2**;

 ```
 nmap -sS -Pn -n --disable-arp-ping -p- -T5 -D RND:5 -oN ports --stats-every 15s -vv 10.10.11.221

PORT   STATE SERVICE REASON

22/tcp open  ssh     syn-ack ttl 63
80/tcp open  http    syn-ack ttl 63

```

Possuindo uma pagina Web Porém sem acesso para isso foi necessário colocar o endereço IP dentro do arquivo `/etc/hosts` para poder ter um DNS.

Após acessar a página me deparo com uma pagina inicial com login e para se registar e necessário ter um Código de convite onde precisa hacker para obter.

indo dentro de ==**/invite**== podemos visualizar o código fonte e obtemos o seguinte resultado.

Dentro do código fonte temos o seguinte script JavaScript
<script defer src="/js/inviteapi.min.js"></script>

Podendo responder a 2 Pergunta: 
Qual é o nome do arquivo JavaScript carregado pela página /invite que tem a ver com códigos de convite? Resposta => inviteapi.min.js

---

```
eval(function(p,a,c,k,e,d){e=function(c){return c.toString(36)};if(!''.replace(/^/,String)){while(c--){d[c.toString(a)]=k[c]||c.toString(a)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1 i(4){h 8={"4":4};$.9({a:"7",5:"6",g:8,b:\'/d/e/n\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}1 j(){$.9({a:"7",5:"6",b:\'/d/e/k/l/m\',c:1(0){3.2(0)},f:1(0){3.2(0)}})}',24,24,'response|function|log|console|code|dataType|json|POST|formData|ajax|type|url|success|api/v1|invite|error|data|var|verifyInviteCode|makeInviteCode|how|to|generate|verify'.split('|'),0,{}))
```

Como podemos ver o código está ofuscado para isso podemos utilizar o site [UnPacker](https://matthewfl.com/unPacker.html) e embelezar ele com o [JavaScript Deobfuscator](https://deobfuscate.relative.im/) e comenta-lo com o ChatGPT, recebemos a seguinte saída.

```
// Função para verificar um código de convite
function verifyInviteCode(code) {
  
  // Cria um objeto contendo o código a ser verificado
  var formData = { code: code };

  // Realiza uma requisição AJAX para o endpoint de verificação de convite
  
  $.ajax({
    type: 'POST',                 // Método HTTP usado para a requisição
    dataType: 'json',             // Tipo de dado esperado na resposta (JSON)
    data: formData,               // Dados enviados no corpo da requisição (o código)
    url: '/api/v1/invite/verify', // URL do endpoint para verificar o código

    // Função executada em caso de sucesso da requisição
    success: function (response) {
      console.log(response);      // Exibe no console o objeto retornado pela API
    },

    // Função executada em caso de erro na requisição
    error: function (response) {
      console.log(response);      // Exibe no console o objeto de erro retornado
    },
  });
}

// Função para gerar um código de convite
function makeInviteCode() {

 // Realiza uma requisição AJAX para o endpoint que gera o código de convite
  $.ajax({
    type: 'POST',                               // Método HTTP usado para a requisição
    dataType: 'json',                           // Tipo de dado esperado na resposta (JSON)
    url: '/api/v1/invite/how/to/generate',      // URL do endpoint para gerar o código

    // Função executada em caso de sucesso da requisição
    success: function (response) {
      console.log(response);      // Exibe no console o objeto retornado pela API
    },

    // Função executada em caso de erro na requisição
    error: function (response) {
      console.log(response);      // Exibe no console o objeto de erro retornado
    },
  });
}
```

Na terceira pergunta temos:

O endpoint em makeInviteCode retorna dados criptografados. Essa mensagem fornece outro endpoint para consulta. Esse endpoint retorna um valor de código que é codificado com um formato binário muito comum para codificação de texto. Qual é o nome dessa codificação?
- Muitas vezes e Base64, no qual essa e a resposta correta.
Resposta: Base64

Para podermos pegar o Código codificado base64 podemos utilizar o curl, e fazer conexão na API e esperar alguma resposta.

Usando o seguinte comando:
```
curl -X POST "http://2million.htb/api/v1/invite/how/to/generate" -H "Content-Type: application/json"
```
Recemos de resposta um 200 em que o dados está criptografado, Após procurar no ChatGPT foi constatado que estaria em ROT13, podemos utilizar o [CyberChef](https://gchq.github.io/CyberChef/) para resolver isso.
```
{"0":200,"success":1,"data":{"data":"Va beqre gb trarengr gur vaivgr pbqr, znxr n CBFG erdhrfg gb \/ncv\/i1\/vaivgr\/trarengr","enctype":"ROT13"},"hint":"Data is encrypted ... We should probbably check the encryption type in order to decrypt it..."}
```

Após decodificar temos a seguinte saída:

![[Pasted image 20250119003534.png]]

dizendo "In order to generate the invite code, make a POST request to /api/v1/invite/generate", o que significa que devemos fazer uma requisição POST para o novo caminho para buscamos alguma informação relevante. Para isso podemos utilizar novamente o curl.
```
curl -X POST "http://2million.htb/api/v1/invite/generate" -H "Content-Type: application/json"
```
Tendo como resposta um Código codificado em base64:
```
{"0":200,"success":1,"data":{"code":"WlpEV1gtQkZTUTQtTFROVzktQk81Rk8=","format":"encoded"}}
```
Para decodificarmos podemos utilizar a propria ferramenta presente no kali ou online, procurando por base64 decode, aqui utilizei o comando:

- `echo "WlpEV1gtQkZTUTQtTFROVzktQk81Rk8=" | base64 -d`

onde fez a decodificação da nossa chave de convidado e permitindo fazer nosso registro no site.
Gerei uma pessoa no 4devs para poder cadastrar e utilizei o seguinte email e senha para essa maquina 

Email: hesac68844@downlor.com @password: xdKK6y3SQW

levando a pergunta de número 5
Qual é o caminho para o endpoint que a página usa quando um usuário clica em "Connection Pack"? 
Para responder so precisamos ir ate a aba access dentro de labs onde encontramos o botão connection pack onde baixa um arquivo VPN, se colocarmos o mouse em cima podemos visualizar o patch no canto inferior esquerdo do navegador ou clicar com o lado direito do mouse e copia o link.

Resposta = /api/v1/user/vpn/generate


