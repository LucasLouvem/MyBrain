## Resumo

A **computação em nuvem** permite o acesso a um conjunto compartilhado de recursos de TI sob demanda, reduzindo custos e aumentando a escalabilidade. Assim como qualquer outra infraestrutura de TI, uma infraestrutura na nuvem precisa ser protegida. Esta leitura explora os principais desafios de segurança na nuvem e o modelo de responsabilidade compartilhada.

## Considerações sobre a Segurança na Nuvem

Muitas empresas adotam a nuvem devido à facilidade de implantação, custo reduzido e escalabilidade. No entanto, a computação em nuvem apresenta desafios específicos de segurança:

### Gerenciamento de Acesso à Identidade

O **Gerenciamento de Identidade e Acesso (IAM)** garante que apenas usuários autorizados possam acessar recursos da nuvem. Uma configuração incorreta pode permitir acessos indevidos a operações críticas, aumentando o risco de segurança.

**Exemplo:** Se um usuário for acidentalmente configurado como administrador global, poderá acessar e modificar qualquer recurso na nuvem.

### Configuração

Cada serviço na nuvem precisa de configurações precisas para manter a segurança. Erros na configuração são uma das principais causas de violações de segurança.

**Exemplo:** Um bucket de armazenamento mal configurado pode expor dados sensíveis publicamente.

### Superfície de Ataque

A utilização de múltiplos serviços aumenta os pontos de entrada para ataques. Redes mal projetadas podem facilitar a inserção de malware e outros tipos de ameaças.

**Exemplo:** Um serviço de API sem autenticação pode permitir que atacantes acessem dados sensíveis sem restrição.

### Ataques de Dia Zero

Ataques de dia zero exploram vulnerabilidades desconhecidas. Provedores de nuvem costumam detectar e corrigir essas falhas mais rapidamente que empresas tradicionais.

**Exemplo:** Se um hipervisor for comprometido, o CSP pode migrar cargas de trabalho para hosts seguros antes que o ataque se espalhe.

### Visibilidade e Rastreamento

A visibilidade do tráfego de rede pode ser limitada na nuvem. Muitas empresas dependem de ferramentas de monitoramento fornecidas pelos CSPs para detectar anomalias e possíveis ataques.

**Exemplo:** Registros de fluxo podem ser usados para detectar tráfego incomum, indicando um possível ataque.

### Mudanças Rápidas na Nuvem

Os CSPs atualizam constantemente suas infraestruturas, impactando configurações de segurança. Organizações precisam se adaptar rapidamente a essas mudanças.

**Exemplo:** Atualizações de segurança podem exigir ajustes em permissões de firewall ou políticas de acesso.

## Modelo de Responsabilidade Compartilhada

A segurança na nuvem segue um **modelo de responsabilidade compartilhada**:
- **O CSP é responsável** pela segurança da infraestrutura da nuvem, incluindo data centers, hipervisores e hardware.
- **O usuário é responsável** pela configuração e proteção dos dados, aplicativos e acessos dentro da nuvem.

**Exemplo:** O CSP garante a segurança física dos servidores, mas a empresa deve configurar corretamente permissões e criptografia para proteger seus dados.

## Conclusão

A segurança na nuvem exige um entendimento claro das responsabilidades e práticas recomendadas. Empresas devem garantir que suas configurações estejam adequadas e acompanhar as mudanças frequentes no ambiente da nuvem. O modelo de responsabilidade compartilhada assegura que tanto os CSPs quanto os usuários saibam exatamente quais são suas obrigações na proteção dos recursos na nuvem.

Próximo Modulo [[Criptografia e segurança na nuvem]]
