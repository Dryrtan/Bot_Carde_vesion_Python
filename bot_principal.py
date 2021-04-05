# coding: utf-8
#!/bin/python3

import time
import requests
import sys
import os
import time

diretorio_principal = '/home/****/irclogs/Chknet/#brasil.log' # O diretório de usuario e local de logs exemplo: "/home/fulando/irclogs/Chknet/#brazil.log"
arquivo_filtrado = '/home/****/irclogs/Chknet/data.txt' # Local dos dados gravados de preferencia coloque o mesmo local do diretorio_principal

while True:
        time.sleep(1)
        os.system('egrep "<%" ' + diretorio_principal + ' > ' + arquivo_filtrado)
        arq = open(arquivo_filtrado, 'r')

        def telegram_bot_sendtext(bot_message):
                bot_token = '*****' # token do bot
                bot_chatID = '****' # local onde receber as menssagens
                send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

                response = requests.get(send_text)

                return response.json()
        qtn_linhas = len(arq.readline())
        contador_de_linhas = 0

        with open(arquivo_filtrado) as file:
            for line in file:
                #print(line)
                #Seleciona as BINs
                if 'BIN:' in line and '<%' in line.split(' ')[1] and line.split(' ')[4] == '»':
                    bin = line.split(' ')
                    telegram_bot_sendtext(bin[2]+' '+bin[3]+'\nBandeira: '+bin[5]+'\nTipo: '+bin[7]+'\nLimite: '+bin[9]+'\nPais:'+bin[11]+"\n#bin")

                #Seleciona os dados fulls
                if 'RESULTADO' in line and 'CONSULTA:' in line.split(' ')[5] and 'RESULTADO' in line.split(' ')[3]:
                    telegram_bot_sendtext('Dados Full\n'+'Link: '+line.split(' ')[6])
                    #print('Dados Full\n'+'Link: '+line.split(' ')[6])
                    

                #Seleciona todos as CCs aprovadas
                if 'APROVADA!' in line and '<%' in line:
                    telegram_bot_sendtext('CC FULL\n'+line.split(' ')[4]+' '+line.split(' ')[6]+'/'+line.split(' ')[8]+' '+line.split(' ')[10]+'\nNivel: '+line.split(' ')[16].split('|')[0]+'\nBandeira: '+line.split(' ')[12])
                    #print('CC FULL\n'+line.split(' ')[4]+' '+line.split(' ')[6]+'/'+line.split(' ')[8]+' '+line.split(' ')[10]+'\nNivel: '+line.split(' ')[16].split('|')[0]+'\nBandeira: '+line.split(' ')[12])
                    exit(0)
                #Seleciona todos as CCs Reprovadas
                if 'REPROVADA' in line and '<%' in line:
                    telegram_bot_sendtext('CC FULL REPROVADA\n'+line.split(' ')[4]+' '+line.split(' ')[6]+'/'+line.split(' ')[8]+' '+line.split(' ')[10]+'\nNivel: '+line.split(' ')[16].split('|')[0]+'\nBandeira: '+line.split(' ')[12])
                    #print('CC FULL REPROVADA\n'+line.split(' ')[4]+' '+line.split(' ')[6]+'/'+line.split(' ')[8]+' '+line.split(' ')[10]+'\nNivel: '+line.split(' ')[16].split('|')[0]+'\nBandeira: '+line.split(' ')[12])
                    

        os.system("echo '' > "+diretorio_principal)


        arq.close()
