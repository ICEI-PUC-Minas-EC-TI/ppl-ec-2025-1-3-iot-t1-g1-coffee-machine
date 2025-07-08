#include <ESP32Servo.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <HX711.h>
#include <arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

#define TOPICO_SUBSCRIBE_SERVO         "topico_abre_fecha_servo"
#define TOPICO_PUBLISH_TEMPERATURA   "topico_sensor_temperatura_coffee"
#define TOPICO_PUBLISH_DISTANCIA   "topico_sensor_distancia_coffee"
#define TOPICO_PUBLISH_PESO   "topico_sensor_peso_coffee"
#define TOPICO_SUBSCRIBE_BOMBA  "topico_liga_desliga_bomba"
#define TOPICO_PUBLISH_BOMBA  "topico_bomba_dagua"
#define TOPICO_SUBSCRIBE_AQUECEDOR   "topico_liga_desliga_aquecedor"
#define TOPICO_PUBLISH_AQUECEDOR  "topico_rabo_quente_aquecedor"
#define TOPICO_PUBLISH_COFFEE "topico_coffee_pronto"
#define ID_MQTT  "IoT_PUC_COFEE"

#define DT_PIN 32
#define SCK_PIN 33
#define SERVO_PIN 21
#define SENSOR_TEMP 19
#define LED_BLUE 25
#define LED_GREEN 26
#define LED_RED 27
#define LED_SERVO 15
#define BOTAO_SERVO 35
#define LED_BALANCA 2
#define TRIG 23
#define ECHO 22
#define BOMBA_PIN 14
#define AQUECEDOR_PIN 13

bool aquecedor_ligado = false;
bool esta_aquecido = false;

const char* BROKER_MQTT = "test.mosquitto.org";
int BROKER_PORT = 1883;

const char* SSID = "Fernanda de Mello's Galaxy S22";
const char* PASSWORD = "nqun2677";

HX711 scale;
Servo meuServo;
OneWire oneWire(SENSOR_TEMP);
DallasTemperature sensors(&oneWire);

WiFiClient espClient;
PubSubClient MQTT(espClient);

void initWiFi(void)
{
  delay(10);
  Serial.println("------Conexao WI-FI------");
  Serial.print("Conectando-se na rede: ");
  Serial.println(SSID);
  Serial.println("Aguarde");

  reconnectWiFi();
}

void initMQTT(void)
{
  MQTT.setServer(BROKER_MQTT, BROKER_PORT);   //informa qual broker e porta deve ser conectado
  MQTT.setCallback(mqtt_callback);
}

void mqtt_callback(char* topic, byte* payload, unsigned int length)
{
  String msg;
  String ele = "L";

  /* obtem a string do payload recebido */
  for (int i = 0; i < length; i++)
  {
    char c = (char)payload[i];
    msg += c;
  }

  Serial.print("Chegou a seguinte string via MQTT: ");
  Serial.println(msg);
  
  if(msg[0] == 'A')
  {
    digitalWrite(LED_SERVO, HIGH);
    meuServo.write(90);
    Serial.println("Servo aberto (90°)");
  }
  else if(msg[0] == 'F')
  {
    digitalWrite(LED_SERVO, LOW);
    meuServo.write(0);
    Serial.println("Servo fechado (0°)");;
  }
  else if(msg[0] == 'L' && msg[5] == 'A')
  {
    digitalWrite(AQUECEDOR_PIN, LOW);
    Serial.println("Aquecedor Ligado!");
    MQTT.publish(TOPICO_PUBLISH_AQUECEDOR, "Aquecedor Ligado!");
    aquecedor_ligado = true;
  }
  else if(msg[0] == 'D' && msg[8] == 'A')
  {
    digitalWrite(AQUECEDOR_PIN, HIGH);
    Serial.println("Aquecedor Desligado!");
    MQTT.publish(TOPICO_PUBLISH_AQUECEDOR, "Aquecedor Desligado!");
    aquecedor_ligado = false;
  }
  else if(msg[0] == 'L' && msg[5] == 'B')
  {
    digitalWrite(BOMBA_PIN, LOW);
    Serial.println("Bomba Ligada!");
    MQTT.publish(TOPICO_PUBLISH_BOMBA, "Bomba Ligada!");
  }
  else if(msg[0] == 'D' && msg[8] == 'B')
  {
    digitalWrite(BOMBA_PIN, HIGH);
    Serial.println("Bomba Desligada!");
    MQTT.publish(TOPICO_PUBLISH_BOMBA, "Bomba Desligada!");
  }
  else
    Serial.println("Não identificou comando MQTT");
  
}

void reconnectMQTT(void)
{
  while (!MQTT.connected())
  {
    Serial.print("* Tentando se conectar ao Broker MQTT: ");
    Serial.println(BROKER_MQTT);
    if (MQTT.connect(ID_MQTT))
    {
      Serial.println("Conectado com sucesso ao broker MQTT!");
      MQTT.subscribe(TOPICO_SUBSCRIBE_SERVO);
      MQTT.subscribe(TOPICO_SUBSCRIBE_BOMBA);
      MQTT.subscribe(TOPICO_SUBSCRIBE_AQUECEDOR);
    }
    else
    {
      Serial.println("Falha ao reconectar no broker.");
      Serial.println("Havera nova tentativa de conexao em 2s");
      delay(2000);
    }
  }  
}

void VerificaConexoesWiFIEMQTT(void)
{
  if (!MQTT.connected())
    reconnectMQTT();

  reconnectWiFi();
}

void reconnectWiFi(void)
{
  if (WiFi.status() == WL_CONNECTED)
    return;

  WiFi.begin(SSID, PASSWORD); // Conecta na rede WI-FI

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(100);
    Serial.println(".");
  }

  Serial.println();
  Serial.print("Conectado com sucesso na rede ");
  Serial.print(SSID);
  Serial.println("\nIP obtido: ");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("\nDisciplina IoT: acesso a nuvem via ESP32");
  delay(1000);

  pinMode(LED_BLUE, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_SERVO, OUTPUT);
  pinMode(LED_BALANCA, OUTPUT);
  pinMode(BOTAO_SERVO, INPUT_PULLDOWN);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(BOMBA_PIN, OUTPUT);
  pinMode(AQUECEDOR_PIN, OUTPUT);

  digitalWrite(BOMBA_PIN, HIGH);
  digitalWrite(AQUECEDOR_PIN, HIGH);

  scale.begin(DT_PIN, SCK_PIN);
  scale.set_scale(40975);
  scale.tare(20);
  Serial.println("Balança calibrada!");
  delay(1000);

  meuServo.attach(SERVO_PIN);
  delay(1000);
  Serial.println("Iniciando sensor DS18B20...");
  sensors.begin();

  Serial.println("Iniciando conexao WI-FI e broker MQTT...");
  initWiFi();
  initMQTT();
}

void loop() {
  char temperatura_str[10] = {0};
  VerificaConexoesWiFIEMQTT();
  digitalWrite(LED_BALANCA, LOW);
  digitalWrite(LED_GREEN, LOW);
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_BLUE, LOW);
  digitalWrite(TRIG, LOW);
 
  int estado = digitalRead(BOTAO_SERVO);
  delay(50);  // Debounce
 
  if (estado == HIGH) {
    digitalWrite(LED_SERVO, HIGH);
    meuServo.write(90);
    Serial.println("Servo aberto (90°)");
  } else {
    digitalWrite(LED_SERVO, LOW);
    meuServo.write(0);
  }

  if(aquecedor_ligado == true) {
    
    sensors.requestTemperatures();
    float temperaturaC = 0;
    for(int i = 0; i < 2; i++) {
      temperaturaC = sensors.getTempCByIndex(0);
    }
  
    if (temperaturaC != DEVICE_DISCONNECTED_C) {
      Serial.print("Temperatura: ");
      Serial.print(temperaturaC);
      Serial.println(" °C");

      String temperatura_str = String(temperaturaC, 2) + "C";
      MQTT.publish(TOPICO_PUBLISH_TEMPERATURA, temperatura_str.c_str());

      if (temperaturaC <= 30) digitalWrite(LED_BLUE, HIGH);
      else if (temperaturaC <= 60) digitalWrite(LED_GREEN, HIGH);
      else digitalWrite(LED_RED, HIGH);

      if (temperaturaC >= 55) {
        Serial.println("Água está aquecida!");
        MQTT.publish(TOPICO_PUBLISH_AQUECEDOR, "Água está aquecida!");
      
        digitalWrite(AQUECEDOR_PIN, HIGH);
        Serial.println("Aquecedor Desligado!");
        MQTT.publish(TOPICO_PUBLISH_AQUECEDOR, "Aquecedor Desligado!");

        esta_aquecido = true;
        aquecedor_ligado = false;
      }    
    } else {
      Serial.println("Sensor não encontrado!");
    }
  } 
  
  if (esta_aquecido == false && aquecedor_ligado == false) {
    Serial.println("Para fazer o café verifique se a temperatura da água está adequada");
    Serial.println("Ligue o aquecedor!");

    MQTT.publish(TOPICO_PUBLISH_AQUECEDOR, "Para fazer o café verifique se a temperatura da água está adequada");
    MQTT.publish(TOPICO_PUBLISH_AQUECEDOR, "Ligue o aquecedor!");
  }

  if (esta_aquecido == true) {
    for(int j = 0; j < 30; j++) {
      Serial.println("Coloque uma caneca!");
      MQTT.publish(TOPICO_PUBLISH_COFFEE, "Coloque uma caneca!");
      // Envia o sinal de disparo
      digitalWrite(TRIG, HIGH);
      delay(500);
      digitalWrite(TRIG, LOW);

      // Lê o tempo do sinal de ECHO
      long duration = pulseIn(ECHO, HIGH);

      // Calcula a distância (em cm)
      long distance = duration * 0.0344 / 2;

      // Exibe a distância na serial
      Serial.print("Distância: ");
      Serial.print(distance);
      Serial.println(" cm");

      String distancia_str = String(distance) + "cm"; 
      MQTT.publish(TOPICO_PUBLISH_DISTANCIA, distancia_str.c_str());

      if(distance < 5) {
        int i = 0;
        delay(1000);

        MQTT.publish(TOPICO_PUBLISH_COFFEE, "Colocando café!");
        Serial.println("Colocando café!");

        digitalWrite(LED_SERVO, HIGH);
        meuServo.write(90);
        Serial.println("Servo aberto (90°)");

        while (i < 15) {
          digitalWrite(LED_BALANCA, HIGH);
          Serial.print("Peso: ");
          float weight = scale.get_units(20);

          Serial.print(weight, 3);
          Serial.println("kg");

          String peso_str = String(weight) + "kg";
          MQTT.publish(TOPICO_PUBLISH_PESO, peso_str.c_str());

          if (abs(weight - 3.20) < 0.07) { //3.20 - 0.05
            digitalWrite(LED_SERVO, LOW);
            meuServo.write(0);
            Serial.println("Servo fechado (0°)");

            digitalWrite(BOMBA_PIN, LOW);
            Serial.println("Bomba Ligada!");
            MQTT.publish(TOPICO_PUBLISH_BOMBA, "Bomba Ligada!");
          }

          if (abs(weight - 4.5) < 0.50) {
            digitalWrite(BOMBA_PIN, HIGH);
            Serial.println("Bomba Desligada!");
            MQTT.publish(TOPICO_PUBLISH_BOMBA, "Bomba Desligada!");
            delay(2000);

            MQTT.publish(TOPICO_PUBLISH_COFFEE, "Agora é só misturar!");
            Serial.println("Agora é só misturar!");
            esta_aquecido = false;
            j = 60;
            break;
          }

          delay(1000);
          i++;
        } 
      } else {
        digitalWrite(LED_BALANCA, LOW);
        Serial.println("Balança desligada.");
        MQTT.publish(TOPICO_PUBLISH_PESO, "Balança desligada!");
      }
      delay(1000);
    }
    esta_aquecido = false;
  }

  MQTT.loop();
  delay(2000);
}
