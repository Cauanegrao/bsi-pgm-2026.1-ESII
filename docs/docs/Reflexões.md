Nesta implementação, a decisão de fronteira mais desafiadora foi definir o limite exato entre o ServicoEmprestimo e o Notificador. 

A dificuldade residiu no receio de gerar um acoplamento desnecessário. Se o serviço conhece detalhes demais da mensagem, ele acaba assumindo 
uma responsabilidade de interface que não lhe pertence. No fim, decidi que o ServicoEmprestimo apenas "dispara" o evento de sucesso, enquanto 
o Notificador encapsula a forma como essa informação chega ao usuário.

Essa decisão foi sustentada pela ideia de Coesão discutida por Valente (Capítulo 5, Seção 5.1). Valente argumenta que uma classe coesa deve ter 
uma única responsabilidade bem definida. Ao isolar o Notificador, garanti que mudanças na forma de comunicação não exijam alterações na lógica 
de cálculo de datas ou verificação de disponibilidade do serviço. 


## Aula 06 — DIP

A aplicação do Princípio da Inversão de Dependência (DIP) altera profundamente a arquitetura de software, promovendo uma mudança que vai muito além de uma simples parametrização técnica de construtores. Conceitualmente, ocorre uma completa inversão no controle e no fluxo de poder do sistema: o módulo de alto nível (`ServicoEmprestimo`) deixa de ser subordinado e acoplado aos detalhes operacionais de baixo nível (`Repositorio` e `Notificador`). Conforme ensina Valente no Capítulo 5 de *Engenharia de Software Moderna*, a inversão reside no fato de que "classes de alto nível não devem depender de classes de baixo nível; ambas devem depender de abstrações". Antes do DIP, os módulos de infraestrutura ditavam indiretamente como o serviço deveria se comportar e impediam sua evolução isolada. Com a inversão, é a lógica de negócio que define o contrato e os métodos que as ferramentas externas de persistência e comunicação são obrigadas a implementar. Essa transição de "criador" para "consumidor" liberta o núcleo do domínio da aplicação, transformando a dependência em uma conexão maleável e permitindo a testabilidade isolada do sistema por meio de dublês de teste.


## Aula 10 — Factory e Facade

1. Centralização da Criação com Simple Factory
A introdução da `EquipamentoFactory` resolveu o problema do acoplamento direto espalhado pelo código. Anteriormente, os controladores ou repositórios precisavam instanciar diretamente classes como `Notebook`, `Projetor` ou `Cabo`. Agora, o cliente do código está completamente desacoplado das implementações concretas; apenas a fábrica conhece essas classes. Se um novo tipo de equipamento precisar ser adicionado ao sistema futuramente, o impacto será isolado exclusivamente no escopo da fábrica, respeitando o princípio de responsabilidade única.

### 2. Simplificação e Delegação com Facade
O padrão `Facade` eliminou a complexidade estrutural de coordenação do arquivo `main.py`. Em vez do arquivo principal interagir individualmente com múltiplos subsistemas (serviço de empréstimo, validador de elegibilidade e calculadora de multas), ele passa a realizar chamadas simples através da fachada. A fachada atua estritamente delegando as responsabilidades aos serviços especialistas, garantindo que não se torne um "God Object" (objeto que centraliza regras de negócio). O Princípio da Inversão de Dependência (DIP) foi integralmente preservado, permitindo que a suíte de testes continue injetando dublês nos serviços de forma limpa e isolada, mantendo todos os testes verdes.
