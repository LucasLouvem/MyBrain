## Introdução

Uma **VPN (Rede Privada Virtual)** é um serviço de segurança que altera o endereço IP público e oculta a localização virtual do usuário, garantindo privacidade ao usar redes públicas como a Internet. As VPNs criam um "túnel virtual" que criptografa os dados em trânsito, permitindo conexões seguras entre computadores e redes não confiáveis.

## Tipos de VPNs

### VPN de Acesso Remoto

- Usada por indivíduos para conectar dispositivos pessoais a servidores VPN.
- Criptografa os dados enviados e recebidos.
- Estabelecida por meio da internet.

**Exemplo:** Usar uma VPN para navegar na internet de forma segura enquanto conectado a uma rede pública Wi-Fi.

### VPN Site a Site

- Usada por empresas para conectar diferentes redes em locais distintos.
- Geralmente utiliza o **IPsec** para criar túneis criptografados entre redes locais.
- Mais complexa para configurar e gerenciar em comparação com VPNs de acesso remoto.

**Exemplo:** Empresas com várias filiais usando VPN Site a Site para integrar suas redes internas de forma segura.

## Protocolos de VPN

### WireGuard

- **Alta velocidade e criptografia avançada**.
- Projetado para ser simples de configurar e manter.
- Usado para conexões **site a site** e **cliente-servidor**.
- Menor código e maior desempenho em comparação com outros protocolos.
- **Código aberto**, o que facilita a implantação e depuração.

**Exemplo:** Usado em serviços de VPN modernos para garantir maior velocidade em atividades como streaming ou download de arquivos grandes.

### IPsec

- **Antigo e mais complexo**.
- Usado para criptografar pacotes de dados e autenticar conexões.
- Suportado por muitos sistemas operacionais devido à sua longa história.
- Embora seguro, é mais difícil de configurar e gerenciar.

**Exemplo:** Frequentemente usado em VPNs corporativas para conectar redes de escritórios diferentes de maneira segura.

## Comparação

|Protocolo|Velocidade|Complexidade|Segurança|Usabilidade|
|---|---|---|---|---|
|**WireGuard**|Alta|Baixa|Avançada|Fácil de configurar e manter|
|**IPsec**|Moderada|Alta|Muito segura|Suporte amplo, porém mais complexo|

**Escolha:**

- **WireGuard** é ideal para quem busca desempenho e simplicidade.
- **IPsec** é preferido para implementações mais tradicionais e seguras em ambientes corporativos.

## Conclusão

- **Protocolos VPN** determinam como os dados se movem entre os dispositivos conectados.
- Existem dois tipos de VPNs: **Acesso Remoto** e **Site a Site**.
- **WireGuard** é mais rápido e fácil de configurar, enquanto o **IPsec** é mais seguro e amplamente suportado.

Próximo Modulo [[Termos do glossário do Curso 3, Modulo 1]]
