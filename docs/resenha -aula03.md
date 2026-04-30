# Resenha Aula 3 — Modelos UML e Design de Componentes
Aluno: Cauã Martins Negrão
**Data:** 29/04/2026
## Questão 1 — Modelos UML como ferramentas de modelagem
### (a) Estrutura × comportamento
O diagrama de classes destaca a estrutura estática: classes, atributos, métodos e relacionamentos (associação, herança, dependência), mas não mostra a ordem das interações nem a dinâmica dos objetos. O diagrama de sequência, por sua vez, modela o comportamento: objetos específicos, ativações retangulares e mensagens em ordem cronológica, omitindo detalhes estruturais como multiplicidades e herança. Valente argumenta (Cap. 4, seção 4.2) que são complementares porque cada um revela uma dimensão diferente 
### (b) Consequência prática
O diagrama de classes apoia decisões de estrutura: definir atributos, métodos, visibilidade e navegabilidade, garantindo coesão. Já o diagrama de sequência orienta decisões de colaboração: qual objeto chama qual método em que ordem, o que revela a necessidade de novos métodos (ex.: verificarDisponibilidade()) e ajuda a distribuir responsabilidades sem vínculos ocultos.
### (c) Aplicação ao UC01
O caso de uso textual diz apenas “sistema verifica disponibilidade e registra empréstimo”. Um diagrama de sequência mostraria objetos concretos (InterfaceEmprestimo, ControladorEmprestimo, RepositorioLivros, Emprestimo) e a ordem exata das mensagens. Revelando a necessidade de métodos como buscarPorISBN e o construtor de Emprestimo detalhes que o texto do caso de uso não explicita.
## Questão 2 — Arquitetura, design e os princípios de decomposição
### (a) Definições
Coesão: Quando as responsabilidades de um módulo estão focadas e relacionadas. Uma classe coesa tem um único propósito e todos os seus métodos contribuem para ele.
Acoplamento: o grau de dependência entre módulos. Baixo acoplamento significa que mudanças em um módulo afetam poucos outros.
Ocultamento de informação: esconder dentro de um módulo tudo o que pode mudar expondo apenas uma interface enxuta e estável.
### (b) Relações entre os princípios
Ocultamento de informação habilita baixo acoplamento porque, ao esconder detalhes internos, a dependência fica restrita à interface pública – mudanças internas não se propagam. Ele se relaciona com coesão: módulos coesos naturalmente ocultam informação, pois têm um assunto único
### (c) Aplicação ao projeto v2.0
* models/: Livro, Usuario, Emprestimo. Representam dados e regras essenciais do domínio, sem vínculo com banco ou interface. Coesão alta e ocultam detalhes como cálculo de data de devolução.
* repositories/: LivroRepository, EmprestimoRepository. Responsabilidade única: acesso ao banco de dados. Ocultam o mecanismo de persistência, permitindo trocar implementação sem afetar outras camadas.
* services/: EmprestimoService. Coordena a lógica de negócio que envolve múltiplos repositórios. 
* main.py: apenas configuração e injeção de dependências. Não contém lógica de negócio; é o ponto que conecta as camadas, respeitando inversão de dependências.
## Questão 3 — Crítica fundamentada à documentação do sistema legado
### (a) Pontos frágeis
Violação de ocultamento de informação e coesão. A classe Sistema acessa diretamente variáveis globais equipamentos e emprestimos_registrados (Cap. 5, seção 5.3). Gerando acoplamento ruim: qualquer mudança no formato dessas listas quebra os métodos.
### (b) Ponto forte
O código é simples e funcional para prototipagem rápida cumprindo os requisitos básicos de registrar, devolver e calcular multa. Essa simplicidade, sem classes nem injeção de dependências, pode ser útil em cenários de prova de conceito.
### (c) Síntese
A fragilidade principal está na ausência de modelos que documentem a intenção do projeto. Se o desenvolvedor tivesse esboçado um UML, perceberia que equipamentos e emprestimos_registrados deveriam estar encapsulados em classes Equipamento e Emprestimo, e que o cálculo de multa deveria ser um método coeso.
## Questão 4 — Tipos como contratos: dicionários × classes
### (a) Prevenção de erros
Usando dicionários,como em emprestimos.py, erros de digitação em chaves só aparecem em execução, muitas vezes tarde. Valores podem ter tipos inconsistentes Ex.: True virar "sim") sem aviso prévio. Com classes, atributos são declarados e verificados antes da execução.
### (b) Capacidade de evolução
Uma classe pode ganhar um método calcular_multa() sem afetar seus clientes, pois o contrato público permanece o mesmo com o mesmo nome e o  mesmo retorno. Com dicionário, qualquer lógica nova exige funções externas que manipulam o dicionário.
### (c) Comunicação do design
O nome de um tipo Equipamento comunica a intenção de domínio. Um dicionário genérico não diz nada: poderia ser qualquer coisa. Valente argumenta no Cap. 4, introdução sobre modelos, que clareza de modelo é parte do projeto, não estilo, porque o modelo (nome, interface, responsabilidades) serve como documentação viva para desenvolvedores. 
