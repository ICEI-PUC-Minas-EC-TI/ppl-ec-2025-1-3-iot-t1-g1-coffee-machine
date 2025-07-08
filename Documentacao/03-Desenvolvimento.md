
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

A interface de controle foi desenvolvida utilizando o aplicativo MQTT Dash, permitindo o gerenciamento remoto da cafeteira de forma simples e intuitiva.

No aplicativo, criamos uma sessão específica para cada tópico MQTT, organizando os elementos da seguinte forma:

- Subscribe (recebimento de mensagens):
Utilizado para monitorar o status dos atuadores, como o aquecedor, a bomba d'água, o servo motor e os LEDs.

- Publish (envio de comandos):
Feito através de botões e caixas de texto, permitindo o envio de comandos aos sensores e atuadores conectados ao ESP32.

Um dos destaques da interface é a visualização da temperatura da água, exibida em uma roda de cores que varia do azul (frio) ao vermelho (quente), proporcionando uma leitura visual clara e rápida para o usuário.

### Código

O desenvolvimento do aplicativo não exigiu programação direta, pois a principal lógica foi baseada na integração dos tópicos MQTT com o broker Mosquitto.org. Após a criação e configuração dos tópicos, realizamos a inscrição (subscribe) e o envio de comandos (publish) diretamente no MQTT Dash, que fornece uma interface gráfica para controlar e monitorar os dispositivos conectados.

A interface foi montada utilizando os recursos nativos do app, como botões, sliders, caixas de texto e indicadores visuais, configurados para interagir com os tópicos previamente definidos. Dessa forma, o código propriamente dito ficou concentrado no firmware do ESP32, enquanto o aplicativo atua como uma ponte intuitiva entre o usuário e o sistema.

## Desenvolvimento do Hardware

### Montagem

A montagem da parte de hardware foi relativamente simples, apesar de algumas dificuldades enfrentadas com componentes específicos, como a balança e o aquecedor. Esses elementos exigiram ajustes mais cuidadosos para funcionarem corretamente dentro do sistema.

Para a estrutura física do protótipo, utilizamos MDF como base e alguns potes de aço inoxidável, que serviram tanto para o aquecimento da água quanto para o armazenamento do café solúvel. A condução da água quente até a xícara foi feita por meio de tubos plásticos resistentes ao calor, garantindo segurança e funcionalidade.

O maior desafio esteve na integração de todos os componentes dentro da estrutura física, de forma que o sistema funcionasse corretamente, sem comprometer a lógica de automação ou a estabilidade dos elementos mecânicos. Foi necessário cuidado na organização interna para acomodar sensores, fios, relés e atuadores de forma eficiente e segura.

### Desenvolvimento do Código

O desenvolvimento do código seguiu a lógica de funcionamento da cafeteira, considerando tanto o controle individual de cada componente quanto a integração entre eles para formar o processo completo de preparo do café.

Inicialmente, realizamos testes isolados com cada sensor e atuador, garantindo que todos respondessem corretamente aos comandos esperados. Após essa etapa, passamos à construção da lógica principal no bloco loop() do código.

A partir daí, o sistema passou a receber comandos via MQTT para iniciar o preparo do café. Uma vez iniciado, o código executa cada etapa do processo de forma sequencial, enviando mensagens MQTT de feedback para o aplicativo, informando o usuário sobre cada fase: desde a presença da xícara, aquecimento da água, liberação do café, até a finalização com o peso ideal detectado.

Essa abordagem garantiu que o sistema fosse reativo, seguro e fácil de acompanhar por meio da interface no MQTT Dash.

## Comunicação entre App e Hardware

A comunicação entre o aplicativo e o hardware foi realizada por meio do protocolo MQTT, utilizando o broker Mosquitto.org como servidor de mensagens. Para isso, utilizamos um código base fornecido pelo professor Júlio, que serviu como ponto de partida para integrar o ESP32 aos tópicos MQTT.

Os tópicos foram previamente criados e testados via MQTT Box, e posteriormente configurados no aplicativo MQTT Dash para envio (publish) e recebimento (subscribe) de mensagens. Essa estrutura permitiu o controle remoto do sistema, com comandos partindo do app e respostas em tempo real sendo transmitidas pelo ESP32, informando o status de cada etapa do preparo do café.

