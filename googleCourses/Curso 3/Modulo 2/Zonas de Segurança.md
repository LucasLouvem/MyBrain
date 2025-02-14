### 🔒 **Zonas de Segurança em Redes**

As **zonas de segurança** são segmentos de uma rede criados para proteger a rede interna da Internet. Elas fazem parte da **segmentação de rede**, que divide a rede em partes menores com **regras de segurança e permissões de acesso específicas**. Isso ajuda a:

✅ **Controlar o acesso** entre diferentes áreas da rede  
✅ **Proteger dados sensíveis**  
✅ **Evitar que ameaças se espalhem**

#### **Exemplo:**

📶 Um hotel que oferece Wi-Fi gratuito para hóspedes mantém essa rede separada da rede interna usada pelos funcionários, garantindo que dispositivos externos não acessem sistemas administrativos.

---

### **📌 Tipos de Zonas de Segurança**

As redes podem ser divididas em **zonas controladas e não controladas**:

🔴 **Zona Não Controlada** → Redes externas fora do controle da organização (ex.: Internet).  
🟢 **Zona Controlada** → Redes internas protegidas por firewalls e outras medidas de segurança.

Dentro da **zona controlada**, existem subcategorias:

1️⃣ **Zona Desmilitarizada (DMZ)**  
🔹 Contém serviços voltados ao público, como:

- Servidores Web
- Servidores DNS
- Servidores de e-mail  
    🔹 Serve como **perímetro de segurança** entre a Internet e a rede interna.

2️⃣ **Rede Interna**  
🔹 Contém **dados privados** e sistemas corporativos essenciais.  
🔹 Protegida por firewalls para impedir acessos não autorizados.

3️⃣ **Zona Restrita**  
🔹 Contém informações **altamente confidenciais**.  
🔹 Só pode ser acessada por funcionários com **privilégios especiais**.

---

### **🔥 Como a DMZ é Protegida?**

A **DMZ** fica entre **dois firewalls**:

🛑 **Firewall Externo** → Filtra tráfego da Internet antes de entrar na DMZ.  
🛑 **Firewall Interno** → Impede que um invasor na DMZ acesse a rede interna.  
🛑 **Firewall Adicional** (se houver Zona Restrita) → Protege dados sigilosos contra invasores.

#### **Exemplo:**

🔐 Em um banco, os servidores de Internet Banking ficam na **DMZ**, enquanto os servidores de transações financeiras ficam na **rede interna**. Assim, mesmo que a DMZ seja comprometida, o acesso às contas dos clientes segue protegido.

---

### **🛡️ Controle de Acesso**

Os analistas de segurança **controlam o tráfego** que passa pela DMZ e rede interna restringindo:

✔️ **Endereços IP** permitidos  
✔️ **Portas** de comunicação autorizadas

#### **Exemplo:**

🌍 Apenas conexões **HTTPS (porta 443)** podem acessar o servidor web na DMZ, impedindo ataques em outras portas.

---

### **🎯 Conclusão**

As **zonas de segurança** são essenciais para proteger redes, especialmente em grandes empresas. Elas garantem que apenas **usuários autorizados** acessem determinados recursos, evitando que ameaças se espalhem.


Próximo Modulo [[Subredes e CIDR]]
