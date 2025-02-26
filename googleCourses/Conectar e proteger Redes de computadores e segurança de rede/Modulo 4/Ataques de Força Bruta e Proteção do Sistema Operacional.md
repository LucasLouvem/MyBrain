## Introdução
Os ataques de força bruta são um método de tentativa e erro para adivinhar credenciais de acesso. Como essa técnica pode comprometer sistemas, diversas estratégias são usadas para preveni-la, incluindo autenticação forte e proteção do sistema operacional por meio de máquinas virtuais e sandboxes.

---

## Tipos de Ataques de Força Bruta

### 1. Ataque de Força Bruta Simples
O invasor tenta várias combinações de nomes de usuário e senhas até encontrar a correta.

**Exemplo:**
```bash
hydra -l admin -P passwords.txt 192.168.1.10 ssh
```
Este comando usa a ferramenta **Hydra** para testar combinações de senhas em um servidor SSH.

### 2. Ataque de Dicionário
Utiliza listas de senhas comuns e credenciais vazadas para aumentar as chances de sucesso.

**Exemplo:**
```bash
john --wordlist=rockyou.txt --format=raw-md5 hash.txt
```
O comando acima usa o **John the Ripper** para tentar quebrar hashes usando um dicionário.

---

## Avaliação de Vulnerabilidades
### Máquinas Virtuais (VMs)
As **VMs** criam um ambiente isolado para testar vulnerabilidades sem afetar o sistema real.

**Exemplo:**
- **VirtualBox** ou **VMware** podem ser usados para executar ambientes de teste.

### Ambientes Sandbox
Os **sandboxes** executam softwares suspeitos sem comprometer o sistema principal.

**Exemplo:**
- **Cuckoo Sandbox** analisa comportamento de malware de forma segura.

---

## Medidas de Prevenção

### 1. Hashing e Salting
Transforma senhas em valores irreversíveis e únicos.

**Exemplo em Python:**
```python
import hashlib, os

salt = os.urandom(16)
hash_senha = hashlib.pbkdf2_hmac('sha256', b'minha_senha', salt, 100000)
```

### 2. Autenticação Multifator (MFA)
Requer mais de um método para validar o acesso.

**Exemplo:**
- Código enviado por SMS ou aplicativo autenticador (Google Authenticator, Authy).

### 3. CAPTCHA e reCAPTCHA
Previne ataques automatizados ao exigir interação humana.

**Exemplo:**
- Implementação do Google reCAPTCHA em um site.

### 4. Políticas de Senha
Definem regras para aumentar a segurança das senhas.

**Exemplo:**
- Exigir pelo menos 12 caracteres com números e símbolos.

---

## Conclusão
Os ataques de força bruta são uma ameaça constante, mas podem ser mitigados com o uso de VMs, sandboxes e medidas como MFA, CAPTCHA e hashing de senhas. Aplicar boas práticas de segurança é essencial para proteger sistemas contra acessos não autorizados.

Próximo Modulo [[Atividade Aplicar técnicas de proteção do sistema operacional]]
