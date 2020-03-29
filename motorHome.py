import Adafruit_DHT
import RPi.GPIO as GPIO
import time
from django.template import loader
from django.http import HttpResponse
import datetime
import sqlite3


def escreveBanco(caminho, temp, umid, pino, agora):
        lid = -1
        if (pino == 23):
            lid = 0
        if (pino == 24):
            lid = 1
        conn = sqlite3.connect(caminho+'db.sqlite3')
        conn.execute("""INSERT INTO controleambiente_ambiente (temperatura, umidade, data, local_id) VALUES (?,?,?,?)""", (temp, umid, agora,lid))
        conn.commit()
        conn.close()
	
def main():	
    # Define o tipo de sensor
    sensor = Adafruit_DHT.DHT22

    GPIO.setmode(GPIO.BOARD)

    # Define a GPIO conectada ao pino de dados do sensor

    pino_sensor1 = 23 # escritorio
    pino_sensor2 = 24 # quarto Maria

    listaSensores = [pino_sensor1, pino_sensor2]
    # Informacoes iniciais
    print ("Lendo os valores de temperatura e umidade (ver.2.0)");


    while(1):
        
       for pino in listaSensores:
           # f = open('sensor_'+str(pino), 'w') # versao nao atualiza os arquivos txt fora do banco
           umid, temp = Adafruit_DHT.read_retry(sensor, pino);
           if umid is not None and temp is not None:
             print ("Sensor " + str(pino) + ": " + "Temperatura = {0:0.2f} Umidade = {1:0.2f}").format(temp, umid);
             conteudo = ("{0:0.2f};{1:0.2f}").format(temp, umid);
             # f.write(conteudo) # versao nao atualiza os arquivos txt fora do banco
             # f.close() # versao nao atualiza os arquivos txt fora do banco
             # data atual
             agora = datetime.datetime.now()
             
             # atualiza sqlite3
             caminho = "/home/pi/Projetos/autohome/home/"
             escreveBanco(caminho, temp, umid, pino, agora)
           else:
             # Mensagem de erro de comunicacao com o sensor
             print("Falha ao ler dados!")
       time.sleep(60)

main()