**Funcionamento Básico:**

- O sistema operacional (SO) é o "motor" do computador, permitindo que outros programas funcionem eficientemente.
- Ele gerencia o hardware, simplificando o uso do computador para o usuário.

**Processo de Inicialização:**

- Ao ligar o computador, o hardware é ativado.
- O BIOS/UEFI (microchip) carrega o carregador de inicialização, que inicia o SO.
- Importância para a segurança: O BIOS/UEFI pode ser vulnerável a malware, pois nem sempre é verificado por antivírus.

**Comunicação Usuário-Sistema:**

- O usuário interage com aplicativos, que enviam solicitações ao SO.
- O SO traduz essas solicitações e as direciona para o hardware apropriado.
- O hardware responde ao SO, que envia a resposta de volta ao aplicativo.
- Exemplo:
    - Ao usar a calculadora, o aplicativo envia os números e a operação ao SO.
    - O SO envia o cálculo para a CPU (hardware).
    - A CPU retorna o resultado ao SO, que o exibe no aplicativo.

**Importância para Analistas de Segurança:**

- Compreender o fluxo de processamento ajuda a rastrear eventos de segurança.
- Exemplo: Analisar onde um ataque ocorreu durante a comunicação entre aplicativo, SO e hardware.
- Conhecer o funcionamento do sistema operacional e tão importante para um analista de segurança como o conhecimento do funcionamento de um carro e para um mecânico.

**Principais pontos:**

- O SO age como um intermediário crucial entre o usuário e o hardware.
- O processo de inicialização e a comunicação são áreas importantes para a segurança.
- Analistas de segurança precisam entender esses processos para investigar e prevenir incidentes.

Próximo Modulo [[Solicitações ao sistema operacional]]