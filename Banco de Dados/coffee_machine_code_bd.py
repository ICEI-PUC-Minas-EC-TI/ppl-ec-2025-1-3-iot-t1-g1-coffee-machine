import paho.mqtt.client as mqtt

# importe o conector do Python com o MySQL: instalar novamente neste env (environment)
import mysql.connector

# agora é necessário criar um objeto de conexão: encontra o MySQL e informa as credenciais para se conectar ao banco
# instalar novamente o concetor: pip install mysql-connector-python
con = mysql.connector.connect(host='localhost', database='IoT',user='root',password='admin')

# verifique se a conexão ao BD foi realizada com sucesso
if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado com sucesso ao Servidor ", db_info)

    # a partir de agora pode-se executar comandos SQL: para tanto é necessário criar um objeto tipo cursor
    # o cursor permite acesso aos elementos do BD
    cursor = con.cursor()

    # agora você pode executar o seu comando SQL. Por exemplo o comando "select database();" mostra o BD atual selecionado
    cursor.execute("select database();")
    # crio uma variável qualquer para receber o retorno do comando de execução
    linha = cursor.fetchone()
    print("Conectado ao DB", linha)

    # createTable é usada no comando SQL para  criar a tabela dadosIoT, que só tem um registro chamado "mensagem"
    createTable = """
                CREATE TABLE TEMPERATURA (id INT AUTO_INCREMENT, 
                                       temperatura TEXT(512), 
                                       PRIMARY KEY (id));
            """

    # este par try/except verifica se a tabela  já está criada. Se a tabela não existe, cai no try e é criada
    # se existe, cai no except e só mostra a mensagem que  a tabela existe
    try:
        cursor.execute(createTable)
    except:
        print("Tabela TEMPERATURA já existe.")
        pass

    # createTable é usada no comando SQL para  criar a tabela dadosIoT, que só tem um registro chamado "mensagem"
    createTable = """
                CREATE TABLE DISTANCIA (id INT AUTO_INCREMENT, 
                                       distancia TEXT(512), 
                                       PRIMARY KEY (id));
            """

    # este par try/except verifica se a tabela  já está criada. Se a tabela não existe, cai no try e é criada
    # se existe, cai no except e só mostra a mensagem que  a tabela existe
    try:
        cursor.execute(createTable)
    except:
        print("Tabela DISTANCIA já existe.")
        pass

    # createTable é usada no comando SQL para  criar a tabela dadosIoT, que só tem um registro chamado "mensagem"
    createTable = """
                CREATE TABLE PESO (id INT AUTO_INCREMENT, 
                                       peso TEXT(512), 
                                       PRIMARY KEY (id));
            """

    # este par try/except verifica se a tabela  já está criada. Se a tabela não existe, cai no try e é criada
    # se existe, cai no except e só mostra a mensagem que  a tabela existe
    try:
        cursor.execute(createTable)
    except:
        print("Tabela PESO já existe.")
        pass

    # createTable é usada no comando SQL para  criar a tabela dadosIoT, que só tem um registro chamado "mensagem"
    createTable = """
                  CREATE TABLE AQUECEDOR \
                  ( \
                      id        INT AUTO_INCREMENT, \
                      aquecedor TEXT(512), \
                      PRIMARY KEY (id) \
                  ); \
                  """

    # este par try/except verifica se a tabela  já está criada. Se a tabela não existe, cai no try e é criada
    # se existe, cai no except e só mostra a mensagem que  a tabela existe
    try:
        cursor.execute(createTable)
    except:
        print("Tabela AQUECEDOR já existe.")
        pass

    # createTable é usada no comando SQL para  criar a tabela dadosIoT, que só tem um registro chamado "mensagem"
    createTable = """
                  CREATE TABLE BOMBA \
                  ( \
                      id    INT AUTO_INCREMENT, \
                      bomba TEXT(512), \
                      PRIMARY KEY (id) \
                  ); \
                  """

    # este par try/except verifica se a tabela  já está criada. Se a tabela não existe, cai no try e é criada
    # se existe, cai no except e só mostra a mensagem que  a tabela existe
    try:
        cursor.execute(createTable)
    except:
        print("Tabela BOMBA já existe.")
        pass

    # createTable é usada no comando SQL para  criar a tabela dadosIoT, que só tem um registro chamado "mensagem"
    createTable = """
                  CREATE TABLE COFFEE \
                  ( \
                      id    INT AUTO_INCREMENT, \
                      coffee TEXT(512), \
                      PRIMARY KEY (id) \
                  ); \
                  """

    # este par try/except verifica se a tabela  já está criada. Se a tabela não existe, cai no try e é criada
    # se existe, cai no except e só mostra a mensagem que  a tabela existe
    try:
        cursor.execute(createTable)
    except:
        print("Tabela COFFEE já existe.")
        pass

def print_hi(name):
    # mensagem inicial
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# esta função é a função callback informando que o cliente se conectou ao servidor
def on_connect(client, userdata, flags, rc):
    print("Connectado com codigo "+str(rc))

    # assim que conecta, assina um tópico. Se a conexão for perdida, assim que
    # que reconectar, as assinaturas serão renovadas
    client.subscribe("topico_sensor_temperatura_coffee")
    client.subscribe("topico_sensor_distancia_coffee")
    client.subscribe("topico_sensor_peso_coffee")
    client.subscribe("topico_bomba_dagua")
    client.subscribe("topico_rabo_quente_aquecedor")
    client.subscribe("topico_coffee_pronto")

# esta função é a função callback que é chamada quando uma publicação é recebida do servidor
def on_message(client, userdata, msg):
    print("Mensagem recebida no tópico: " + msg.topic)
    print("Mensagem: "+ str(msg.payload.decode()) + "º")

    if(msg.topic == "topico_sensor_temperatura_coffee"):
        # ao receber um dado, insere como um registro da tabela TEMPERATURA
        cursor = con.cursor()
        cursor.execute("INSERT INTO TEMPERATURA (mensagem) VALUES ('{}')".format(str(msg.payload.decode())))
        con.commit()

        cursor.execute("SELECT * FROM TEMPERATURA")
        myresult = cursor.fetchall()
        print(myresult)

        if str(msg.payload.decode().strip()) == "termina":
            print("Recebeu comando termina.")
            if con.is_connected():
                cursor.close()
                con.close()
                print("Fim da conexão com o Banco dadosIoT")

        if str(msg.payload.decode().strip()) == "delete":
            cursor.execute("TRUNCATE TABLE TEMPERATURA")

    if(msg.topic == "topico_sensor_distancia_coffee"):
        # ao receber um dado, insere como um registro da tabela DISTANCIA
        cursor = con.cursor()
        cursor.execute("INSERT INTO DISTANCIA (mensagem) VALUES ('{}')".format(str(msg.payload.decode())))
        con.commit()

        cursor.execute("SELECT * FROM DISTANCIA")
        myresult = cursor.fetchall()
        print(myresult)

        if str(msg.payload.decode().strip()) == "termina":
            print("Recebeu comando termina.")
            if con.is_connected():
                cursor.close()
                con.close()
                print("Fim da conexão com o Banco dadosIoT")

        if str(msg.payload.decode().strip()) == "delete":
            cursor.execute("TRUNCATE TABLE DISTANCIA")

    if (msg.topic == "topico_sensor_peso_coffee"):
        # ao receber um dado, insere como um registro da tabela PESO
        cursor = con.cursor()
        cursor.execute("INSERT INTO PESO (mensagem) VALUES ('{}')".format(str(msg.payload.decode())))
        con.commit()

        cursor.execute("SELECT * FROM PESO")
        myresult = cursor.fetchall()
        print(myresult)

        if str(msg.payload.decode().strip()) == "termina":
            print("Recebeu comando termina.")
            if con.is_connected():
                cursor.close()
                con.close()
                print("Fim da conexão com o Banco dadosIoT")

        if str(msg.payload.decode().strip()) == "delete":
            cursor.execute("TRUNCATE TABLE PESO")


    if (msg.topic == "topico_bomba_dagua"):
        # ao receber um dado, insere como um registro da tabela BOMBA
        cursor = con.cursor()
        cursor.execute("INSERT INTO BOMBA (mensagem) VALUES ('{}')".format(str(msg.payload.decode())))
        con.commit()

        cursor.execute("SELECT * FROM BOMBA")
        myresult = cursor.fetchall()
        print(myresult)

        if str(msg.payload.decode().strip()) == "termina":
            print("Recebeu comando termina.")
            if con.is_connected():
                cursor.close()
                con.close()
                print("Fim da conexão com o Banco dadosIoT")

        if str(msg.payload.decode().strip()) == "delete":
            cursor.execute("TRUNCATE TABLE BOMBA")

    if (msg.topic == "topico_rabo_quente_aquecedor"):
        # ao receber um dado, insere como um registro da tabela AQUECEDOR
        cursor = con.cursor()
        cursor.execute("INSERT INTO AQUECEDOR (mensagem) VALUES ('{}')".format(str(msg.payload.decode())))
        con.commit()

        cursor.execute("SELECT * FROM AQUECEDOR")
        myresult = cursor.fetchall()
        print(myresult)

        if str(msg.payload.decode().strip()) == "termina":
            print("Recebeu comando termina.")
            if con.is_connected():
                cursor.close()
                con.close()
                print("Fim da conexão com o Banco dadosIoT")

        if str(msg.payload.decode().strip()) == "delete":
            cursor.execute("TRUNCATE TABLE AQUECEDOR")

    if (msg.topic == "topico_coffee_pronto"):
        # ao receber um dado, insere como um registro da tabela COFFEE
        cursor = con.cursor()
        cursor.execute("INSERT INTO COFFEE (mensagem) VALUES ('{}')".format(str(msg.payload.decode())))
        con.commit()

        cursor.execute("SELECT * FROM COFFEE")
        myresult = cursor.fetchall()
        print(myresult)

        if str(msg.payload.decode().strip()) == "termina":
            print("Recebeu comando termina.")
            if con.is_connected():
                cursor.close()
                con.close()
                print("Fim da conexão com o Banco dadosIoT")

        if str(msg.payload.decode().strip()) == "delete":
            cursor.execute("TRUNCATE TABLE COFFEE")

if __name__ == '__main__':
    print_hi('Olá Turma.')

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)
    #client.connect("broker.hivemq.com", 1883, 60) # broker alternativo

    # a função abaixo manipula trafego de rede, trata callbacks e manipula reconexões.
    client.loop_forever()
