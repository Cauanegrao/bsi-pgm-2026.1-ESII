Decomposição em camadas

Classes principais e as razões em que estão em cada camada:

Abaixo estão as classes principais e a razão de estarem em cada camada:

* Equipamento (Camada de Modelos): Esta classe mora aqui porque representa o objeto central do domínio (como Notebook ou Projetor) e os seus dados básicos. Ela é independente de como os dados são salvos ou mostrados.

* RepositorioEmprestimo (Camada de Dados): Mora nesta camada para aplicar o ocultamento de informação. O resto do sistema não precisa de saber se os dados estão numa lista ou num banco de dados; apenas este repositório lida com isso.

* ServicoEmprestimo (Camada de Negócio): Esta é a camada onde moram as regras de negócio. Ela coordena as ações do sistema, como validar a disponibilidade de um item e calcular multas, ligando os modelos aos repositórios.

* Notificador (Camada de Infraestrutura): Mora aqui para isolar a comunicação externa. Seguindo o Princípio da Responsabilidade Única (SRP), se decidirmos mudar o aviso de e-mail para SMS, alteramos apenas esta classe sem mexer nas regras de empréstimo.

Bloco do diagrama 

```mermaid
sequenceDiagram
 actor Atendente
 participant main as main.py
 participant servico as ServicoEmprestimo
 participant repo as RepositorioEmprestimo
 participant notif as Notificador
 Atendente->>main: informa equip_id, nome, email, dias
 main->>servico: registrar(equip_id, nome, email, dias)
 servico->>repo: buscar_equipamento(equip_id)
 repo-->>servico: Equipamento
 alt equipamento disponível
 servico->>repo: salvar_emprestimo(emprestimo)
 servico->>repo: marcar_indisponivel(equip_id)
 servico->>notif: notificar_emprestimo(email, data_devolucao)
 servico-->>main: True
 else equipamento indisponível
 servico-->>main: False
 end
```

