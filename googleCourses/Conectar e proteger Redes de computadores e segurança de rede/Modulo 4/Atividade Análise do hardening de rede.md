## Parte 1: Selecione até três ferramentas e métodos de hardening para implementar

Diante das vulnerabilidades identificadas na rede da organização de mídia social, as seguintes medidas de hardening deverão ser implementadas:

1. **Política de Gerenciamento de Senhas**: Implementação de um gerenciador de senhas e educação dos funcionários sobre boas práticas de segurança para evitar compartilhar com qualquer pessoa.
    
2. **Configuração Segura de Firewalls**: Criar definições de regras de filtragem para controles de tráfegos na rede.
    
3. **Autenticação Multifator (MFA)**: Implementação da MFA para acessos administrativos e usuários críticos.
    

## Parte 2: Explique suas recomendações

### 1. Política de Gerenciamento de Senhas

Os funcionários que compartilham senhas alem da senha do banco de dados do administrador ainda está definida como padrão, representa um grande risco. Para resolver isso, a organização deve:

- Exigir senhas fortes e únicas.
    
- Utilizar um gerenciador de senhas.
    
- Implementar educação em segurança para conscientização dos funcionários.
    

### 2. Configuração Segura de Firewalls

A organização não possui regras de firewall configuradas, permitindo a entrada e saída irrestrita de tráfego. Para mitigar esse risco, poderão ser adotadas as seguintes medidas:

- Criar regras para bloquear tráfego não autorizado.
    
- Permitir apenas serviços e portas essenciais, desabilitando o que não for utilizado.
    
- Implementar monitoramento de logs para detectar tentativas de intrusão.
    

**Como por exemplo**: Configurar um firewall para bloquear conexões externas não autorizadas na porta 22 (SSH).

### 3. Autenticação Multifator (MFA)

A falta de MFA aumenta significativamente o risco de acessos não autorizados. Para reforçar a segurança, deverá ser implementado:

- MFA obrigatória para todos os acessos administrativos.
    
- Uso de aplicativos de MFA como Google Authenticator ou Microsoft Authenticator.
    
- Proteção contra ataques de phishing e comprometimento de credenciais.
    

**Como por exemplo**: Implementar MFA no acesso ao painel de gerenciamento do banco de dados e sistemas críticos como os de administradores.

Próximo Modulo [[Segurança da rede na nuvens]]

