# Problemas Identificados — Leitura Inicial do Código

documento de requisitos (RNF03) diz que deveria ser fácil adicionar novos tipos de equipamentos, mas no código eu teria que mexer em vários lugares diferentes e criar várias condições

envio do e-mail, com a devolução e o empréstimo, caso o usuário mude de e-mail, terá de fazer diversas mudanças no sistema

As listas com os nomes dos equipamentos e os registros de empréstimos estão fora da classe do sistema, jogadas no início do arquivo.

---

## Minha leitura inicial

*(Espaço reservado para o estudante preencher)*

Exemplo de entradas:
- "A classe faz muita coisa ao mesmo tempo"
- "Tem código de e-mail misturado com o cálculo de multa"
- "O mesmo cálculo aparece duas vezes no código"
- "As listas de equipamentos estão fora da classe, soltas no arquivo"

---

## Revisão com vocabulário técnico

* O sistema apresenta dificuldade em cumprir o requisito RNF03, pois a falta de uma estrutura polimórfica exige modificações em múltiplos pontos do código para adicionar novos equipamentos, caracterizando um design rígido e pouco coeso.
* Existe uma mistura de responsabilidades onde a lógica de negócio está fundida com os serviços de notificação; este acoplamento viola o Princípio da Responsabilidade Única (SRP), exigindo alterações estruturais sempre que houver mudanças nos dados de contacto ou canais de comunicação.
* A manutenção de listas de dados fora das classes expõe a estrutura interna do sistema ao ambiente global, impedindo o ocultamento de informação e comprometendo a integridade e a segurança dos registos de empréstimos e equipamentos.
