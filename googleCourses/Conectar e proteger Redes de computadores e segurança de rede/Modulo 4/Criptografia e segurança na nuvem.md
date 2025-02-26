# Resumo: Criptografia e Segurança na Nuvem

## 1. Modelo de Responsabilidade Compartilhada e Segurança na Nuvem

As redes em nuvem precisam de proteção semelhante às redes locais, combinando práticas de hardening de segurança e criptografia. As principais estratégias incluem:

- **Gerenciamento de Identidade e Acesso (IAM)**
- **Proteção de hipervisores**
- **Definição de linha de base**
- **Criptografia e eliminação criptográfica**

## 2. Técnicas de Fortalecimento da Segurança na Nuvem

### **Gerenciamento de Acesso à Identidade (IAM)**

IAM gerencia identidades digitais e define permissões para acessar recursos na nuvem. Exemplo: restrição de acesso administrativo a usuários específicos.

### **Hipervisores**

Hipervisores são responsáveis por virtualizar ambientes de software:

- **Tipo 1:** Executado diretamente no hardware do host (ex: VMware ESXi).
- **Tipo 2:** Executado sobre um sistema operacional (ex: VirtualBox).

Os provedores de serviços em nuvem (CSPs) usam hipervisores tipo 1 e fornecem atualizações para evitar ataques como **VM escape**, onde um invasor acessa o hipervisor e outras VMs.

### **Linha de Base**

A linha de base estabelece um padrão seguro para o ambiente de nuvem, ajudando a identificar mudanças indesejadas. **Exemplos:**

- Restringir acesso ao portal de administração.
- Ativar criptografia de arquivos.
- Configurar gerenciamento de senhas seguras.
- Habilitar detecção de ameaças em bancos de dados.

## 3. Criptografia na Nuvem

A criptografia protege dados armazenados e processados na nuvem, garantindo **integridade** e **confidencialidade**.

### **Como Funciona?**

A criptografia transforma dados em **texto cifrado**, que só pode ser lido com a chave correta. Atualmente, a segurança se baseia na proteção da **chave criptográfica**, e não no algoritmo.

**Exemplo:**

- Um arquivo armazenado no Google Drive pode ser criptografado para que apenas usuários autorizados consigam acessá-lo.

### **Eliminação Criptográfica**

Método para apagar dados destruindo suas chaves criptográficas. Sem a chave, os dados se tornam inacessíveis.

**Exemplo:**

- Uma empresa de saúde apaga registros antigos excluindo suas chaves criptográficas.

## 4. Gerenciamento de Chaves

A proteção das chaves criptográficas é essencial para manter a segurança dos dados.

### **Mecanismos de Proteção**

- **TPM (Trusted Platform Module):** Chip que armazena senhas e chaves criptográficas com segurança.
- **CloudHSM (Hardware Security Module):** Dispositivo que armazena chaves e executa operações criptográficas.

Os CSPs geralmente não dão acesso às chaves de criptografia usadas, mas permitem que os clientes forneçam suas próprias chaves para maior controle. Caso uma chave do cliente seja comprometida, o CSP tem pouca capacidade de ajudar.

## 5. Conclusão

Para proteger a segurança na nuvem, é fundamental adotar medidas como:

- **Gerenciamento de identidade e acesso (IAM)**
- **Configuração segura da linha de base**
- **Proteção de hipervisores contra ataques**
- **Uso correto da criptografia para proteger dados**
- **Aplicação da eliminação criptográfica para destruir informações sensíveis**

Essas práticas garantem maior proteção aos dados e ao ambiente de computação em nuvem.

Próximo Modulo [[Termos do glossário Curso 3 Módulo 4]]
