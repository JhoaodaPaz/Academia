from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import json

CONFIGURACOES_CONVERSAS = ([
    "/home/jhoao/Downloads/chatterbot/Dialogo/saudacoes.json",
    "/home/jhoao/Downloads/chatterbot/Dialogo/informacoes.json"
])

def iniciar():
    global Bot
    global treiner

Bot = ChatBot("robo de Atendimento da Academia")
treiner = ListTrainer(Bot)

def carregar_conversas():
    conversas = []

    for arquivo_configuracao in CONFIGURACOES_CONVERSAS:
        with open(arquivo_configuracao, "r") as arquivo:
            conversas_configuradas = json.load(arquivo)
            conversas.append(conversas_configuradas["conversas"])

            arquivo.close()

    return conversas

def treinar_robo(conversas):
    global treiner

    for conversa in conversas:
        for mensagens_resposta in conversa:
            mensagens = mensagens_resposta["mensagens"]
            resposta = mensagens_resposta["resposta"]

            print("treinando o robô para responder a: ", mensagens, "com a resposta:", resposta)
            for mensagem in mensagens:
                treiner.train([mensagem, resposta])

if __name__ == "__main__":
    iniciar()

    conversas = carregar_conversas()
    if conversas:
        treinar_robo(conversas)
