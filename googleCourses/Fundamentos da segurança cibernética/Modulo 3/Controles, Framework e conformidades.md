## **Relação entre Controles, Frameworks e Conformidade**

1. **Controles**:
    
    - Ferramentas ou processos usados para proteger dados, reduzir riscos e mitigar ameaças específicas.
    - **Exemplo**: Firewalls, criptografia, backups e autenticação multifator (MFA).
2. **Frameworks**:
    
    - Diretrizes amplas que organizam os controles para alcançar objetivos de segurança cibernética.
    - **Exemplo**: O NIST CSF orienta como proteger, detectar, responder e recuperar-se de incidentes.
3. **Conformidade**:
    
    - Adesão a regulamentações externas (leis) e padrões internos para garantir que as práticas de segurança estejam alinhadas com as exigências legais ou industriais.
    - **Exemplo**: GDPR, PCI DSS, HIPAA.

Esses três elementos funcionam juntos:

- **Frameworks** fornecem a estratégia de segurança.
- **Controles** implementam essa estratégia.
- **Conformidade** garante que as práticas sigam as regras e normas aplicáveis.

---

## **Principais Frameworks e Regulamentos**

### **Frameworks NIST (CSF e RMF)**:

1. **NIST Cybersecurity Framework (CSF)**:
    
    - Voltado para a proteção de sistemas e dados contra ameaças cibernéticas.
    - **Cinco Funções Principais**:
        - Identificar, Proteger, Detectar, Responder e Recuperar.
2. **NIST Risk Management Framework (RMF)**:
    
    - Focado na gestão de riscos ao longo do ciclo de vida dos sistemas.
    - Utilizado principalmente por agências governamentais e indústrias regulamentadas.

---

### **Regulamentos e Padrões de Conformidade**

1. **FERC-NERC**:
    
    - Regulamenta organizações relacionadas à infraestrutura elétrica.
    - **Objetivo**: Garantir que redes de energia estejam protegidas contra incidentes cibernéticos e operem de forma confiável.
    - **Requisito**: Cumprir os Padrões de Confiabilidade de Infraestrutura Crítica (CIP).
2. **FedRAMP**:
    
    - Padroniza a segurança e a avaliação de serviços na nuvem para o setor governamental dos EUA.
    - **Requisito**: Provedores de nuvem devem obter certificações para oferecer serviços ao governo.
3. **CIS (Center for Internet Security)**:
    
    - Publica controles acionáveis para proteger sistemas e redes.
    - **Exemplo**: Os 18 controles do CIS ajudam organizações a priorizar ações de segurança com base em ameaças reais.
4. **GDPR (Regulamento Geral de Proteção de Dados)**:
    
    - Lei da União Europeia que protege os direitos de privacidade dos cidadãos da UE.
    - **Requisitos**:
        - Notificar violações de dados em até 72 horas.
        - Garantir transparência sobre como os dados pessoais são usados.
5. **PCI DSS**:
    
    - Padrão global para proteger dados de cartões de pagamento.
    - **Requisitos**:
        - Criptografar dados de cartão.
        - Controlar o acesso a informações sensíveis.
        - Monitorar regularmente redes e sistemas.
6. **HIPAA**:
    
    - Protege dados de saúde nos EUA.
    - **Requisitos**:
        - Garantir privacidade e segurança das informações de saúde protegidas (PHI).
        - Informar os pacientes sobre violações de dados.
7. **ISO (Organização Internacional de Padronização)**:
    
    - Define padrões internacionais de segurança, como o ISO/IEC 27001.
    - **Objetivo**: Melhorar a proteção de dados e processos organizacionais.
8. **SOC 1 e SOC 2**:
    
    - Relatórios usados para avaliar conformidade financeira e segurança de dados em organizações.
    - **Exemplo**: SOC 2 analisa confidencialidade, integridade e disponibilidade de sistemas.
9. **Lei Sarbanes-Oxley (SOX)**:
    
    - Focada em proteger investidores de fraudes contábeis.
    - Inclui requisitos de auditoria e segurança de dados.
10. **Lei Gramm-Leach-Bliley (GLBA)**:
    
    - Protege dados financeiros nos EUA.
    - **Requisito**: Bancos e instituições financeiras devem garantir a privacidade de dados de clientes.

---

## **Outros Programas e Diretrizes**

1. **Ordem Executiva Presidencial 14028**:
    
    - Emitida em 2021 para fortalecer a segurança cibernética dos EUA.
    - Inclui:
        - Uso de autenticação multifator.
        - Implementação de sistemas de detecção de ameaças.
2. **HITRUST**:
    
    - Framework que ajuda as organizações a atenderem aos requisitos da HIPAA.
    - Focado na segurança de dados de saúde.

---

## **Exemplo Prático de Integração**

Imagine uma empresa que processa pagamentos de cartão de crédito e está localizada na UE:

1. **Framework**: Utiliza o NIST CSF para estruturar a segurança.
2. **Controles**:
    - Criptografia para proteger dados de pagamento (PCI DSS).
    - Monitoramento contínuo (CIS).
3. **Conformidade**:
    - Adere ao GDPR para garantir a privacidade de dados.
    - Segue o PCI DSS para proteger informações financeiras.

Essa abordagem garante que a empresa esteja protegida contra ameaças, alinhada às regulamentações e em conformidade com padrões globais.

Próximo Modulo [[Proteção de PII]]