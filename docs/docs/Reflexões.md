Nesta implementação, a decisão de fronteira mais desafiadora foi definir o limite exato entre o ServicoEmprestimo e o Notificador. 

A dificuldade residiu no receio de gerar um acoplamento desnecessário. Se o serviço conhece detalhes demais da mensagem, ele acaba assumindo 
uma responsabilidade de interface que não lhe pertence. No fim, decidi que o ServicoEmprestimo apenas "dispara" o evento de sucesso, enquanto 
o Notificador encapsula a forma como essa informação chega ao usuário.

Essa decisão foi sustentada pela ideia de Coesão discutida por Valente (Capítulo 5, Seção 5.1). Valente argumenta que uma classe coesa deve ter 
uma única responsabilidade bem definida. Ao isolar o Notificador, garanti que mudanças na forma de comunicação não exijam alterações na lógica 
de cálculo de datas ou verificação de disponibilidade do serviço. 


## Aula 06 — DIP

A aplicação do Princípio da Inversão de Dependência (DIP) altera profundamente a arquitetura de software, promovendo uma mudança que vai muito além de uma simples parametrização técnica de construtores. Conceitualmente, ocorre uma completa inversão no controle e no fluxo de poder do sistema: o módulo de alto nível (`ServicoEmprestimo`) deixa de ser subordinado e acoplado aos detalhes operacionais de baixo nível (`Repositorio` e `Notificador`). Conforme ensina Valente no Capítulo 5 de *Engenharia de Software Moderna*, a inversão reside no fato de que "classes de alto nível não devem depender de classes de baixo nível; ambas devem depender de abstrações". Antes do DIP, os módulos de infraestrutura ditavam indiretamente como o serviço deveria se comportar e impediam sua evolução isolada. Com a inversão, é a lógica de negócio que define o contrato e os métodos que as ferramentas externas de persistência e comunicação são obrigadas a implementar. Essa transição de "criador" para "consumidor" liberta o núcleo do domínio da aplicação, transformando a dependência em uma conexão maleável e permitindo a testabilidade isolada do sistema por meio de dublês de teste.

## Aula 11

A migração do cálculo de multas de uma estrutura baseada em herança para o padrão Strategy representa uma evolução crítica de design com base no princípio de favorecer a composição em detrimento da herança (Valente, Cap. 6). Na arquitetura anterior (Aula 5), o algoritmo de cálculo estava engessado dentro da hierarquia de tipos de `Equipamento`. Isso gerava um forte acoplamento, impossibilitando que uma nova política de multa (como uma tarifa progressiva ou promocional) fosse aplicada sem a necessidade de inflar ou alterar a estrutura de classes de domínio. 

A composição soluciona esse problema ao isolar o algoritmo volátil em classes de estratégia independentes (`MultaStrategy`), tornando o `Equipamento` um mero contexto que delega a execução. Isso não desfaz o Princípio do Aberto/Fechado (OCP); pelo contrário, ele o mantém e potencializa sob uma nova perspectiva. Agora, o sistema está fechado para modificações em classes existentes de equipamentos e permanentemente aberto para extensões, bastando criar novas classes de estratégia para implementar novas regras de negócio sem impactar o código legado.

### 2. Observer e o Evento-Dict
A introdução do padrão Observer no `ServicoEmprestimo` promoveu melhorias profundas em relação aos princípios SRP, OCP e DIP (Valente, Cap. 6). Quanto ao SRP (Princípio da Responsabilidade Única), o serviço agora foca exclusivamente nas regras de negócio de empréstimo e devolução, deixando de gerenciar canais de envio de notificações. O OCP é atendido porque novos destinos ou mídias de alerta (como SMS ou Logs) podem ser adicionados por meio de novos observers concretos registrados na fachada, sem que uma única linha do serviço precise ser alterada. O DIP (Princípio da Inversão de Dependência) é respeitado na medida em que o `ServicoEmprestimo` (módulo de alto nível) deixa de depender de implementações concretas de envio e passa a interagir estritamente com a abstração `Subject`/`Observer`.

Por outro lado, o tráfego de dados utilizando um dicionário comum (`dict`) introduz manifestamente o code smell de *Primitive Obsession*. Isso ocorre porque dicionários não possuem verificação de tipos em tempo de compilação, tornando a comunicação frágil e propensa a erros caso chaves obrigatórias (como `"email"` ou `"tipo"`) sejam digitadas incorretamente. Apesar disso, o uso do `dict` foi uma decisão pedagógica consciente nesta aula para reduzir a complexidade inicial e isolar o aprendizado na mecânica de comportamento e desacoplamento do padrão Observer, estabelecendo uma dívida técnica controlada que será devidamente refatorada para uma `@dataclass Evento` tipada na próxima aula.


## Aula 12 — Dívida Técnica e Refactoring Seguro

### 1. Dívida Técnica e Aceleração Inicial vs. Custo Contínuo
A dívida técnica é criada quando tomamos atalhos de implementação para entregar valor mais rápido — como utilizar dicionários genéricos (`dict`) em vez de estruturas tipadas para eventos. Embora acelere o desenvolvimento inicial, o custo contínuo surge na forma de falta de autocompletar, erros em tempo de execução (*KeyError*) e dificuldade na manutenção. A refatoração contínua paga essa dívida sem alterar o comportamento externo da aplicação.

### 2. O Papel das Dataclasses na Eliminação da Obsessão por Primitivos
A introdução da `@dataclass Evento` substituiu estruturas fracamente tipadas por uma abstração clara e autodocumentada. Isso elimina a obsessão por primitivos, reduz o acoplamento entre emissor e observador e torna os contratos entre módulos explícitos.

### 3. A Importância da Rede de Segurança (pytest) no Refactoring
A regra de ouro do *refactoring* é que o comportamento externo não deve mudar. Ter uma suíte de testes automatizados (`pytest`) e integração contínua (GitHub Actions) atuando como rede de segurança garante que melhorias internas na qualidade do código possam ser feitas de forma destemida e sem introduzir regressões.
