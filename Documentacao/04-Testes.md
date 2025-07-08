# Testes do Projeto

  Os primeiros testes do projeto foram focados na verificação individual dos componentes principais: servo motor, LEDs, sensor ultrassônico, balança com módulo HX711, bomba d'água e aquecedor 12V.

  Durante essa fase, enfrentamos algumas dificuldades significativas. A balança, por exemplo, exigia um valor de tara muito específico, difícil de ser calibrado corretamente, pois sua precisão dependia da angulação e do peso do suporte em que estava instalada. Isso fez com que só conseguíssemos integrá-la ao sistema corretamente após a montagem final da estrutura.

  Já o primeiro aquecedor adquirido apresentou desempenho insuficiente: sua bobina era muito fina e não conseguia aquecer a água de forma eficaz. Substituímos por um aquecedor mais potente, que, por sua vez, exigia uma corrente de 8A, maior do que a fornecida pela nossa fonte de 12V original. Adquirimos uma nova fonte com capacidade para 10A, porém os fios utilizados nas ligações com o relé – responsável por controlar tanto a bomba quanto o aquecedor – não suportaram a nova amperagem. Durante os testes, os fios começaram a derreter.

  Foi necessário refazer toda a fiação do relé com cabos apropriados para a corrente utilizada. Após esses ajustes, conseguimos fazer todos os componentes funcionarem corretamente e de forma sincronizada, de acordo com a lógica definida para o preparo automatizado do café.
