
## Instruções de utilização

Ao ligar o projeto, a primeira mensagem exibida ao usuário será uma solicitação para ligar o aquecedor, já que o café só pode ser preparado quando a água estiver a uma temperatura acima de 60 °C, sendo 75 °C a ideal.

Após o aquecedor ser ativado, o sensor de temperatura começará a enviar dados continuamente até que a temperatura desejada seja atingida.

Quando a água estiver devidamente aquecida, o usuário deve posicionar a caneca no suporte da balança. O sensor de distância detectará a presença da caneca, e então o sistema irá abrir o servomotor e iniciar a pesagem do pó de café. O servo permanecerá aberto até que a quantidade ideal de pó seja dispensada na caneca.

Em seguida, o servomotor será fechado automaticamente e a bomba d’água será acionada para adicionar a quantidade correta de água quente. O sistema continuará monitorando o peso total (caneca + pó + água) até que o valor programado seja atingido, momento em que a bomba será desligada e o processo finalizado.

Além do preparo automático, o usuário também pode ligar manualmente o aquecedor, a bomba e o servomotor a qualquer momento, por meio do aplicativo (via tópicos publish dos atuadores/sensores), para fins de manutenção e limpeza dos componentes da cafeteira.
