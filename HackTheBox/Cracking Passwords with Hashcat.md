# Hashing vs. Encryption

### 📌 Hashing vs. Encryption

## 🔹 Hashing

- **O que é?**
    
    - Converte texto em uma string única e de comprimento fixo.
    - Processo unidirecional (não pode ser revertido para o texto original).
    - Usado para verificar integridade de arquivos (MD5, SHA256) e armazenar senhas (PBKDF2).
    - Algumas funções de hash podem ser baseadas em chave (ex.: HMAC).
- **Ataques contra hashing:**
    
    - Força bruta: comparar hashes de uma lista de senhas comuns.
    - Tabelas arco-íris: pré-computam hashes para acelerar a quebra de senhas.
- **Proteção de senhas em Unix:**
    
    - **SHA-512**: rápido, mas vulnerável a tabelas arco-íris.
    - **Blowfish**: mais seguro que SHA-512, mas mais lento.
    - **BCrypt**: usa um hash lento para dificultar ataques.
    - **Argon2**: moderno, projetado para hashing de senhas, exige mais memória e tempo.
- **Proteção contra ataques:**
    
    - **Salting**: adiciona um valor aleatório à senha antes de aplicar o hash.
    - **Exemplo:**
        
        bash
        
        CopyEdit
        
        `echo -n "p@ssw0rd" | md5sum 0f359740bd1cda994f8b55330c86d845  echo -n "p@ssw0rd123456" | md5sum f64c413ca36f5cfe643ddbec4f7d92d0`
        
    - **Colisões**: alguns algoritmos como MD5 são vulneráveis (diferentes entradas podem gerar o mesmo hash).

---

## 🔹 Encryption

- **O que é?**
    - Transforma dados em um formato ilegível que pode ser revertido (diferente de hashing).
    - Usado para comunicação segura (ex.: HTTPS).
    - Dois tipos: **Simétrica** e **Assimétrica**.

### 🔸 Simetric Encryption

- **Usa a mesma chave para criptografar e descriptografar**.
- **Exemplo (XOR em Python):**
    
    python
    
    CopyEdit
    
    `from pwn import xor print(xor("p@ssw0rd", "secret"))  # Criptografa print(xor(b'\x03%\x10\x01\x12D\x01\x01', "secret"))  # Descriptografa`
    
- **Algoritmos comuns:** AES, DES, 3DES, Blowfish.
- **Vulnerabilidades:** ataques de força bruta, análise de frequência, ataque de padding oracle.

### 🔸 Asymmetric Encryption

- **Usa um par de chaves (pública e privada)**.
- **Chave pública**: usada para criptografar os dados.
- **Chave privada**: usada para descriptografar os dados.
- **Algoritmos comuns:** RSA, ECDSA, Diffie-Hellman.
- **Aplicação:** HTTPS/SSL – usado para comunicação segura entre cliente e servidor.