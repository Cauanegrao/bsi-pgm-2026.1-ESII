Nesta implementação, a decisão de fronteira mais desafiadora foi definir o limite exato entre o ServicoEmprestimo e o Notificador. 

A dificuldade residiu no receio de gerar um acoplamento desnecessário. Se o serviço conhece detalhes demais da mensagem, ele acaba assumindo 
uma responsabilidade de interface que não lhe pertence. No fim, decidi que o ServicoEmprestimo apenas "dispara" o evento de sucesso, enquanto 
o Notificador encapsula a forma como essa informação chega ao usuário.

Essa decisão foi sustentada pela ideia de Coesão discutida por Valente (Capítulo 5, Seção 5.1). Valente argumenta que uma classe coesa deve ter 
uma única responsabilidade bem definida. Ao isolar o Notificador, garanti que mudanças na forma de comunicação não exijam alterações na lógica 
de cálculo de datas ou verificação de disponibilidade do serviço. 
