# Código do App
O aplicativo foi desenvolvido utilizando o MQTT Dash, que permite a criação de interfaces personalizadas para controle de dispositivos via protocolo MQTT, sem a necessidade de programação adicional no aplicativo.

A lógica de funcionamento e os comandos enviados à cafeteira são definidos diretamente no painel do app, por meio de botões, sliders e indicadores configuráveis. A comunicação é realizada utilizando o broker Mosquitto (hospedado em mosquitto.org), com suporte ao protocolo MQTT, e foi integrada à estrutura do projeto por meio da plataforma AWS.

Toda a lógica de automação e resposta aos comandos está implementada no código principal do ESP32, enquanto o app atua como interface de controle remoto, oferecendo praticidade e acessibilidade ao usuário
