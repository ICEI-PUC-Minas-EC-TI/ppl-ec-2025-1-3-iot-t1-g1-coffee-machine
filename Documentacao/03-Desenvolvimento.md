
# Materiais

Os materiais utilizados no projeto foram:

Microcontrolador:

- ESP32

Sensores:

- Módulo HX711 (para balança)
- Sensor ultrassônico
- Sensor de temperatura da água

Atuadores:
- Bomba d'água
- Aquecedor 12V
- Servo motor
- Relé
- LEDs RGB

Estrutura:
- Potes de aço inoxidável
- Funil de aço inoxidável
- Suportes de aço inoxidável
- MDF
- Parafusos

# Desenvolvimento
O desenvolvimento do projeto foi inicialmente focado na criação da lógica de funcionamento dos componentes eletrônicos — sensores e atuadores — responsáveis por automatizar o preparo do café. Após essa etapa, os componentes foram integrados à estrutura física da cafeteira, e então ajustamos os detalhes relacionados à pesagem, à quantidade de água e à dosagem de café solúvel, a fim de obter um resultado satisfatório.

Cada componente foi testado individualmente e ajustado para funcionar de forma coerente com a lógica previamente definida. O sistema opera da seguinte maneira:

- Aquecimento da água: realizado por um aquecedor 12V, até a temperatura ideal ser alcançada;
- Medição da quantidade de água: feita por uma balança com módulo HX711, que detecta o peso da xícara com a água;
- Detecção da presença da xícara: realizada por um sensor ultrassônico posicionado na base;
- Leitura da temperatura da água: feita por um sensor específico, com indicação visual no LED RGB, que muda de cor de acordo com a temperatura;
- Controle do fluxo de café: um servo motor com uma pequena placa de plástico acoplada atua como uma “válvula” no pote de café solúvel. Ele abre para liberar o café quando o preparo é iniciado, e se fecha automaticamente ao atingir o peso ideal da xícara com o café pronto.

O resultado é um sistema totalmente automatizado, sincronizado e adaptado para entregar um café pronto com o mínimo de intervenção do usuário. Mas ainda sim ele é capaz de mecher em cada componente pelo aplicativo caso deseje.

## Desenvolvimento do Aplicativo

### Interface

Descreva o desenvolvimento das telas do aplicativo.

### Código

Descreva o desenvolvimento do código do aplicativo.

## Desenvolvimento do Hardware

### Montagem

Descreva como foi o processo da montagem do projeto.

### Desenvolvimento do Código

Descreva como foi o desenvolvimento do código do arduino/ESP.

## Comunicação entre App e Hardware

Descreva como foi o processo de comunicação entre App e arduino/ESP.

