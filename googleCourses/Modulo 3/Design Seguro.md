## **1. Tríade da CIA**

A tríade da CIA (Confidencialidade, Integridade e Disponibilidade) é o pilar central da segurança da informação e define as metas fundamentais que qualquer sistema de segurança deve alcançar.

### **1.1 Confidencialidade**

- **Objetivo**: Impedir que informações sejam acessadas por pessoas ou sistemas não autorizados.
    
- **Implementações Comuns**:
    
    - **Criptografia**: Protege dados em repouso ou em trânsito.
        - Exemplo: HTTPS para proteger comunicação web.
    - **Controle de Acesso**:
        - Listas de Controle de Acesso (ACLs).
        - Autenticação Multifactor (MFA).
    - **Segregação de Redes**:
        - Separar redes internas (privadas) de redes públicas.
    - **Treinamento de Usuários**:
        - Educação sobre phishing, engenharia social e práticas seguras.
- **Ameaças**:
    
    - Vazamento de dados (data leaks).
    - Acesso não autorizado por credenciais comprometidas.

---

### **1.2 Integridade**

- **Objetivo**: Garantir que os dados sejam exatos e não adulterados, deliberada ou acidentalmente.
    
- **Implementações Comuns**:
    
    - **Hashing**: Usa algoritmos como SHA-256 para verificar a integridade dos dados.
        - Exemplo: Um sistema que valida downloads comparando o hash do arquivo baixado.
    - **Assinaturas Digitais**:
        - Garante que os dados vieram de uma fonte confiável e não foram alterados.
    - **Logs e Auditorias**:
        - Verifica mudanças e identifica comportamentos anômalos.
- **Ameaças**:
    
    - Alteração de dados sem autorização.
    - Corrupção de arquivos devido a falhas de hardware ou ataques.

---

### **1.3 Disponibilidade**

- **Objetivo**: Garantir que os dados e sistemas estejam acessíveis aos usuários autorizados sempre que necessário.
    
- **Implementações Comuns**:
    
    - **Redundância**:
        - Backups frequentes.
        - Servidores redundantes e balanceadores de carga.
    - **Mitigação de Ataques DDoS**:
        - Ferramentas como Cloud flare ou AWS Shield.
    - **Manutenção de Sistemas**:
        - Aplicação de patches para corrigir vulnerabilidades e melhorar desempenho.
    - **Planejamento de Recuperação de Desastres**:
        - Planos de continuidade de negócios (BCP).
- **Ameaças**:
    
    - Ataques DDoS.
    - Desastres naturais ou falhas de hardware.

---

## **2. Framework NIST Cybersecurity (NIST CSF)**

O **NIST Cybersecurity Framework (CSF)** é um guia amplamente adotado que organiza padrões, diretrizes e práticas recomendadas para gerenciar e reduzir os riscos de cibersegurança.

### **2.1 Estrutura do NIST CSF**

Ele é composto de **5 funções principais**, que formam um ciclo contínuo de segurança:

1. **Identificar**:
    
    - Compreender os ativos, sistemas, dados e riscos organizacionais.
    - Exemplos:
        - Inventário de hardware e software.
        - Mapeamento de riscos e impacto nos negócios.
2. **Proteger**:
    
    - Desenvolver e implementar medidas para mitigar riscos.
    - Exemplos:
        - Controles de acesso.
        - Segmentação de redes.
        - Treinamento em conscientização de segurança.
3. **Detectar**:
    
    - Identificar eventos de segurança em tempo real.
    - Exemplos:
        - Sistemas de Detecção e Prevenção de Intrusões (IDS/IPS).
        - Logs centralizados via SIEM (Security Information and Event Management).
4. **Responder**:
    
    - Desenvolver processos para lidar com incidentes.
    - Exemplos:
        - Planos de resposta a incidentes.
        - Comunicação com stakeholders.
5. **Recuperar**:
    
    - Restaurar serviços após um incidente de segurança.
    - Exemplos:
        - Recuperação de backups.
        - Revisão pós-incidente para melhorar os processos.

---

## **3. Agentes de Ameaças**

Um agente de ameaça é qualquer entidade que pode causar um impacto negativo em uma organização. Eles incluem:

### **3.1 Tipos de Agentes**

1. **Internos**:
    
    - Funcionários insatisfeitos ou negligentes.
    - Exemplo: Funcionário que vaza dados confidenciais intencionalmente.
2. **Externos**:
    
    - Hackers, grupos de ransomware, ou concorrentes maliciosos.
    - Exemplo: Ataques de phishing para comprometer credenciais.
3. **Automatizados**:
    
    - Bots ou malwares.
    - Exemplo: Bots que realizam ataques DDoS.
4. **Ameaças Ambientais**:
    
    - Desastres naturais, falhas de hardware.

---

## **4. Frameworks e Controles de Segurança**

### **4.1 Frameworks Populares**

Além do NIST CSF, existem outros frameworks usados globalmente:

1. **ISO/IEC 27001**:
    
    - Focado em sistemas de gestão de segurança da informação (SGSI).
    - Proporciona diretrizes para proteger dados e ativos.
2. **COBIT**:
    
    - Framework de governança de TI.
    - Define responsabilidades para as práticas de segurança.
3. **PCI DSS**:
    
    - Voltado para proteger informações de cartões de crédito.
    - Exigido para empresas que processam pagamentos online.
4. **GDPR**:
    
    - Regulamentação europeia que foca na privacidade e proteção de dados pessoais.

---

### **4.2 Controles de Segurança**

Os controles são divididos em três categorias principais:

1. **Controles Preventivos**:
    
    - Bloqueiam ou minimizam os riscos antes que um incidente ocorra.
    - Exemplo: Firewall, MFA.
2. **Controles Detectivos**:
    
    - Identificam ataques ou atividades suspeitas em tempo real.
    - Exemplo: Monitoramento SIEM.
3. **Controles Corretivos**:
    
    - Agem após um incidente para mitigar danos.
    - Exemplo: Recuperação de backups.

Próximo Modulo [[ Controles, Framework e conformidades]]
