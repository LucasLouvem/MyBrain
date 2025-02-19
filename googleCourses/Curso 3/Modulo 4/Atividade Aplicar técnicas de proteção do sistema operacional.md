**Relatório de Incidente de Segurança**

**Seção 1: Identificação dos Protocolos de Rede Envolvidos no Incidente**

Os protocolos de rede envolvidos no incidente incluem:

1. **DNS (Domain Name System)**: Utilizado para resolver os endereços IP dos domínios "yummyrecipesforme.com" e "greatrecipesforme.com".
    
2. **HTTP (Hypertext Transfer Protocol)**: Utilizado para carregar o site comprometido e para realizar o download do arquivo malicioso.
    
3. **TCP (Transmission Control Protocol)**: Responsável pelo estabelecimento da conexão entre o cliente e os servidores web.
    

**Seção 2: Documentação do Incidente**

O incidente foi causado por um ataque de força bruta contra o painel administrativo do site "yummyrecipesforme.com". Um ex-funcionário conseguiu acesso utilizando credenciais padrão não alteradas. Após obter acesso, ele inseriu um código malicioso em JavaScript no código-fonte do site, forçando os visitantes a baixarem um arquivo executável comprometido.

Os logs do **tcpdump** mostram a sequência dos eventos:

1. O navegador do usuário faz uma requisição DNS para "yummyrecipesforme.com" e recebe o endereço IP correspondente.
    
2. O navegador inicia uma conexão HTTP com "yummyrecipesforme.com" e carrega a página.
    
3. O site solicita o download de um arquivo executável alegando ser uma "atualização do navegador".
    
4. Após executar o arquivo, o navegador faz uma nova requisição DNS para "greatrecipesforme.com", um site malicioso.
    
5. O navegador estabelece uma conexão HTTP com "greatrecipesforme.com" e é redirecionado para o site comprometido.
    

**Seção 3: Recomendação para Prevenir Ataques de Força Bruta**

Para evitar ataques de força bruta no futuro, recomenda-se a implementação de autenticação multifator (MFA). Isso adiciona uma camada extra de segurança ao login administrativo, tornando ineficaz a tentativa de descobrir senhas apenas por tentativa e erro. Além disso, deve-se considerar as seguintes medidas adicionais:

- Alterar imediatamente qualquer senha padrão após a configuração inicial do sistema utilizando politicas de Senhas para impedir a criação de senhas fracas.
    
- Implementar um mecanismo de bloqueio de conta após um número excessivo de tentativas de login falhas, diminuindo a chance de ataques de força bruta.
    
- Monitorar ativamente logs de acesso e autenticação para detectar atividades suspeitas, como um usuário acessar de um pais diferente.
	
- Utilizar autenticação de multi-fatores impedindo acessos anômalos. 
    
- Manter os sistemas e plugins atualizados para mitigar vulnerabilidades exploráveis.
    
- Utilizar criptografia com HTTPS para impedir vazamentos de dados.
	
Essas medidas ajudarão a proteger o sistema contra acessos não autorizados e futuros ataques semelhantes.

Próximo Modulo [[Praticas de Hardening de rede]]
