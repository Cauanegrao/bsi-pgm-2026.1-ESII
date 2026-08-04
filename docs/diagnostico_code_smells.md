# Diagnóstico de Code Smells e Dívida Técnica - Aula 12

### 1. Obsessão por Primitivos (Primitive Obsession)
- **Onde ocorria:** No sistema de eventos/notificações (`services/servico_emprestimo.py` e observadores).
- **Problema:** O evento era representado por um dicionário genérico (`dict`), sem garantia de chaves obrigatórias e sem validação de tipos.
- **Refatoração aplicada:** Criação da `@dataclass Evento` tipada em `services/evento.py`, garantindo autocompletar e validação em tempo de desenvolvimento.

### 2. Nomes Pouco Reveladores
- **Onde ocorria:** Parâmetros e variáveis internas do `ServicoEmprestimo`.
- **Problema:** Nomes abreviados ou genéricos que dificultavam a leitura sem contexto.
- **Refatoração aplicada:** Padronização e clareza nos nomes das variáveis no fluxo de empréstimo e devolução.

### 3. Ausência de Extração de Funções
- **Onde ocorria:** Lógica de montagem e validação de dicionários dentro dos métodos de negócio.
- **Problema:** Código duplicado e acoplado.
- **Refatoração aplicada:** Isolação do contrato do evento através da classe tipada, facilitando a reutilização e testes.
